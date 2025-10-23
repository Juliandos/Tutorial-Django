from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)

class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    year = models.IntegerField()
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None)


    def __str__(self):
        return self.name