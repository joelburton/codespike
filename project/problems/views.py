from django.shortcuts import render
from django.views import generic
from problems.models import StudentProblem
from students.models import Student


class MyProblemsView(generic.ListView):
    template_name = "problems/studentproblem_list.html"

    def get_queryset(self):
        # return StudentProblem.objects.filter(student=self.request.user).all()
        return StudentProblem.objects.all()


class MyProblemDetailView(generic.DetailView):
    template_name = "problems/studentproblem_detail.html"

    def get_queryset(self):
        return StudentProblem.objects.all()