from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('main/',views.main,name="main"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('cart/',views.cart,name="cart"),
    path('payment/',views.payment,name="payment"),
    path('logout/',views.logout,name="logout"),
    path('problem/',views.problem,name="problem")
]
