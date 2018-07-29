from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from .customNLTK import *
from .pln import *


class TrabalhadorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_by_idGmail(self, idGmail):
        return Trabalhador.objects.all().filter(idGmail=idGmail)


@python_2_unicode_compatible
class Trabalhador(models.Model):
    nome = models.TextField(blank=True,null=True,default = 'Não Informado!')
    nascimento = models.TextField(blank=True,null=True,default = 'Não Informado!')
    cpf = models.TextField(blank=True,null=True,default = 'Não Informado!')
    email = models.TextField(blank=True,null=True,default = 'Não Informado!')
    nacionalidade = models.TextField(blank=True,null=True,default = 'Não Informado!')
    estadoCivil = models.TextField(blank=True,null=True,default = 'Não Informado!')
    endereco = models.TextField(blank=True,null=True,default = 'Não Informado!')
    cidade = models.TextField(blank=True,null=True,default = 'Não Informado!')
    unidadeFederal = models.TextField(blank=True,null=True,default = 'Não Informado!')
    telefone = models.TextField(blank=True,null=True,default = 'Não Informado!')
    celular = models.TextField(blank=True,null=True,default = 'Não Informado!')
    infoPessoal = models.TextField(blank=True,null=True,default = 'Não Informado!')
    idGmail = models.TextField(blank=True,null=True,default = 'Não Informado!')

    objetivo = models.TextField(blank=True,null=True,default = 'Não Informado!')
    perfil = models.TextField(blank=True,null=True,default = 'Não Informado!')
    experiencia = models.TextField(blank=True,null=True,default = 'Não Informado!')
    formacao = models.TextField(blank=True,null=True,default = 'Não Informado!')
    cursoComplementar = models.TextField(blank=True,null=True,default = 'Não Informado!')
    idiomas = models.TextField(blank=True,null=True,default = 'Não Informado!')
    infoProfissional = models.TextField(blank=True,null=True,default = 'Não Informado!')

    objects = models.Manager()
    busca = TrabalhadorManager()

    def __str__(self):
        return "{0}".format(self.nome,)


class MoveManager(models.Manager):
    def get_queryset(self, curriculo):
        lista = []
        lista.append(None)
        lista.append(None)
        lista.append(None)
        valor = 0
        maior1 = 0
        maior2 = 0
        maior3 = 0
        i=0

        #text1 = list_to_text(re_text(curriculo))
        text1 = curriculo
        #print(text1)
        emprego = Empregador.objects.all()
        for x in emprego:
            req = x.requisitos + " " + x.experiencia + " " + x.formacao
            #text2 = list_to_text(re_text(req))
            text2 = req
            #if semelhanca(text1, text2) > 0.6:
            #    lista.append(x)
            valor = semelhanca(text1, text2)

            if valor>maior1:
                lista[2] = lista[1]
                lista[1] = lista[0]
                lista[0] = x
                maior1 = valor

            elif valor>maior2 and valor<=maior1:
                lista[2] = lista[1]
                lista[1] = x
                maior2 = valor

            elif valor>maior3 and valor<=maior2:
                lista[2] = x
                maior3 = valor
            else:
                i=i

        return lista


@python_2_unicode_compatible
class Empregador(models.Model):
    nome = models.TextField(blank=True,null=True,default = 'Não Informado!')
    email = models.TextField(blank=True,null=True,default = 'Não Informado!')
    idGmail = models.TextField(blank=True,null=True,default = 'Não Informado!')
    requisitos = models.TextField(blank=True,null=True,default = 'Não Informado!')
    formacao = models.TextField(blank=True,null=True,default = 'Não Informado!')
    experiencia = models.TextField(blank=True,null=True,default = 'Não Informado!')
    salario = models.TextField(blank=True,null=True,default = 'Não Informado!')
    local = models.TextField(blank=True,null=True,default = 'Não Informado!')
    disponibilidade = models.TextField(blank=True,null=True,default = 'Não Informado!')
    objects = models.Manager()
    busca = MoveManager()

    def __str__(self):
        return "{0}:{1}".format(self.nome, self.email,)


# from django.contrib.auth.models import User
# user = User.objects.create_user('john', 'lennon@thebeatles.com', 'password')
