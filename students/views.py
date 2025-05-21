from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from students.models import Student, MyModel
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden


class ExpelStudentView(LoginRequiredMixin, View):
    def post(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)

        if not request.user.has_perm('students.can_expel_student'):
            return HttpResponseForbidden('У вас нет прав для исключения студента')

        student.delete()

        return redirect('students:student_list')

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "students/student_list.html"
    context_object_name = 'students'

    def get_queryset(self):
        if not self.request.user.has_perm('students.view_student')
            return Student.objects.none()
        return Student.objects.all()



class MyModelCreateView(CreateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')


class MyModelDetailView(DetailView):
    model = MyModel
    template_name = 'students/mymodel_detail.html'
    context_object_name = 'mymodel'


class MyModelUpdateView(UpdateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')

class MyModelDeleteView(DeleteView):
    model = MyModel
    template_name = 'students/mymodel_confirm_delete.html'
    success_url = reverse_lazy('students:mymodel_list')


class MyModelListView(ListView):
    model = MyModel
    template_name = 'students/mymodel_list.html'
    context_object_name = 'mymodels'


def about(request):
    return render(request, "students/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, 'students/contact.html')


def student_detail(request):
    student = Student.objects.get(id=1)
    context = {
        'student': student,
    }
    return render(request, 'students/student_detail.html', context=context)


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/student_list.html', context=context)
