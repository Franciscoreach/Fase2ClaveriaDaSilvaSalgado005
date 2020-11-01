from django.test import TestCase
from . models import Entrada

class EntradaTestCase(TestCase):

    @classmethod

    def setUpTestData(cls):
        test_entrada = Entrada.objects.create(id= '44fc2b9d-2b04-45cb-af4a-c4601727c158', titulo='Como intentar no sufrir bullying',tema='Hola, esto es una prueba para no sufrir mas abusos en el colegio.')
    
    def test_titulo_label(self):
        entrada=Entrada.objects.get(id= '44fc2b9d-2b04-45cb-af4a-c4601727c158')
        field_label = Entrada._meta.get_field('titulo').verbose_name
        self.assertEquals(field_label,'titulo')

    def test_tema_label(self):
        entrada=Entrada.objects.get(id='44fc2b9d-2b04-45cb-af4a-c4601727c158')
        field_label = Entrada._meta.get_field('tema').verbose_name
        self.assertEquals(field_label,'tema')

    def test_titulo_max_length(self):
        entrada=Entrada.objects.get(id='44fc2b9d-2b04-45cb-af4a-c4601727c158')
        max_length = Entrada._meta.get_field('titulo').max_length
        self.assertEquals(max_length,100)
    
    def test_tema_max_length(self):
        entrada=Entrada.objects.get(id='44fc2b9d-2b04-45cb-af4a-c4601727c158')
        max_length = Entrada._meta.get_field('tema').max_length
        self.assertEquals(max_length,5000)
        
    def test_get_absolute_url(self):
        entrada=Entrada.objects.get(id='44fc2b9d-2b04-45cb-af4a-c4601727c158')
        self.assertEquals(entrada.get_absolute_url(), '/contacto/entrada/44fc2b9d-2b04-45cb-af4a-c4601727c158')