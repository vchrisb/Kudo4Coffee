from django.db import models
from django.utils import timezone

# Create your models here.
class Beverage(models.Model):
    """( description)"""
    created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    fill_quantity_min = models.IntegerField()
    fill_quantity_max = models.IntegerField()
    fill_quantity_steps = models.IntegerField()
    def __str__(self):
        return str(self.name)


class BeverageHistory(models.Model):
    bean_amount_choices = (
        ('VeryMild', 'Very mild'),
        ('Mild', 'Mild'),
        ('MildPlus', 'Mild +'),
    )
    temperature_choices = (
        ('88C', '88 °C'),
        ('90C', '90 °C'),
        ('92C', '92 °C'),
    )
    created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    bean_amount = models.CharField(max_length=100, choices=bean_amount_choices, default='Mild')
    temperature = models.CharField(max_length=100, choices=temperature_choices, default='90C')
    beverage = models.ForeignKey(Beverage, on_delete=models.CASCADE)