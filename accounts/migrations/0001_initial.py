# Generated by Django 3.0.7 on 2020-06-16 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mask', models.CharField(blank=True, max_length=128, null=True)),
                ('cc', models.CharField(blank=True, max_length=8, null=True)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=128, null=True)),
                ('description_ru', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=128, null=True)),
                ('company', models.CharField(blank=True, max_length=128, null=True)),
                ('position', models.CharField(blank=True, max_length=128, null=True)),
                ('public', models.BooleanField(default=1)),
                ('rank', models.CharField(choices=[('0', 'Not in Committee'), ('1', 'First'), ('2', 'Second'), ('3', 'Third')], default='0', max_length=1)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('degree', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Degree')),
                ('reference', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Reference')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Region')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('company', models.CharField(blank=True, max_length=128, null=True)),
                ('position', models.CharField(blank=True, max_length=128, null=True)),
                ('degree', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Degree')),
            ],
        ),
    ]