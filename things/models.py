from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.Charfield(max_length=30, unique=True, blank=False)
    description = models.Charfield(max_length=120, blank=True)
    quantity = models.IntegerField(
      default=0,
      validators=[
        MaxValueValidator(100, message = "The maximum quantity is 100. "),
        MinValueValidator(0, message = "The minimum quantity is 0. "),
      ]
    )
