from django.urls import path
from problems import views

urlpatterns = [
    path('', views.MyProblemsView.as_view()),
    path('<slug:pk>/', views.MyProblemDetailView.as_view(), name="problem-detail"),
]