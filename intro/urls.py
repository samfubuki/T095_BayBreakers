from django.urls import path
from . import views

app_name='intro'
urlpatterns = [
    path('',views.intro, name="intro"),
    ##path('success/',views.success,name="success"),
]
