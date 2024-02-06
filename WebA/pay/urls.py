from django.urls import path, include,re_path
from . import views
urlpatterns = [
    re_path(r'^$',views.LoginView.as_view(),name='index'),
    re_path(r'^transfer/$',views.TransferView.as_view(),name='transfer'),
]