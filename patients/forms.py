from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        labels = {
            'patient_id': 'Patient ID',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'medical_diagnosis': 'Medical Diagnosis',
            'urine_ph': 'Urine pH'
        }
        widgets = {
            'patient_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'medical_diagnosis': forms.TextInput(attrs={'class': 'form-control'}),
            'urine_ph': forms.NumberInput(attrs={'class': 'form-control'}),
        }
