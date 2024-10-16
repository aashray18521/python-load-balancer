import socket
# type: ignore


# Socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding socket to a port
sock.bind("localhost", 8080)

# Listen for incoming connections
# "5" specifies the maximim number of queued connections.
sock.listen(5)

while True:
  # Accept an incoming connection
  client_sock, client_address = sock.accept()
  print(f"[INFO]Received connection from {client_address}")

  # Choose a server to forward the connection to
  server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_sock.connect(("localhost", 8000))

  # Forward the connection
  server_sock.sendall(client_sock.recv*(1024))

  # Close connections
  client_sock.close()
  server_sock.close()