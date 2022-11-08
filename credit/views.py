from django.shortcuts import render
from django.views import generic

from .models import Client, Credit, Account


class ClientView(generic.ListView):
    model = Client
    template_name = 'clients_view.html'
    context_object_name = 'clients'


class AccountView(generic.ListView):
    model = Account
    template_name = 'accounts_view.html'
    context_object_name = 'accounts'


class CreditView(generic.ListView):
    model = Credit
    template_name = 'credits_view.html'
    context_object_name = 'credits'


class ClientDetailView(generic.DetailView):
    model = Client
    template_name = 'client_detail.html'
