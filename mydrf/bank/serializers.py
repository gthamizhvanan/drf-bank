from rest_framework import serializers
from bank.models import customers,account
from rest_framework import permissions


class customerSerializer(serializers.HyperlinkedModelSerializer):
	accounts = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='account-detail')
	class Meta:
		model  = customers
		fields = ('name','email','mobile','accounts')
		read_only_fields = ('createdon')

class accountSerializer(serializers.ModelSerializer):
	customerid = serializers.PrimaryKeyRelatedField(queryset=customers.objects.all())
	class Meta:
		model  = account
		fields = ('accountid','credit','debit','customerid')
		read_only_fields = ('total','lasttransactionon','createdon')

class accountCreditSerializer(serializers.ModelSerializer):
	customerid = serializers.PrimaryKeyRelatedField(queryset=customers.objects.all())
	class Meta:
		model  = account
		fields = ('accountid','credit','customerid','total','lasttransactionon','createdon')
		read_only_fields = ('lasttransactionon','createdon')

class accountDebitSerializer(serializers.ModelSerializer):
	customerid = serializers.PrimaryKeyRelatedField(queryset=customers.objects.all())
	class Meta:
		model  = account
		fields = ('accountid','debit','customerid')
		read_only_fields = ('total','lasttransactionon','createdon')