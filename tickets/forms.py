
from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
            'category',
            'priority',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter a short title for your issue'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe the problem in detail',
                'rows': 5
            }),
        }