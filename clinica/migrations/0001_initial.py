# Generated by Django 2.2.6 on 2019-10-31 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=70)),
                ('cnpj', models.CharField(max_length=14)),
                ('ramo', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=8)),
                ('rua', models.CharField(max_length=100)),
                ('numero', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='NomeExame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_exame', models.CharField(max_length=50)),
                ('valor_exame', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='TipoExame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_tipo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('cpf', models.CharField(max_length=11)),
                ('aniversario', models.DateField()),
                ('cep', models.CharField(max_length=8)),
                ('rua', models.CharField(max_length=100)),
                ('numero', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=60)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.Cliente')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.Genero')),
            ],
        ),
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_exame', models.DateTimeField()),
                ('data_exame_devolucao', models.DateTimeField(blank=True, null=True)),
                ('exames_padrao', models.TextField(blank=True, help_text='Notas sobre o paciente', null=True)),
                ('lista_exames', models.TextField(blank=True, help_text='Exames ecolhidos par ao paciente', null=True)),
                ('obs_exame', models.TextField(blank=True, help_text='Notas sobre o paciente', null=True)),
                ('nome_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.Paciente')),
                ('tipo_exame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.TipoExame')),
            ],
        ),
    ]
