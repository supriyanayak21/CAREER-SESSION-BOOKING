from django import forms
from .models import GuidanceSession

from django.contrib.auth.models import User
from django import forms
from .models import CareerSession

class CareerSessionForm(forms.ModelForm):
    class Meta:
        model = CareerSession
        fields = ['title', 'description', 'date', 'time', 'location', 'seats_available']



class GuidanceSessionForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Enter your email to receive booking details.")
    class Meta:
        model = GuidanceSession
        fields = ['career', 'session_date','email']
        widgets = {
            'session_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")