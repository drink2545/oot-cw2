from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/',views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('search_result/', views.search_record, name='search_record'),
    path('delete/<int:id>', views.remove_record, name='remove_record'),
    path('update/<int:id>', views.edit, name='update'),
    path('update/edit_record/<int:id>', views.edit_record, name='edit_record')
]