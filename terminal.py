#!/usr/bin/python


###################
##               ##
##  SERVER SIDE  ##
##               ##
###################


'''
    # Description :
    Terminal.py - This program is a simple backdoor which control the VICTIM's
    machine,  and send an ECHO back to the client

    # Terms Of Use :
    This project is owned by Hacking|Pentesting Group on facebook
    ( https://www.facebook.com/groups/1740722166239140/ ) for learning
    purposes uses only!
    Therefore, the admis, moderators and authors do not hold any legal
    actions of whom is going to use this program in ilegal way.


'''


import socket
import sys



# Globals:
##########


# Get all connections no exception
HOST = '0.0.0.0'
# Arbitrary non-privileged port
PORT = 50007

# Create a SOCKET object
sock = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
# Bind connections
sock.bind(( HOST , PORT ))
# Listen for connections , 
# if there's more then 1 connection the server will crtash
sock.listen(1)
# Accept connection
conn, addr = sock.accept()
# Print the connectio IP
print( '[+] Connected by ', addr )


# MAIN
while 1:    # 1= True , 0 = False
    # Receive data from client
    data = conn.recv( 1024 )
    # Check if data is empty
    if not data:
        # print msg to server
        print( '[!] NO DATA SENT!' )
        break
    # Send data back to the Client
    conn.sendall( data )
# Close the connection from client
conn.close()
# exiting the program
sys.exit()

        
