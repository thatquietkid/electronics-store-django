from django.urls import path
from core.views import frontpage, shop, signup, myaccount, edit_myaccount, about
from django.contrib.auth import views
from product.views import product

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('about/', about, name='about'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/edit/', edit_myaccount, name='edit_myaccount'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
]