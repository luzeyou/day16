from django.shortcuts import render

def upload_list(request):
    return render(request, "upload_list.html")