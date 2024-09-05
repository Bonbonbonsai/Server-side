from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    email = forms.CharField(label="My email", required=False)
    bio = forms.CharField(label="My bio", widget=forms.Textarea)
    birthdate = forms.DateField(label="My birthdate", widget=forms.SelectDateWidget)