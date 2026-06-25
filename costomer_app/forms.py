from django import forms
from .models import costomer
from django.core.exceptions import ValidationError
import re


class costomerRegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = costomer
        fields = [
            'first_name',
           
            'username',
            'phone',
        ]

    def clean_password(self):
        password = self.cleaned_data.get("password")

        if not password:
            raise ValidationError("Password is required.")
        
        if len(password) < 0:
            raise ValidationError("Password must be at least 8 characters long.")
        '''
       # if not re.search(r"[A-Z]", password):
            raise ValidationError("Password must contain at least one uppercase letter.")

       # if not re.search(r"[a-z]", password):
            raise ValidationError("Password must contain at least one lowercase letter.")

       # if not re.search(r"[0-5s]", password):
            raise ValidationError("Password must contain at least one digit.")

       # if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValidationError("Password must contain at least one special character.")
          '''
        return password

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error(
                "confirm_password",
                "Passwords do not match."
            )

        return cleaned_data

    def save(self, commit=True):
        customer = super().save(commit=False)
        customer.password = self.cleaned_data["password"]

        if commit:
            customer.save()

        return customer