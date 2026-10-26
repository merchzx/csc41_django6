import json

from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404,HttpResponseBadRequest,JsonResponse
from django.views.decorators.http import require_POST
from django.template.context_processors import request


def home(request):
    return HttpResponse("Hello World")

def hello(request):
    return HttpResponse("Hello")

def article(request,pk):
    if pk not in {1,2,3}:
        raise Http404("Статтю не знайдено")
    return HttpResponse(f"Стаття №{pk}")


def greet(request):
    name = request.GET.get("name","guest")
    return HttpResponse(f"Hello {name}!")

@require_POST
def echo_json(request):
    try:
        data = json.loads(request.body)
    except (ValueError,UnicodeDecodeError):
        return HttpResponseBadRequest("Invalid JSON")
    if not isinstance(data,dict):
        return HttpResponseBadRequest("Waiting JSON Object")
    return JsonResponse({"received":data})\

def status_demo(request):
    response = JsonResponse({"ok":True,"count":3},status=200)
    response["X-Lesson"]="11"
    return response

def go_home(request):
    return redirect("pages:hello")


def hello_name(request):
    context = {
        "student_name": "Олена",
        "technologies": ["Python", "Django", "NumPy"],
        "comment": "<script>alert(1)</script>",
    }
    return render(request, "pages/hello.html", context)
# Create your views here.
