from django.urls import path

from . import views

urlpatterns = [
  path('upload', views.FileView.as_view(), name='file-upload'),
  path('data',views.DataList.as_view(),name='data'),
]