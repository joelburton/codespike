from django.urls import path
from problems.views import MyProblemsView

urlpatterns = [
    path('', MyProblemsView.as_view()),
]