from django.urls import path
from . import views

app_name='decryptpart'
urlpatterns = [
    path('',views.enterform,name="decrypthome"),
    path('outputform',views.output,name="outputform")
]
