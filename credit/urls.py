from django.urls import path
from .views import ClientView, AccountView, CreditView, ClientDetailView

urlpatterns = [
    path('clients/', ClientView.as_view(), name='clients'),
    path('clients/<int:pk>', ClientDetailView.as_view(), name='client'),
    path('accounts/', AccountView.as_view(), name='accounts'),
    path('credits/', CreditView.as_view(), name='credits'),


]