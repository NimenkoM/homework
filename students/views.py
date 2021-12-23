import random

from django.forms import model_to_dict
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from faker import Faker

from students.forms import StudentForm
from students.models import Student


def get_students(request):
    queryset = Student.objects.all()
    return render(request, 'index.html',
                  context={'students': queryset})


def get_student(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
        response = model_to_dict(student)
    except Student.DoesNotExist:
        raise Http404
    return JsonResponse(response)


@require_http_methods(['GET', 'POST'])
def create_students(request):

    if request.method == 'GET':
        fake = Faker()

        data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'age': random.randint(5, 18),
        }

        form = StudentForm(initial=data)

        return render(request, 'create-student.html',
                      context={'form': form})

    form = StudentForm(request.POST)

    if form.is_valid():
        form.save()

        return HttpResponseRedirect(reverse('students-list'))

    return HttpResponse(str(form.errors), status=400)
