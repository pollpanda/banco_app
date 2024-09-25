from django import forms
from .models import UsuarioBanco

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = UsuarioBanco
        fields = ['nombre', 'tipo_documento', 'numero_documento', 'email', 'telefono', 'fecha_nacimiento', 'saldo']
        widgets = {
            'saldo': forms.TextInput(attrs={'readonly': 'readonly'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_numero_documento(self):
        numero_documento = self.cleaned_data.get('numero_documento')
        if not numero_documento.isdigit():
            raise forms.ValidationError('El número de documento debe contener solo números.')
        return numero_documento

class SaldoForm(forms.Form):
    monto = forms.DecimalField(max_digits=10, decimal_places=2, label="Monto a Añadir")

    def clean_monto(self):
        monto = self.cleaned_data.get('monto')
        if monto <= 0:
            raise forms.ValidationError("El monto debe ser mayor a cero.")
        return monto
