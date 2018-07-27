from django.contrib import admin
from .models import Trabalhador, Empregador


# Register your models here.
admin.site.register(Empregador)
admin.site.register(Trabalhador)