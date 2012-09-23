from django.db import models
from django.contrib.auth.models import User


class Map(models.Model):
	name		= models.CharField(max_length=100)
	user		= models.ForeignKey(User)
	public		= models.BooleanField(default=False)


class EntityClass(models.Model):
	"""Individual, Group, Organization, State"""
	name		= models.CharField(max_length=100)


class Need(models.Model):
	"""Six Ways to Die, plus other stuff."""
	name		= models.CharField(max_length=100)
	entityclass	= models.ForeignKey(EntityClass)


class Tier(models.Model):
	"""Individual, Household, Region, Country, World, etc."""
	name		= models.CharField(max_length=100)


class ServiceProvider(models.Model):
	"""Electricity company, supermarket, etc."""
	map		= models.ForeignKey(Map)
	name		= models.CharField(max_length=100)
	tier		= models.ForeignKey(Tier)


class Resource(models.Model):
	"""Food, electricity, etc."""
	map		= models.ForeignKey(Map)
	name		= models.CharField(max_length=100)
	needs		= models.ManyToManyField(Need)
	serviceprovider = models.ManyToManyField(ServiceProvider)
	dependency	= models.ManyToManyField('Resource')
	
	def todict(self):
		return {"name": self.name}
