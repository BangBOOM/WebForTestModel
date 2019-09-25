from django.urls import path,re_path
from show import views

app_name='show'

urlpatterns=[
    path('index.html',views.index,name='index'),
    path('get_res/',views.get_res,name='get_res'),
]