# Overview
A terminal based chat made using sockets and threads. It saves a history of the chat using SQLite in a .db file. 

# Set-Up
1. Clone the repository
```bash
git clone https://github.com/SushiMan-o3/Sockets.git
cd socket-chat
```

2. Start the server
```bash
cd Server
python server.py
```

After setting up the server, it returns an IPv4 address in the terminal which can be used by the client to join that server and start texting. Every message and announcement is stored in a db file along with the username, the message itself, the time stamp and the IPv4 address.

# Usage
## Terminal Based 
Clients will open up client.py from a device, and run the file. They will be prompted to enter an IPv4 address which the server prints out and enter a username. 

## Web based
