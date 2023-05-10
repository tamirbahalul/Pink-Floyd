import socket
import json


def get_all_albums(pinkfloyd_alboms):
    temp_list = pinkfloyd_alboms.keys()
    temp_string = "\n".join(map(str, temp_list))
    return temp_string


def get_all_song_of_album(album, pinkfloyd_alboms):
    if album in pinkfloyd_alboms.keys():
        temp_list = pinkfloyd_alboms[album].keys()
        temp_string = "\n".join(map(str, temp_list))
        return temp_string
    else:
        return "not found"


def get_length_of_song(song, pinkfloyd_alboms):
    for album in pinkfloyd_alboms.keys():
        if song in pinkfloyd_alboms[album]:
            return pinkfloyd_alboms[album][song]["length"]
    return "not found song!"


def get_words_from_song(song, pinkfloyd_alboms):
    for album in pinkfloyd_alboms.keys():
        if song in pinkfloyd_alboms[album]:
            return pinkfloyd_alboms[album][song]["words"]
    return "not found song!"


def get_album_where_song_is(song, pinkfloyd_alboms):
    for album in pinkfloyd_alboms.keys():
        for songs in pinkfloyd_alboms[album]:
            if song in songs:
                return album
    return "not found this song in album"


def search_word(search_word, pinkfloyd_alboms):
    # have more than 1 sentence or word
    list_word = []
    for album in pinkfloyd_alboms.keys():
        for song in pinkfloyd_alboms[album]:
            if search_word in pinkfloyd_alboms[album][song]["words"]:
                list_word.append(song)
                break
    if len(list_word) == 0:
        return "not found this words in any song"
    temp_string = "\n".join(map(str, list_word))
    return temp_string


def main():
    # read json file
    fo = open("pink.json", "r")
    pinkfloyd_alboms = json.load(fo)
    fo.close()

    # create a tcp socket
    listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # binding to local port 80
    server_address = ('localhost', 80)
    listening_sock.bind(server_address)

    # listen for incoming connections
    listening_sock.listen(1)

    # create a new conversation socket
    client_soc, client_address = listening_sock.accept()

    flag = True
    while flag:

        # Receiving data from the client
        client_msg = client_soc.recv(1024)
        client_msg = client_msg.decode('utf-8')

        # answer to client
        if client_msg == '1':
            answer = get_all_albums(pinkfloyd_alboms)
            str(answer)

        elif client_msg.startswith('2'):
            client_msg = client_msg[1:]
            answer = get_all_song_of_album(client_msg, pinkfloyd_alboms)

        elif client_msg.startswith('3'):
            client_msg = client_msg[1:]
            answer = get_length_of_song(client_msg, pinkfloyd_alboms)

        elif client_msg.startswith('4'):
            client_msg = client_msg[1:]
            answer = get_words_from_song(client_msg, pinkfloyd_alboms)

        elif client_msg.startswith('5'):
            client_msg = client_msg[1:]
            answer = get_album_where_song_is(client_msg, pinkfloyd_alboms)
            str(answer)

        elif client_msg.startswith('6'):
            client_msg = client_msg[1:]
            answer = search_word(client_msg, pinkfloyd_alboms)
            str(answer)

        elif client_msg == "7":
            answer = "by by"
            flag = False

        else:
            answer = 'wrong command'

        # sending data back
        answer = bytes(answer, 'utf-8')
        client_soc.sendall(answer)

    # closing the conversation socket
    client_soc.close()

    # closing the listening socket
    listening_sock.close()


if __name__ == "__main__":
    main()
