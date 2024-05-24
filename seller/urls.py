from django.urls import path
from . import views
app_name='seller'
urlpatterns = [
    path('sellerhome/<int:id>',views.sellerhome,name='sellerhome'),
    path('updatepetdetail/<int:uid>/<int:pid>',views.updatepetdetail,name='updatepetdetail'),
    path('sellerlogout',views.sellerlogout,name='sellerlogout'),
    path('listed_products/<int:id>',views.listed_products,name='listed_products'),
    path('deletepet/<int:uid>/<int:pid>',views.deletepet,name='deletepet'),
    path('viewpetdetails/<int:uid>/<int:id>',views.viewpetdetails,name='viewpetdetails'),
]
