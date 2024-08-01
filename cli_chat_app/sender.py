# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM )         #Dgram = UDP protocol
# target_ip = "127.0.0.1"   #for single person
# port_no = 2525   

# target_address = (target_ip,port_no)


# condition = True
# while condition:
#     message = input("plz write your message here : ")
#     encrypt_message = message.encode('ascii')
#     s.sendto(encrypt_message,target_address)


import socket

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Dgram = UDP protocol
ip_address = "127.0.0.1"  # for single person
port_no = 2525

target_address = (ip_address, port_no)

while True:
    # Sending message
    message = input("Please write your message here: ")
    encrypt_message = message.encode('ascii')
    s.sendto(encrypt_message, target_address)

    # Receiving response
    response, addr = s.recvfrom(1024)  # buffer size is 1024 bytes
    decrypted_response = response.decode('ascii')
    print(f"Received response: {decrypted_response}")

