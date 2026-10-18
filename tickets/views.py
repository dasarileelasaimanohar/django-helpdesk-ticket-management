
from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm


def ticket_list(request):
    tickets = Ticket.objects.all().order_by('-created_at')

    context = {
        'tickets': tickets,
        'open_count': Ticket.objects.filter(status='open').count(),
        'resolved_count': Ticket.objects.filter(status='resolved').count(),
    }

    return render(request, 'tickets/ticket_list.html', context)




def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            if request.user.is_authenticated:
                ticket.created_by = request.user
            else:
                from django.contrib.auth.models import User
                ticket.created_by = User.objects.filter(is_superuser=True).first()

            if ticket.created_by is None:
                form.add_error(None, "Please log in before creating a ticket.")
            else:
                ticket.save()
                return redirect('ticket_list')
    else:
        form = TicketForm()

    return render(request, 'tickets/create_ticket.html', {'form': form})


    

def ticket_detail(request, ticket_id):
    from django.shortcuts import get_object_or_404
    from django.contrib.auth.models import User

    ticket = get_object_or_404(Ticket, id=ticket_id)
    staff_members = User.objects.filter(is_staff=True)

    return render(
        request,
        'tickets/ticket_detail.html',
        {
            'ticket': ticket,
            'staff_members': staff_members,
        }
    )
    
def update_ticket_status(request, ticket_id):
    from django.shortcuts import get_object_or_404
    from django.http import HttpResponseRedirect
    from django.urls import reverse

    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')

        allowed_statuses = ['open', 'in_progress', 'resolved', 'closed']

        if new_status in allowed_statuses:
            ticket.status = new_status
            ticket.save()

        return HttpResponseRedirect(
            reverse('ticket_detail', args=[ticket.id])
        )

    return redirect('ticket_detail', ticket_id=ticket.id)
    
def assign_ticket(request, ticket_id):
    from django.shortcuts import get_object_or_404
    from django.contrib.auth.models import User

    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == 'POST':
        staff_id = request.POST.get('assigned_to')

        if staff_id:
            staff = get_object_or_404(User, id=staff_id, is_staff=True)
            ticket.assigned_to = staff
        else:
            ticket.assigned_to = None

        ticket.save()

    return redirect('ticket_detail', ticket_id=ticket.id)