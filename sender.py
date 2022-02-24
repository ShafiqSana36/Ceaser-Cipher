import socket
import encrypt

def create_socket():
    try:    #exception handling as sometimes socket creation can throw errors
        global host
        global port
        global sock

        host = "127.0.0.1"
        port = 5555
        sock = socket.socket()

    except socket.error as msg:
        print ("Socket creation error: " + str(msg))

def bind_socket():
    try:
        global host
        global port
        global sock

        sock.bind((host,port))
        sock.listen(5)  #listen for connections from client

    except socket.error as msg:
        print ("Socket binding error " + str(msg) + "\n Retrying...")
        bind_socket()   #recursive call in case of failure


# Inputting text to encrypt and send to client
def take_input(conn):
    while True:
        try:
            txt = input("Enter text to send: ").upper()

            if len(str.encode(txt)) > 0:    #checking if its not an empty string
                new_text = encrypt.encrypt(txt)
                print("Encrypted text is: " + new_text)
                conn.send(str.encode(new_text))

        except:
            print("Error sending text to receiver.")
            break

def accept_conn():
    while True:
        try:
            conn, addr = sock.accept()
            sock.setblocking(1)     #prevents timeout and disconnectivity
            print ("Established connection to receiver!")
            take_input(conn)

            conn.close()

        except:
            print("Error accepting connections!")


def main():
    print("CEASER CIPHER")
    create_socket()
    bind_socket()
    accept_conn()
    return 0


# formula: chr(((ord('Z')-65+3)%26)+65)


main()