def list_ifname_ip():
	fin = open("running-config.cfg",'r')
	a = i.split(",")
	for b in  a:
		d = dict(b)
		for key, value in b:
			print(key, value)


