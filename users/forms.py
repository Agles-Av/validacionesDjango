from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel','password1', 'password2']
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'forms-control',
                    'placeholder': 'Ingrese su correo',
                    'required': True,
                    'pattern': '^[0-9]{5}tn[0-9]{3}@utez\.edu\.mx$',
                    'title': 'Ingrese un correo de la UTEZ'
                }
                
            )
        }
    def email_utez(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@utez.edu.mx'):
            raise forms.ValidationError('El correo debe ser de la UTEZ')
        return email
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        pattern = r'^[0-9]{5}tn[0-9]{3}@utez\.edu\.mx$'
        if not email.match(pattern, email):
            raise forms.ValidationError('El correo debe ser institucional de la UTEZ (xxxxxtnxxx@utez.edu.mx)')
        return email
    
    def clean_control_number(self):
        control_number = self.cleaned_data.get('control_number')
        pattern = r'^[0-9]{5}tn[0-9]{3}$'
        if not control_number.match(pattern, control_number):
            raise forms.ValidationError('El número de matrícula debe tener el formato correcto de la UTEZ (xxxxxtnxxx)')
        return control_number
    
    def clean_tel(self):
        tel = self.cleaned_data.get('tel')
        if not tel.isdigit() or len(tel) != 10:
            raise forms.ValidationError('El teléfono debe contener exactamente 10 dígitos numéricos')
        return tel
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        if not password1.match(pattern, password1):
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres, incluir una mayúscula, un número y un carácter especial.')
        return password1
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        
        return cleaned_data

class CustomUserLoginForm(AuthenticationForm):
    pass