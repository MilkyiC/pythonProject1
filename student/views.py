from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation.template import context_re
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView
from django_filters.views import FilterView
from rest_framework import viewsets

from student.models import Student,Book,Passport,Curator,Course,Enrollment
from student import filters
from student import serialazers



class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class=serialazers.Student

class BookApi(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serialazers.Book

class CuratorApi(viewsets.ModelViewSet):
    queryset = Curator.objects.all()
    serializer_class = serialazers.Curator

class CourseApi(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = serialazers.Course

class EnrollmentApi(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = serialazers.Enrollment

class PassportApi(viewsets.ModelViewSet):
    queryset = Passport.objects.all()
    serializer_class = serialazers.Passport




class StudentList(ListView):
    template_name = 'student/student_list.html'
    model = Student
    context_object_name = 'students'

class StudentDetail(DetailView):
    template_name = 'student/student_detail.html'
    model = Student
    context_object_name = 'student'

class StudentCreate(CreateView):
    template_name = 'student/student_create.html'
    model = Student
    fields = ['full_name', 'date_of_birth']
    success_url = reverse_lazy('students')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class StudentUpdate(UpdateView):
    template_name = 'student/student_form.html'
    model = Student
    fields=['full_name','date_of_birth','curator']

    def get_success_url(self):
        return reverse_lazy('student_detail',kwargs={'pk':self.object.pk})

class StudentDelete(DeleteView):
    template_name = 'student/student_confirm_delete.html'
    model = Student
    success_url = reverse_lazy('student_list')
