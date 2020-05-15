from django.urls import path

from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('booking',views.booking,name='booking'),
    path('about',views.about,name='about'),
    path('FAQ',views.FAQ,name='FAQ'),
    path('rent',views.rent,name='rent'),
    path('rentyourhouse',views.rentyourhouse,name='rentyourhouse'),

]
