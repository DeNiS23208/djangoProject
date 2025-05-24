from django.views.generic import DetailView
from .models import Student
from .services import StudentService

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        # Получаем стандартный контекст данных из родительского класса
        context = super().get_context_data(**kwargs)
        # Получаем ID студента из объекта
        student_id = self.object.id
        # Добавляем в контекст полное имя, средний балл и статус сдачи предмета
        context['full_name'] = StudentService.get_full_name(student_id)
        context['average_grade'] = StudentService.calculate_average_grade(student_id)
        context['has_passed'] = StudentService.has_passed(student_id)
        return context