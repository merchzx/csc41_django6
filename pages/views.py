from django.shortcuts import redirect, render
from .forms import FeedbackForm, OrderForm


def hello(request):
    context = {
        "student_name": "Олена",
        "technologies": ["Python", "Django", "NumPy"],
        "comment": "<script>alert(1)</script>",
    }
    return render(request, "pages/hello.html", context)


def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            return redirect("pages:feedback_success")
    else:
        form = FeedbackForm()
    return render(request, "pages/feedback.html", {"form": form})


def feedback_success(request):
    return render(request, "pages/success.html")


def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            return redirect("pages:order_success")
    else:
        form = OrderForm()
    return render(request, "pages/order.html", {"form": form})


def order_success(request):
    return render(request, "pages/order_success.html")