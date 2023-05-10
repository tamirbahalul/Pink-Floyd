import socket
import time, sys
LOCALHOST = 'localhost'
PORT = 80


def main():
    try:
        # create a tcp socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print("not can create a socket")
        time.sleep(1)
        sys.exit()
    try:
        # connecting to remote computer 80
        server_address = (LOCALHOST, PORT)
        sock.connect(server_address)
    except socket.error:
        print("not can connect to the server")
        time.sleep(1)
        sys.exit()

    flag = True
    while flag:
        command = input("""please enter your choice:
            1. get all the album of pink floyd = all Album
            2. get list all song of album specific = all Song
            3. get a length of specific song = length song
            4. get a word of specific song = word from song
            5. in which album is a song? = which album
            6. search word in song = search word
            7. exit program = exit\n""")

        if command == "all Album":
            command = "1"

        elif command == "all Song":
            command = "2"
            album = input("please enter album: ")
            command += album

        elif command == "length song":
            command = "3"
            song = input("please enter song for length: ")
            command += song

        elif command == "word from song":
            command = "4"
            song = input("please enter song for words: ")
            command += song

        elif command == "which album":
            command = "5"
            song = input("please enter song for know album is in: ")
            command += song

        elif command == "search word":
            command = "6"
            word = input("please enter your word or sentence you want find in: ")
            command += word

        elif command == "exit":
            command = "7"
            flag = False

        b_command = bytes(command, 'utf-8')

        # sending data to server
        sock.sendall(b_command)

        # receiving data from the server
        server_msg = sock.recv(1024)

        server_msg = server_msg.decode('utf-8')
        print("\n"+server_msg+"\n")

    # closing the socket
    sock.close()


if __name__ == "__main__":
    main()
