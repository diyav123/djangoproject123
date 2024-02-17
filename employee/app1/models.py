from django.db import models

class Category(models.Model):
    category_name=models.CharField(max_length=20)
    def __str__(self):
        return self.category_name

class Student(models.Model):
    employee_name=models.CharField(max_length=20)
    category_name=models.ForeignKey(Category,on_delete=models.CASCADE)
    place=models.CharField(max_length=30)
    mobile_number=models.IntegerField()
    def __str__(self):
        return self.employee_name
