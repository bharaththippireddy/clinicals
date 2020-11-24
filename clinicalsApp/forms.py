from django import forms
from clinicalsApp.models import ClinicalData,Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields='__all__'

class ClinicalDataForm(forms.ModelForm):
    class Meta:
        model=ClinicalData
        fields='__all__'
