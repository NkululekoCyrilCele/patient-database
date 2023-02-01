from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Patient
from .forms import PatientForm


def index(request):
    return render(request, 'patients/index.html', {
        'patients': Patient.objects.all()
    })


def PatientView(request, id):
    patient = Patient.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


def addView(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            new_patient_id = form.cleaned_data['patient_id']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_medical_diagnosis = form.cleaned_data['medical_diagnosis']
            new_urine_ph = form.cleaned_data['urine_ph']

            new_patient = Patient(
                patient_id=new_patient_id,
                first_name=new_first_name,
                last_name=new_last_name,
                email=new_email,
                medical_diagnosis=new_medical_diagnosis,
                urine_ph=new_urine_ph
            )
            new_patient.save()
            return render(request, 'patients/add.html', {
                'form': PatientForm(),
                'success': True
            })
    else:
        form = PatientForm()  # blank form
    return render(request, 'patients/add.html', {
        'form': PatientForm()
    })


def edit(request, id):
    if request.method == 'POST':
        patient = Patient.objects.get(pk=id)
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return render(request, 'patients/edit.html', {
                'form': form,
                'success': True
            })
    else:
        patient = Patient.objects.get(pk=id)
        form = PatientForm(instance=patient)
    return render(request, 'patients/edit.html', {
        'form': form
    })


def delete(request, id):
    if request.method == 'POST':
        patient = Patient.objects.get(pk=id)
        patient.delete()
    return HttpResponseRedirect(reverse('index'))
