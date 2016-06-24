import math
from copy import copy

class Common():
    def __init__(self,params={}):
        self.server_types      =    {'large':1,'xlarge':2,'2xlarge':4,'4xlarge':8,'8xlarge':16,'10xlarge':32}
        self.server_types_flip =    {v:k for k,v in self.server_types.items()}

    def get_costs(self, instances={}, hours=0, cpus=0, price='', self_call=''):
        result = []
        for single_instance in instances:
            region = single_instance
            if hours!=0 and cpus!=0 and price!='':
                single_instance_list = self.getServerCpuList(instances[single_instance])
                cpu_result = self.getAllocate(cpus,single_instance_list,'cpu')
                allocate_cpu_dict = {self.server_types_flip[k]:v for k,v in cpu_result.items()}
                total_cost = "{0:.2f}".format(self.getPriceByCpu(cpu_result,hours,instances[single_instance]))
                tuple_value_servers = [(v,k) for k,v in allocate_cpu_dict.items()]
                result.append({'region':region, "total_cost": "$"+total_cost, "servers": tuple_value_servers})

            elif hours!=0 and cpus!=0 and price=='':
                single_instance_list = self.getServerCpuList(instances[single_instance])
                cpu_result = self.getAllocate(cpus,single_instance_list,'cpu')
                allocate_cpu_dict = {self.server_types_flip[k]:v for k,v in cpu_result.items()}
                total_cost = "{0:.2f}".format(self.getPriceByCpu(cpu_result,hours,instances[single_instance]))
                tuple_value_servers = [(v,k) for k,v in allocate_cpu_dict.items()]
                result.append({'region':region, "total_cost": "$"+total_cost, "servers": tuple_value_servers})

            elif hours!=0 and cpus==0 and price!='':
                avail_server_values_list = list(instances[single_instance].values())
                avail_server_values_list.sort()
                avail_server_values_list = avail_server_values_list[::-1]
                price_result = self.getAllocate(price/hours,avail_server_values_list,'price')
                price_result_round = {k:v for k,v in price_result.items()}
                price_final_result = {k:round(price_result_round[v]*hours) for k,v in self.getCpu(price_result,instances[single_instance]).items()}
                tuple_value_servers = [(v,k) for k,v in price_final_result.items()]
                total_cost = sum([k*v for k,v in price_result_round.items()])*hours
                result.append({'region':region, "total_cost": "$"+str(total_cost), "servers": tuple_value_servers})
        return result

    def getAllocate(self, min_cpu,avail_cpu,call_for=''):
        cpu_split = {}
        cpu_split_list = []
        min_cpu_x = min_cpu
        for x in avail_cpu:
            if min_cpu_x >= x:
                y = math.floor(min_cpu_x/x)
                if call_for == 'cpu':
                    min_cpu_x = int(min_cpu_x-(x*y))
                    cpu_split[x] = int(y)
                    cpu_split_list.append(int(x*y))
                elif call_for == 'price':
                    min_cpu_x = float(min_cpu_x-(x*y))
                    cpu_split[x] = float(y)
                    cpu_split_list.append(float(x*y))
        else:
            if min_cpu_x:
                min_avail_cpu = min(avail_cpu)
                cpu_split[min_avail_cpu] = min_cpu_x if min_avail_cpu not in cpu_split else cpu_split[min_avail_cpu]+min_cpu_x
                cpu_split_list.append(min_cpu_x)

        if sum(cpu_split_list) > 0:
            remain_value = min_cpu - sum(cpu_split_list)
            if (remain_value > 0):
                self.getAllocate(remain_value,avail_cpu,call_for='')

        for k,v in cpu_split.items():
            if k*v in avail_cpu and v>1:
                cpu_split[k*v] = 1
                del cpu_split[k]

        return cpu_split

    def getServerCpuList(self, avail_server):
        avail_server_cpu_keys = list(set(self.server_types.keys())-set(avail_server.keys()))
        server_type_del = copy(self.server_types)
        del server_type_del[avail_server_cpu_keys[0]]
        result = list(server_type_del.values())
        result.sort()
        return result[::-1]

    def getPriceByCpu(self, cpu_result,hours,avail_server):
        hrs_result = []
        for cpu_res in cpu_result:
            hrs_result.append(avail_server[self.server_types_flip[cpu_res]]*cpu_result[cpu_res]*hours)
        return sum(hrs_result)

    def getCpu(self, price_result, avail_server):
        avail_server_flip = {v:k for k,v in avail_server.items()}
        cpu_result = {}
        for price_res in price_result:
            price_res = price_res
            try:
                cpu_result[price_res] = avail_server_flip[price_res]
            except:
                avail_server_values_list = list(avail_server.values())
                avail_server_values_list.sort()
                avail_server_values_list_cp = copy(avail_server_values_list)
                for x in avail_server_values_list_cp:
                    if price_res < x:
                        cpu_result[x] = avail_server_flip[x]
                        avail_server_values_list_cp.remove(x)

        cpu_result_flip = {v:k for k,v in cpu_result.items()}
        return cpu_result_flip

    def dict_flip(self, req_dict={}):
        if isinstance(req_dict,dict):
            return {v:k for k,v in req_dict.items()}
        return False
