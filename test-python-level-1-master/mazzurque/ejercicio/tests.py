from django.test import TestCase, Client
from .models import Fisica , Juridica



class FisicaTest(TestCase):
    """ Test  para Fisica model """

    def setUp(self):
        Fisica.objects.create(
            nombre='Alberto',apellido="Yaque" , dni=99999999,cuit = 20999999991)
        Fisica.objects.create(
            nombre='Diego',apellido="Figueroa" , dni=88888888,cuit = 20888888881)

    def test_fisica_apellido(self):
        fisica_Alberto = Fisica.objects.get(nombre='Alberto')
        fisica_Diego = Fisica.objects.get(nombre='Diego')
        self.assertEqual(
            fisica_Alberto.apellido, "Yaque")
        self.assertEqual(
            fisica_Diego.apellido, "Figueroa")



class JuridicaTest(TestCase):
    """ Test  para Juridica model """

    def setUp(self):
        Juridica.objects.create(
            razon='Hogar Obrero',año=1905 , cuit = 30501875828)
        Juridica.objects.create(
            razon='Asociación Panadería del Pueblo',año=1855 ,cuit = 30408157288)

    def test_juridica_apellido(self):
        juridica_Hogar = Juridica.objects.get(razon='Hogar Obrero')
        juridica_panaderia = Juridica.objects.get(razon='Asociación Panadería del Pueblo')
        self.assertEqual(juridica_Hogar.año, 1905)
        self.assertEqual(juridica_panaderia.año, 1855)

