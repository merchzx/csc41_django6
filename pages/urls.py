from django.urls import path
from . import views


app_name = "pages"
urlpatterns = [
    path("",views.home,name="home"),
path("hello/",views.hello,name="hello"),
path("articles/<int:pk>/",views.article,name="article"),
path("greet/",views.greet,name="greet"),
    path("api/echo/",views.echo_json,name="echo"),
    path("go/",views.go_home,name="go"),
    path("status/",views.status_demo,name="status"),
    path("hello_name/",views.hello_name,name="hello_name")
]

