import os
from django.shortcuts import render, HttpResponse
from django import forms
from django.conf import settings
from app01.utils.bootstrap import BootStrapForm, BootStrapModelForm
from app01 import models


def upload_list(request):
    return render(request, "upload_list.html")


class UpForm(BootStrapForm):
    bootstrap_exclude_fields = ["img"]
    name = forms.CharField(label="姓名")
    age = forms.IntegerField(label="年龄")
    img = forms.FileField(label="头像")


def upload_form(request):
    title = "Form上传"
    if request.method == "GET":
        form = UpForm()
        return render(request, "upload_form.html", {"form": form, "title": title})

    form = UpForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        image_object = form.cleaned_data.get("img")
        media_path = os.path.join("media", image_object.name)
        f = open(media_path, mode="wb")
        for chunk in image_object.chunks():
            f.write(chunk)
        f.close()

        models.Boss.objects.create(
            name=form.cleaned_data["name"],
            age=form.cleaned_data["age"],
            img=media_path,
        )

        return HttpResponse("...")

    return render(request, "upload_form.html", {"form": form, "title": title})


class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ["img"]

    class Meta:
        model = models.City
        fields = "__all__"


def upload_model_form(request):
    title = "ModelForm上传文件"
    if request.method == "GET":
        form = UpModelForm()
        return render(request, "upload_form.html", {"form": form, "title": title})

    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse("成功")

    return render(request, "upload_form.html", {"form": form, "title": title})
