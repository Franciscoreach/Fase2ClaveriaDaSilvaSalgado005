from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Entrada(models.Model):
	
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID única para el caso de un Alumno.')
	titulo = models.CharField(max_length=100)
	tema = models.TextField(max_length=5000)

	class Meta:
		ordering = ['titulo']

	def get_absolute_url(self):
		return reverse('entrada-detail', args=[str(self.id)])

	def __str__(self):
		return f'Entrada: {self.titulo}'