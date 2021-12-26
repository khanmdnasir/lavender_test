from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('create_mobile/',views.create_mobile,name="create_mobile"),
    path('edit_mobile/<int:id>',views.create_mobile,name="edit_mobile"),
    # path('find_mobile/',views.index,name="find_mobile"),
    path('delete_mobile/<int:id>',views.delete_mobile,name="delete_mobile")
]