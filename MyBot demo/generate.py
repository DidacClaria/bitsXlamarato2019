import requests as requests

def main():

    f = open("malalties.txt", "r")
    lineas = f.readlines()

    for linea in lineas:
        for caracter in linea:
            if ord(caracter) == 39:
                x = 1


def old_main():

    output = open("malalties.txt", "w+")

    for i in range(ord('A'), ord('Z') + 1):

        f = open(chr(i)+".txt", "r")

        f1 = f.readlines()

        for i in f1:
            x = 0
            url = ""
            name = ""
            for j in i:
                if ord(j) == 39 and x == 0:
                    x = 1
                elif ord(j) == 39 and x == 1:
                    x = 2
                    #urlcomplete = "https://www.orpha.net/consor/cgi-bin/" + url
                    #test = requests.get(urlcomplete)
                    #print(test.text)
                    output.write("https://www.orpha.net/consor/cgi-bin/" + url + "'")
                elif x == 1:
                    url += j
                elif x == 2 and ord(j) == 62:
                    x = 3
                elif x == 3 and ord(j) == 60:
                    x = 4
                    output.write(name + "\n")
                    #print(name)
                elif x == 3:
                    name += j
                else:
                    x = 0
        f.close()
    output.close()


main()
