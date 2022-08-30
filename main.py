#import socket module
import socket

# In order to terminate the program
import sys 

# Boilerplate
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Prepare a sever socket
address = ("", 2048)

try:
    server_socket.bind(address)
    server_socket.listen(1)
except socket.error:
    print("Server bind failed")
    sys.exit(1)


while True:
    
    #Establish the connection
    print('Ready to serve...')
    
    # # More boilerplate
    connectionSocket, addr = server_socket.accept()
    
    try:
        message = #Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = #Fill in start #Fill in end
        
    #     #Send one HTTP header line into socket
    #     #Fill in start
    #     #Fill in end
        
    #     #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
        
    except IOError:
        pass
        #Send response message for file not found
        #Fill in start
        #Fill in end

#Close client socket
#Fill in start
#Fill in end

# Close the socket
server_socket.close()

#Terminate the program after sending the corresponding data
sys.exit()