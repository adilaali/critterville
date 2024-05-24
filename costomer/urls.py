from django.urls import path
from . import views
app_name='costomer'
urlpatterns = [
    path('',views.index,name='index'),
    path('usersignup', views.usersignup, name='usersignup'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userhome/<int:id>', views.userhome, name='userhome'),
    path('buyerhome/<int:id>', views.buyerhome, name='buyerhome'),
    path('updatebuyer/<int:id>',views.updatebuyer,name='updatebuyer'),
    path('changepasswordbuyer/<int:id>',views.changepasswordbuyer,name='changepasswordbuyer'),
    path('buyerlogout',views.buyerlogout,name='buyerlogout'),
    path('readcategory/<int:id>/<int:uid>',views.readcategory,name='readcategory'),
    path('viewprofile/<int:id>',views.viewprofile,name='viewprofile'),
    path('viewpetdetails2/<int:id>',views.viewpetdetails2,name='viewpetdetails2'),
    path('deleteuser/<int:id>',views.deleteuser,name='deleteuser'),
    path('mail/',views.mail,name='mail'),
]