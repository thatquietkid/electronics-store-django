from django.urls import path
from core.views import frontpage, shop, signup
from django.contrib.auth import views
from product.views import product

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
]