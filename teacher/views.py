import random

from django.forms import model_to_dict
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from faker import Faker

from teacher.forms import TeacherForm
from teacher.models import Teacher


def get_teachers(request):
    queryset = Teacher.objects.all()
    return render(request, 'teacher.html',
                  context={'teachers': queryset})


def get_teacher(request, teacher_id):
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
        response = model_to_dict(teacher)
    except Teacher.DoesNotExist:
        raise Http404
    return JsonResponse(response)


@require_http_methods(['GET', 'POST'])
def create_teachers(request):

    if request.method == 'GET':
        fake = Faker()

        data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'age': random.randint(18, 65),
        }

        form = TeacherForm(initial=data)

        return render(request, 'create-teacher.html',
                      context={'form': form})

    form = TeacherForm(request.POST)

    if form.is_valid():
        form.save()

        return HttpResponseRedirect(reverse('teacher-list'))

    return HttpResponse(str(form.errors), status=400)
