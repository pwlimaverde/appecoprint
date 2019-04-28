# Generated by Django 2.2 on 2019-04-28 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulopcp', '0003_upload_list_op'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orcamento', models.IntegerField(max_length=5)),
                ('cliente', models.CharField(max_length=300)),
                ('servico', models.TextField()),
                ('quant', models.DecimalField(decimal_places=0, max_digits=7)),
                ('valor', models.DecimalField(decimal_places=4, max_digits=7)),
                ('entrada', models.DateField()),
                ('vendedor', models.CharField(max_length=100)),
                ('op', models.IntegerField(max_length=5)),
                ('prev_entrega', models.DateField()),
                ('faturamento', models.CharField(blank=True, max_length=100, null=True)),
                ('entrega', models.DateField(blank=True, null=True)),
                ('cancelada', models.BooleanField(blank=True, null=True)),
                ('obs', models.TextField(blank=True, null=True)),
            ],
        ),
    ]