from rest_framework import viewsets
from bank.serializers import customerSerializer,accountSerializer,accountCreditSerializer,accountDebitSerializer
from bank.models import customers,account
from rest_framework.decorators import detail_route, list_route

class customerViewSet(viewsets.ModelViewSet):
		queryset         = customers.objects.all()
		serializer_class = customerSerializer

class accountViewSet(viewsets.ModelViewSet):
		fields = ('accountid','credit','debit','customerid')
		queryset         = account.objects.all()
		serializer_class = accountSerializer

class accountViewCredit(viewsets.ModelViewSet):
		fields = ('accountid','credit','customerid','total')
		queryset         = account.objects.all()
		#queryset         = account.objects.values('accountid', 'credit','customerid','total')
		serializer_class = accountCreditSerializer

class accountViewDebit(viewsets.ModelViewSet):
		fields = ('accountid','debit','customerid')
		queryset         = account.objects.all()
		serializer_class = accountDebitSerializer




# Create your views here.
