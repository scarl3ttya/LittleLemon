from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    guest_count = models.SmallIntegerField(default=2)
    date = models.DateTimeField()
    
    def __str__(self): 
        return self.name



class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(default=1)

    def __str__(self): 
        return f'#{self.id} - {self.title}  (${str(self.price)})'
    

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self): 
        return f'#{self.id} - {self.title}  (${str(self.price)})'

    def get_item(self):
        return f'#{self.id} - {self.title}  (${str(self.price)})'