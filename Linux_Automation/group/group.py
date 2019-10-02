#!/usr/bin/python36
#importing python modules
import subprocess as sp
import cgi

print("content-type: text/html")

#variables
form=cgi.FieldStorage()
grpname=form.getvalue("Group_Name")
grpname=str(grpname)

#opening file in write mode to write variables
fp=open("/var/www/cgi-bin/server/group/groupvar.yml",mode='w')

#writing varibles in file
fp.write('grpname: "{}"\n'.format(grpname))

#closing file
fp.close()



################## reading number from the file stored for the given ip ############
fp=open("/var/www/cgi-bin/server/gen_var.yml")
number=int(fp.read())
fp.close()

########### changing host name of main ansible playbook to run #########
fp=open("ref_group.yml","r")
ch=fp.read()
fp.close()
String ="- hosts: root" +str(number)+"\n"
fp1=open("group.yml","w")
fp1.write(String)
fp1.write(ch)
fp1.close()



#running ansible playbook
x=sp.getoutput("sudo ansible-playbook group.yml")
print("location: http://192.168.43.228/server_menu.html\n")
