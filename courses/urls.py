from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.course_list, name="list"),
    path("new/", views.course_create, name="create"),
    path("search/", views.course_search, name="search"),
    path("slug/<slug:slug>/", views.course_by_slug, name="by-slug"),
    path("<int:pk>/", views.course_detail, name="detail"),
    path("<int:pk>/json/", views.course_json, name="json"),
    path("create/", views.course_create, name="create"),
    path("lessons/<int:pk>/", views.lesson_detail, name="detail"),
]

