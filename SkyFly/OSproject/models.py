from django.db import models

# Create your models here.
class Flight(models.Model):
	departure =  models.CharField(max_length=30)
	landing =  models.CharField(max_length=30)
	price = models.IntegerField()
	date = models.DateField()

class Offer(models.Model):
	client = models.CharField(max_length=30)
	flight = models.CharField(max_length=30)
	discount = models.FloatField()

class Meeting(models.Model):
	date = models.DateField()
	hour = models.IntegerField()
	employees = models.CharField(max_length=50)

class Client(models.Model):
	email = models.CharField(max_length=50)
	phone = models.CharField(max_length=20)

class Company(Client):
	budget = models.IntegerField()
	nationality = models.CharField(max_length=50)
	domainOfActivity = models.CharField(max_length=50)

class Person(Client):
	nationality = models.CharField(max_length=50)
	age = models.IntegerField()

class Employee(models.Model):
	firstName = models.CharField(max_length=50)
	lastName= models.CharField(max_length=50)
	role= models.CharField(max_length=50)
	address= models.CharField(max_length=50)
	phone= models.CharField(max_length=50)
	availability= models.CharField(max_length=50)
	certifications= models.CharField(max_length=50)
	contract= models.CharField(max_length=50)


