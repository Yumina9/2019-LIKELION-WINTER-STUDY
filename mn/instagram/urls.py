from django.urls import path
from . import views

# 2버전때부터 필수
app_name = 'instagram'

urlpatterns = [

    # /instagram/
    path('', views.image_list, name='image_list')
]
