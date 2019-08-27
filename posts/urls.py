from django.contrib import admin
from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
	path('create/',views.post_create),
    path('',views.post_list),
    path(r'detail/(?P<id>\d+)/',views.post_detail),
    path('update/',views.post_update),
    path('delete/',views.post_delete),
    ]