from django.urls import path,re_path
from . import views
from django.conf import settings

urlpatterns = [
path('',views.homepage,name='homepage'),
path('profile/',views.profile,name='profile'),
path('newpost/',views.new_post,name='new_post'),
path('newhome/',views.new_neighborhood,name='new_home'),
path('more/<int:id>',views.moreabout_neighborhood,name='more'),
path('newbusiness/',views.new_business,name='new_business'),
path('deletehood/<int:id>',views.deletehood,name='deletehood'),
path('deletebusiness/<int:id>',views.deletebusiness,name='deletebusiness'),
path('search/',views.search,name='search'),
path('deletepost/<int:id>',views.delete_post,name='delete_post'),




]