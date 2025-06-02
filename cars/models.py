from django.db import models

class CarBodyType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
class CarBrand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
class Dealer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name
    

class Car(models.Model):
    model_name = models.CharField(max_length=100)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    body_type = models.ForeignKey(CarBodyType, on_delete=models.CASCADE)
    dealer = models.ForeignKey(Dealer, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=5)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.brand.name} {self.model_name} {self.year}"