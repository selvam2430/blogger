from django.urls import path
from .views import  *

urlpatterns = [
    path("", test),
    path("homepage/", home, name="home"),
    path("details/<int:pk>/", blogDetails, name="details_page"),
    path('form/',add_blog, name="form_page"),
    path('edit/<int:pk>/',edit_page, name="edit_form_page"),
    path('login/',login_page, name="login_page"),
    path('register/',reg_page, name="reg_page"),
]