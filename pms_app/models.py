from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='company', blank=True)
    information = models.CharField(max_length=250, blank=True)
    website = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=150)
    contact = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=150)
    contact = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
