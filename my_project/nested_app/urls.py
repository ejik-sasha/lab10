from django.urls import path
from . import views

urlpatterns = [
    path('nested1/', views.nested_view1, name='nested_view1'),
    path('nested2/', views.nested_view2, name='nested_view2'),
]