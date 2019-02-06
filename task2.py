def my_func():
	fin=open("running-config.cfg",'r')
	line=f.readline()
	while line:
		line=line.split()
		ip = 192,172
		if ip in line:
			line=line.replace(192,10)
			line=line.replace(172,10)
		subnet= "255.255.255.0"
		if subnet in line:
			a=line.replace("255.255.255.0","255.0.0.0")
			a=line.replace("255,255.0.0","255.0.0.0")
fout=open("newconfig",'a')
fout.write("line")
fout.write("a")

