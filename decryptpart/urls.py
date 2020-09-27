from django.urls import path
from . import views

app_name='decryptpart'
urlpatterns = [
    path('',views.loginpage,name="loginpage"),
    path('enterform',views.enterform,name="enterform"),
    path('outputform',views.output,name="outputform")
]
