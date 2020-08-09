from django.urls import path
from .views import QuizTest
app_name='Quiz'
urlpatterns = [
    path('',QuizTest.as_view(),name='quiz'),
    path('<str:Title>/',QuizTest.as_view()),
]