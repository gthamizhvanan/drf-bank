from common import Common
from pprint import pprint

instances      = {'us-east':{'large':0.12,'xlarge':0.23,'2xlarge':0.45,'4xlarge':0.774,'8xlarge':1.4}, 'us-west':{'large':0.14,'2xlarge':0.413,'4xlarge':0.89,'8xlarge':1.3, '10xlarge':2.97}}

print ('\n')
print ('INPUT - HOURS : 24, CPUS : 135')
print ('------------------------------')
x = Common().get_costs(instances=instances, hours=24, cpus=135, price='')
pprint (x)
print ('\n')
print ('INPUT - HOURS : 10, PRICE : 65')
print ('------------------------------')
x = Common().get_costs(instances=instances, hours=10, cpus=0, price=65)
pprint (x)
print ('\n')
print ('INPUT - HOURS : 6, CPUS : 180, PRICE : 65')
print ('-----------------------------------------')
y = Common().get_costs(instances=instances, hours=6, cpus=180, price=65)
pprint (y)

