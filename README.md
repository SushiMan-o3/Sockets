# Overview
A terminal based chat made using sockets and threads. It saves a history of the chat using SQLite in a .db file. 

# Set-Up
After setting up the server, it returns an IPv4 address in the terminal which can be used by the client to join that server and start texting. Every message and announcement is stored in a db file along with the username, the message itself, the time stamp and the IPv4 address.

# Usage
Clients will open up client.py from a device, and run the file. They will be prompted to enter an IPv4 address which the server prints out and enter a username. 
