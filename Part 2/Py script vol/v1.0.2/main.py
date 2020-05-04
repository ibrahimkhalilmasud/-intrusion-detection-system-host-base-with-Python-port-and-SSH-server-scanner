import glob
import socket
from os.path import basename, dirname, isfile, join
import time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

hostname = socket.gethostname() 
IPAddr = socket.gethostbyname(hostname) 
print()
print ("Author   : Muhammad Ibrahim Khalil")
print ("LinkdIn : https://www.linkedin.com/in/muhammad-ibrahim-khalil-03686978/")
print ("github   : https://github.com/ibrahimkhalilmasud")
print ("Facebook : https://www.facebook.com/Ibrahimkhalilmasudik")
print()
print("Your Computer Name is:" + hostname) 
print("Your Computer IP Address is:" + IPAddr) 


print("Welcome, this is a IDS Ports and SSH server scanner tool")
print("-----------------------------------------------------")

ip_addr = input("Please enter the Host that you want to scan: ")
remoteServerIP  = socket.gethostbyname(ip_addr)
print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)

# Print a nice banner with information on which host we are about to scan
print ("-" * 60)
print ("Please wait, scanning remote host", remoteServerIP) # justify your ip address
print ("-" * 60)
print("The IP you entered is: ", ip_addr)
type(ip_addr)

respons = input("""\nPlease select one to start
                1) Port scanner
                2) SSH server Scan
                3) Only scan open ports\n""")
print("You have selected option: ", respons)

if respons=="1":
    import Port2
    Port2.main()

elif respons=="2":
    import ssh_scanner_1
    ssh_scanner_1.main()

elif respons=="3":
    import port3
    port3.main()

else:
    print("Sorry invalid input")
    exit()
