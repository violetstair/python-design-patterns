# 싱글톤 패턴 사례 2


class HealthCheck:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance
    
    def __init__(self):
        self._servers = []
    
    def add_server(self, server):
        self._servers.append(server)
    
    def change_server(self, index, server):
        self._servers.pop(index)
        self._servers.append(server)
    

hc1 = HealthCheck()
hc2 = HealthCheck()

hc1.add_server("server 1")
hc1.add_server("server 2")
hc1.add_server("server 3")
hc1.add_server("server 4")

print("Schedule health check for servers (1)... ")
for i in range(4):
    print("checking : ", hc1._servers[i])

print("Schedule health check for servers (2)... ")
hc2.change_server(3, "server 5")
for i in range(4):
    print("checking : ", hc2._servers[i])
