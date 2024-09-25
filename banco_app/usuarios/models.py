from django.db import models

class UsuarioBanco(models.Model):
    # Definir las opciones para el tipo de documento
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('PA', 'Pasaporte'),
    ]

    nombre = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=2, choices=TIPO_DOCUMENTO_CHOICES)  # Cambiamos a ChoiceField
    numero_documento = models.CharField(max_length=15, unique=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)


    def __str__(self):
        return f"{self.nombre} ({self.numero_documento})"
    
class Transaccion(models.Model):
    usuario = models.ForeignKey(UsuarioBanco, on_delete=models.CASCADE, related_name='transacciones')
    tipo_transaccion = models.CharField(max_length=10, choices=[('Ingreso', 'Ingreso'), ('Retiro', 'Retiro')])
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_transaccion} de {self.monto} para {self.usuario.nombre}"


