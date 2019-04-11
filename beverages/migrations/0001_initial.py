# Generated by Django 2.2 on 2019-04-11 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('fill_quantity_min', models.IntegerField()),
                ('fill_quantity_max', models.IntegerField()),
                ('fill_quantity_steps', models.IntegerField()),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BeverageHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('bean_amount', models.CharField(choices=[('VeryMild', 'Very mild'), ('Mild', 'Mild'), ('MildPlus', 'Mild +')], default='Mild', max_length=100)),
                ('temperature', models.CharField(choices=[('88C', '88 °C'), ('90C', '90 °C'), ('92C', '92 °C')], default='90C', max_length=100)),
                ('beverage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beverages.Beverage')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]