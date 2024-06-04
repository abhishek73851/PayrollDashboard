# forms.py
from django import forms
from .models import EmpAttendance

class EmpSelectionForm(forms.Form):
    empnum = forms.ModelChoiceField(queryset=EmpAttendance.objects.values_list('empnum', flat=True).distinct())
    month = forms.ChoiceField(choices=EmpAttendance.MONTH_CHOICES)
