from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('student_detail/', views.student_detail, name='student_detail'),
    path('student_list/', views.student_list, name='student_list'),
]
