from django import forms
from django.forms import DateInput
from bootstrap_datepicker_plus import DatePickerInput

from .models import Doctors, Nurses, Patients, Appointments, Prescriptions
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from bootstrap_datepicker_plus import DatePickerInput,MonthPickerInput


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = ('name', 'age', 'gender', 'address', 'email', 'phone', 'specialty', 'created_date',)
        GENDER_CHOICES = (
            ('', 'Select a gender'),
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Others', 'Others'),

        )
        date = forms.DateField(
            widget=DatePickerInput(
                options={
                    "format": "mm/dd/yyyy",
                    "autoclose": True
                }
            )
        )


class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurses
        fields = ('name', 'age', 'gender', 'address', 'email', 'phone', 'assigned_doctor', 'created_date',)
        GENDER_CHOICES = (
            ('', 'Select a gender'),
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Others', 'Others'),

        )
        widgets = {
            'gender': forms.Select(choices=GENDER_CHOICES, attrs={'class': 'form-control'}),
        }


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ('name', 'age', 'gender', 'address', 'email', 'phone')
        GENDER_CHOICES = (
            ('', 'Select a gender'),
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Others', 'Others'),

        )
        widgets = {
            'gender': forms.Select(choices=GENDER_CHOICES, attrs={'class': 'form-control'}),
        }


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescriptions
        fields = ('patient', 'doctor', 'date', 'symptoms', 'description', 'pharmacy_address', 'created_date')
        date = forms.DateField(
            widget=DatePickerInput(
                options={
                    "format": "mm/dd/yyyy",
                    "autoclose": True
                }
            )
        )


class AppointmentForm(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    class Meta:
        model = Appointments
        fields = ('patient', 'doctor', 'date', 'time', 'status')
        date = forms.DateField(
            widget=DatePickerInput(
                options={
                    "format": "mm/dd/yyyy",
                    "autoclose": True
                }
            )
        )

