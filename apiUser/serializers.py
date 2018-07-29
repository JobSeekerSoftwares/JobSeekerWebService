from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Trabalhador, Empregador


class TrabalhadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trabalhador
        fields = ('nome', 'nascimento', 'cpf', 'email', 'nacionalidade', 'estadoCivil', 'endereco', 'cidade',
                  'unidadeFederal', 'telefone', 'celular', 'infoPessoal', 'idGmail', 'objetivo', 'perfil',
                  'experiencia', 'formacao', 'cursoComplementar', 'idiomas', 'infoProfissional')


class EmpregadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empregador
        fields = ('nome', 'email', 'idGmail', 'requisitos', 'formacao',
                  'experiencia', 'salario', 'local', 'disponibilidade')

