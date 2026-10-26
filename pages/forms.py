from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Ім’я",
        min_length=2,
        max_length=60,
    )
    message = forms.CharField(
        label="Повідомлення",
        min_length=10,
        widget=forms.Textarea(attrs={"rows": 4}),
    )