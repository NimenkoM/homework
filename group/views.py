import random

from django.forms import model_to_dict
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from faker import Faker

from group.forms import GroupForm
from group.models import Group


def get_groups(request):
    queryset = Group.objects.all()
    return render(request, 'group.html',
                  context={'groups': queryset})


def get_group(request, group_id):
    try:
        group = Group.objects.get(pk=group_id)
        response = model_to_dict(group)
    except Group.DoesNotExist:
        raise Http404
    return JsonResponse(response)


@require_http_methods(['GET', 'POST'])
def create_groups(request):

    if request.method == 'GET':
        fake = Faker()

        data = {
            'group_name': fake.license_plate(),
            'group_direction': fake.language_name(),
            'group_size': random.randint(6, 20),
        }

        form = GroupForm(initial=data)

        return render(request, 'create-group.html',
                      context={'form': form})

    form = GroupForm(request.POST)

    if form.is_valid():
        form.save()

        return HttpResponseRedirect(reverse('group-list'))

    return HttpResponse(str(form.errors), status=400)
