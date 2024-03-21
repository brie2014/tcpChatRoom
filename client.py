import socket
import threading

# Get inputs now, so we don't have to try to do it while the socket is running
nickname = input('Choose a nickname: ')
if nickname == 'admin':
    password = input('Enter admin password: ')

# same variables as the server
host = '127.0.0.1'  # localhost
port = 55555

# Create socket and connect it to the same address and port as the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))  # same arguments as the server

# Variable to let our threads know when to stop running
stop_thread = False


# Function to receive incoming messages from the server
def receive():
    while True:
        global stop_thread
        if stop_thread:
            break
        try:
            # Always decode and encode messages
            message = client.recv(1024).decode('ascii')
            # The server will initially send a message to ask for a nickname
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
                next_message = client.recv(1024).decode('ascii')
                # If the nickname we send is "admin", the server will ask for a password next
                if next_message == 'PASSWORD':
                    client.send(password.encode('ascii'))
                    if client.recv(1024).decode('ascii') == 'REFUSE':
                        print("Connection was refused! Wrong password!")
                        stop_thread = True
                        client.close()
                # If the nickname is on the bans list, the connection will be refused
                elif next_message == 'BAN':
                    print('Connection refused because of ban!')
                    stop_thread = True
                    client.close()
            # Otherwise, this is a normal message and we want to print it as is
            else:
                print(message)
        except:
            print('An error occurred!')
            client.close()
            break


# Function to write outgoing messages to the server
def write():
    while True:
        global stop_thread
        if stop_thread:
            break
        while True:
            # Get the message from the user
            user_input = f'{input("")}'
            # If an admin types /kick or /ban we send a special message to the server
            if nickname == 'admin' and user_input.startswith('/kick'):
                client.send(f'KICK {user_input[6:]}'.encode('ascii'))
            elif nickname == 'admin' and user_input.startswith('/ban'):
                print('I am banning')
                client.send(f'BAN {user_input[5:]}'.encode('ascii'))
            # If a non-admin tries to send a command, print a message
            elif nickname != 'admin' and user_input.startswith('/'):
                print("Commands can only be executed by the admin")
            # Otherwise, send the message normally
            else:
                message = f'{nickname}: {user_input}'
                client.send(message.encode('ascii'))


# Start a receiving thread for each client
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Start a writing thread for each client
write_thread = threading.Thread(target=write)
write_thread.start()
