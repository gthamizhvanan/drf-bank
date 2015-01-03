from django.db import models
import datetime

class customers(models.Model):
	customerid = models.AutoField(primary_key=True)
	name       = models.CharField(max_length=100)
	email      = models.CharField(max_length=100)
	mobile     = models.CharField(max_length=15)
	createdon  = models.DateTimeField(default=datetime.datetime.now)
	def __str__(self):
		return str(self.customerid)

class account(models.Model):
	accountid         = models.AutoField(primary_key=True)
	customerid        = models.ForeignKey(customers, related_name='accounts')
	credit            = models.CharField(max_length=100,default=0)
	debit             = models.CharField(max_length=100,default=0)
	total             = models.CharField(max_length=100,default=0)
	# crediton          = models.DateTimeField(default=datetime.datetime.now)
	# debiton           = models.DateTimeField(default=datetime.datetime.now)
	lasttransactionon = models.DateTimeField(default=datetime.datetime.now)
	createdon         = models.DateTimeField(default=datetime.datetime.now)
	def __str__(self):
		return str(self.accountid)
	# class Meta:
	# 	unique_together = ('accountid','credit','debit','total','lasttransactionon')
	# 	ordering = ('lasttransactionon',)
	# 	#order_by      = 'lasttransactionon'
	# def __str__(self):
	# 	return '%d: %s: %s: %s: %s:' % (self.accountid, self.credit,self.debit,self.total,self.lasttransactionon)

# Create your models here.
