from django.contrib.auth import views
from django.urls import path

from core.views import frontpage, loja, credito, signup, myaccount, edit_myaccount
from product.views import produto

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/edit', edit_myaccount, name='edit_myaccount'),
    path('loja/', loja, name='loja'),
    path('credito/', credito, name='credito'),
    path('loja/<slug:slug>', produto, name='produto'),
]
