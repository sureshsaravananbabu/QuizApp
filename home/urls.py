from django.urls import path
from .views import CreateQuiz,Home
app_name='Home'
urlpatterns = [
    path('',Home.as_view(),name='quiz'),
    path('create/',CreateQuiz.as_view()),
]