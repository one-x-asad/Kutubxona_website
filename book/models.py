from django.db import models

class Category(models.Model):
    category=models.CharField(max_length=255,null=False)

    def __str__(self):
        return self.category

class Book(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(null=False)
    name=models.CharField(max_length=255,null=False)
    author=models.CharField(max_length=100)
    description=models.TextField()
    date=models.TimeField(null=False)
    price=models.FloatField(null=False)


    def __str__(self):
        return self.name