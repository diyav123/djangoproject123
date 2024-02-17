from app1.models import Student
from django import forms

class studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'