# Generated by Django 2.0.5 on 2018-07-03 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiUser', '0002_auto_20180702_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabalhador',
            name='celular',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='cidade',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='cpf',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='cursoComplementar',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='email',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='endereco',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='estadoCivil',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='experiencia',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='formacao',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='idGmail',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='idiomas',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='infoPessoal',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='infoProfissional',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='nacionalidade',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='nascimento',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='nome',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='objetivo',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='perfil',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='telefone',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
        migrations.AlterField(
            model_name='trabalhador',
            name='unidadeFederal',
            field=models.TextField(blank=True, default='Não Informado!', null=True),
        ),
    ]
