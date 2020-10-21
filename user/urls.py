from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),   
    path('logout', views.logout_user ,name='logoutuser'),
    # path('register',views.register,name='register'),
    path('register',views.registerclass.as_view(),name='register')
]