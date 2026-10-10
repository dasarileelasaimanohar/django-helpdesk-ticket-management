
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
    path('create/', views.create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('ticket/<int:ticket_id>/update-status/', views.update_ticket_status, name='update_ticket_status'),
    path('ticket/<int:ticket_id>/assign/', views.assign_ticket, name='assign_ticket'),
]