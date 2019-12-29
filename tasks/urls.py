from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path("",views.home,name ='home'),
    path("create/",views.add_subject,name ='add_subject'),
    path("edit/<int:sr_no>",views.edit,name='edit'),
    path("delete/<int:sr_no>/",views.delete,name='delete'),
    path("update/<int:sr_no>/",views.update,name='update')
]
