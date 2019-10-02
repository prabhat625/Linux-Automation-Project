#!/usr/bin/python36
#importing python modules
import random
import subprocess as sp
import cgi

print("content-type: text/html")
form=cgi.FieldStorage()


#variables
username=form.getvalue("User_Name")
username=str(username)

#opening file in write mode to write variables
fp=open("/var/www/cgi-bin/server/user/uservar.yml",mode='w')

#writing varibles in file
fp.write('username: "{}"\n'.format(username))

#closing file
fp.close()
################## reading number from the file stored for the given ip ############
fp=open("/var/www/cgi-bin/server/gen_var.yml")
number=int(fp.read())
fp.close()

########### changing host name of main ansible playbook to run #########
fp=open("ref_user.yml","r")
ch=fp.read()
fp.close()
String ="- hosts: root" +str(number)+"\n"
fp1=open("user.yml","w")
fp1.write(String)
fp1.write(ch)
fp1.close()



#running ansible playbook
x=sp.getoutput("sudo ansible-playbook user.yml")

print("location: http://192.168.43.228/server_menu.html\n")
