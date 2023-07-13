from django.db import models

# Create your models here.

class Booking(models.Model):
    reservation_name = models.CharField(max_length=200, null=False)
    reservation_date = models.CharField(max_length=15)
    reservation_time = models.SmallIntegerField(default=10)
    guest_count = models.SmallIntegerField(default=2)

    def __str__(self): 
        return self.reservation_name +' '+self.reservation_date+' '+str(self.reservation_slot)

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(default=1)
    description = models.TextField(max_length=1000, default='')

    def __str__(self): 
        return f'#{self.id} - {self.title}  (${str(self.price)})'
    

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()    

    def __str__(self): 
        return f'#{self.id} - {self.title}  (${str(self.price)})'

    def get_item(self):
        return f'{self.title} : {str(self.price)}'