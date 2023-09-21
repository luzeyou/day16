from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from django import forms
from app01.utils.pagination import Pagination


class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"
        widgets = {
            "detail": forms.TextInput
        }


def task_list(request):
    queryset = models.Task.objects.all().order_by("-id")

    form = TaskModelForm()

    page_object = Pagination(request, queryset)

    context = {
        "form": form,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }

    return render(request, "task_list.html", context)


@csrf_exempt
def task_ajax(request):
    print(request.POST)
    data_dict = {"status": True, "data": [11, 22, 33, 44]}
    return HttpResponse(json.dumps(data_dict))


@csrf_exempt
def task_add(request):
    # print(request.POST)

    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))

    data_dict = {"status": False, "error": form.errors}
    return HttpResponse(json.dumps(data_dict))
