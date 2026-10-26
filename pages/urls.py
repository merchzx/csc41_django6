from django.urls import path
from . import views


app_name = "pages"
urlpatterns = [
path("hello/",views.hello,name="hello"),
path("feedback/",views.feedback,name="feedback"),
    path("feedback/success/", views.feedback_success, name="feedback_success"),
    path("order/", views.order, name="order"),
    path("order/success/", views.order_success, name="order_success"),

]

