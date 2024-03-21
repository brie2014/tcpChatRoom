import threading
import socket

# cd Code/cse310/tcpChatRoom

host = '127.0.0.1'  # localhost
port = 55555

# setup server and socket
# socket.AF_INET means internet socket; SOCK_STREAM means TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


# Send a message to every client
def broadcast(message):
    for client in clients:
        client.send(message)


# function to handle incoming messages
def handle(client):
    while True:
        try:
            # one variable for checking commands, one for broadcasting to avoid loop issues
            msg = message = client.recv(1024)
            # Handle KICK messages (admin only)
            if msg.decode('ascii').startswith('KICK'):
                if nicknames[clients.index(client)] == 'admin':
                    # cut off the first 5 characters KICK+whitespace
                    name_to_kick = msg.decode('ascii')[5: ]
                    kick_user(name_to_kick, False)
                else:
                    client.send('Command was refused'.encode('ascii'))
            # Handle BAN messages (admin only)
            elif msg.decode('ascii').startswith('BAN'):
                if nicknames[clients.index(client)] == 'admin':
                    # cut off the first 4 characters BAN+whitespace
                    name_to_ban = msg.decode('ascii')[4:]
                    kick_user(name_to_ban, True)
                    # add user to ban list
                    with open('bans.txt', 'a') as f:
                        f.write(f'{name_to_ban}\n')
                    print(f'{name_to_ban} was banned!')
                else:
                    client.send('Command was refused'.encode('ascii'))
            # Broadcast all other messages
            else:
                broadcast(message)
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f"{nickname} left the chat".encode('ascii'))
                nicknames.remove(nickname)
                break


# Function to receive connecting clients to the server
def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        client.send('NICK'.encode())
        nickname = client.recv(1024).decode('ascii')

        with open('bans.txt', 'r') as f:
            bans = f.readlines()

        # If the client's nickname is in the bans list, reject the connection
        if nickname+'\n' in bans:
            client.send('BAN'.encode('ascii'))
            client.close()
            continue

        # If the client's nickname is admin, check and verify the password
        if nickname == 'admin':
            client.send('PASSWORD'.encode('ascii'))
            password = client.recv(1024).decode('ascii')

            if password != 'adminpass':
                client.send('REFUSE'.encode('ascii'))
                client.close()
                continue

        # Otherwise, add the client to the list, and their nickname to the nickname list
        nicknames.append(nickname)
        clients.append(client)

        # Print some output to the server and let the other clients know of the newcomer
        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat".encode('ascii'))

        # Send a message to the client confirming the connection
        client.send('Connected to the server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


# Function to kick user from the chatroom
def kick_user(name, is_ban):
    if name in nicknames:
        name_index = nicknames.index(name)
        client_to_kick = clients[name_index]
        clients.remove(client_to_kick)
        action = 'kicked'
        if is_ban:
            action = 'banned'
        client_to_kick.send(f'You were {action} by an admin!'.encode('ascii'))
        client_to_kick.close()
        nicknames.remove(name)
        broadcast(f'{name} was {action} by an admin'.encode('ascii'))


# Start the server
print("Server is listening...")
receive()
