from django.urls import path
from . import views

urlpatterns = [
    path('redirect/', views.redirect_example, name="redirect_example"),
    path('hello/<str:name>/', views.hello_world, name='hello_world'),
    path('json/', views.json_example,name='json_example'),
    path('cookies/', views.show_cookie,name='show_cookie'),
]
