from django.db import models

class ErrorLog(models.Model):
    #es igual a poner Varchar(10)
    codigo = models.CharField(max_length=10)
    #es igual a poner longText
    mensaje = models.TextField()
    #es igual a poner datetime pero con auto_now_add=True se pone la fecha automaticamente
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{codigo} - {mensaje}"