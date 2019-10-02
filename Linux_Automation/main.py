#!/usr/bin/python36


import subprocess as sp
import cgi
import random
print("content-type: text/html")

form=cgi.FieldStorage()

############### storing variable #############
username="root"
passwd=str(form.getvalue("Password"))
ip=str(form.getvalue("Ip"))



###############  generat random number to avoid the user name conflict in ansible hosts file ############
number=random.randrange(1,1000,1);



########  writing variables in file  ###############
fp=open("/var/www/cgi-bin/server/var.yml","w")

fp.write('passwd: "{}"\n'.format(passwd))
fp.write('username: "{}"\n'.format(username))
fp.write('number: "{}"\n'.format(number))
fp.write('ip: "{}"\n'.format(ip))
fp.close()
############### cleaning  ansible host ############

fp=open("/etc/ansible/hosts","w")
ch=fp.write("localhost")
fp.close();

################# writer number to a file for use it everywhere###########
fp=open("/var/www/cgi-bin/server/gen_var.yml","w")
fp.write('{}'.format(number))
fp.close() 
############## putting entry of user in hosts file #############
x=sp.getoutput("sudo ansible-playbook form.yml")
##############  Checking For User Password is Correct  ######################
y=str(username)+str(number);
x="sudo ansible "+y+  " -a date";
z=sp.getoutput(x)
l=z.split()
#print(z)
#print(l)
###########------------------------------------------############

if "false,"  in l:

	print("\n ENTERED WRONG INFORMATION")
else:
	################# redirecting to mainmenu ####################
	print("location: http://192.168.43.228/server_menu.html\n")
