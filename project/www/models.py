from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Shoe(models.Model):
    model = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)  # Dodano relację ForeignKey do Brand

    def __str__(self):
        return f"{self.brand.name} - {self.model}"
