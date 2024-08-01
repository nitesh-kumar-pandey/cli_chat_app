# socket lib establish a connection between system 
# socket lib is used to create a socket object
# socket object is used to create a connection between two systems
# socket object is used to send and receive data between two systems

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM )         #Dgram = UDP protocol
# ip_address = "192.168.226.227"
ip_address = "127.0.0.1"   #for single person
port_no = 2525   

complete_address = (ip_address, port_no)
s.bind(complete_address) #bind the socket object to the ip address and port
print("Hey i am receiving your messages ")

#cryptography
while True:
    message = s.recvfrom(100)
    #print(message)
    sender_address = message[1][0]
    sender_port = message[1][1]
    received_message = message[0]
    decrypted_message = received_message.decode('ascii')
    print(decrypted_message)

    with open(sender_address +'.txt', 'a+') as file:
        file.write(decrypted_message + '\n')


    response = input("Enter response: ")
    encrypt_response = response.encode('ascii')
    s.sendto(encrypt_response, (sender_address, sender_port))

