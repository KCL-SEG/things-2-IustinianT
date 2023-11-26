"""Forms of the project."""
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Thing

# Create your forms here.
class ThingForm(forms.ModelForm):

    class Meta:
        model = Thing
        fields = ["name", "description", "quantity"]
    
    def is_valid(self):
        return super().is_valid()