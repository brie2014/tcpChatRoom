# Overview

If you are looking to dabble in the basics of networking, you've found the right repo! 
Networking is a powerful tool--it's how you're viewing this page on the world wide web right now. 
By creating a system of connected computers, we are able to accomplish a lot of great things.

In this repo, I've built  a basic client-server TCP chatroom application, that can be ran in the command prompt. 
It uses sockets and threading to allow multiple clients to connect to the same local server, and send messages back and forth.
To add additional functionality, we now support a password protected admin user that can kick and ban users from the chatroom.

**Getting Started**
1. Clone the repository and make sure python is setup on your computer
2. Open the command terminal and navigate to the directory with this repo
3. Run `python server.py` to start the chatroom server
4. Open the command terminal and navigate to the directory with this repo
5. Run `python client.py` to start a client and join the chatroom
6. Repeat steps 4-5 as many times as you would like to add additional clients to the chatroom
7. Chat away!

Note: To join as an admin, when you start the client, enter `admin` as the nickname, then enter `adminpass` as the password

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

Architecture: Client-Server

Protocol: TCP

Port: 55555

Message format: ASCII encoded text

# Development Environment

Tools: PyCharm, Command Prompt

Language: Python

Libraries: socket, threading

# Useful Websites

**Python**
* [Python Documentation](https://www.w3schools.com/python/default.asp)
* [Python startswith (be careful with casing!)](https://www.w3schools.com/python/ref_string_startswith.asp)

**Networking**
* [Client-Server Model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
* [What's the Difference Between TCP and UDP](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)
* [Computer Networks](https://www.youtube.com/watch?v=3QhU9jd03a0)
* [The World Wide Web](https://www.youtube.com/watch?v=guvsH5OFizE&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo&index=32)
* [The Internet](https://www.youtube.com/watch?v=AEaKrq3SpW8&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo&index=31)

**Setup**
* [PyCharm Download](https://www.jetbrains.com/pycharm/download/?section=windows)

**Videos**
* [Python Sockets Simply Explained](https://www.youtube.com/watch?v=YwWfKitB8aA)
* [Simple TCP Chat Room in Python](https://www.youtube.com/watch?v=3UOyky9sEQY)
* [Advanced TCP Chat Room in Python](https://www.youtube.com/watch?v=F_JDA96AdEI)
* [Python for Networking Playlist](https://www.youtube.com/playlist?list=PL7yh-TELLS1FwBSNR_tH7qVbNpYHL4IQs)

# Future Work

* Ban users by IP address
* Don't double print sent messages
* Add user commands for special features (ex. print participant list)