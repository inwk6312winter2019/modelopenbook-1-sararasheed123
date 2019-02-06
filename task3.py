def myfunc():
	fin = open("running-config.cfg",'r')
	line = fin.readline()
	while line:

		list_1=[]
		list_2=[]
		list_3=[]
	if "access-list" in line:
		if "transit_access_in" in line:
			list_1.append(line)
		elif "fw-management_access_in" in line:
			list_2.append(line)
		else:
			"global_access"in line
			list_3.append(line)
	print(list_1)
myfunc()
