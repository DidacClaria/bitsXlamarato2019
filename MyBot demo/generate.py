import requests as requests


def main():

    output = open("malalties.aiml", "w+")
    output.write("<aiml version=\"1.0.1\" encoding=\"UTF-8\">")
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
                    #output.write("https://www.orpha.net/consor/cgi-bin/" + url + "'")
                elif x == 1:
                    url += j
                elif x == 2 and ord(j) == 62:
                    x = 3
                elif x == 3 and ord(j) == 60:
                    x = 4
                    #output.write(name + "\n")
                    #print(name)
                    name = name.upper()
                    output.write("<category><pattern> * ")
                    output.write(name)
                    output.write(" * </pattern><template>")
                    output.write(url)
                    output.write(" </template></category>\n")

                    output.write("<category><pattern> * ")
                    output.write(name)
                    output.write(" </pattern><template>")
                    output.write(url)
                    output.write(" </template></category>\n")

                    output.write("<category><pattern> ")
                    output.write(name)
                    output.write(" * </pattern><template>")
                    output.write(url)
                    output.write(" </template></category>\n")

                    oldname = name
                    i = 0
                    for char in name:
                        if char == "Á":
                            name = name[:i] + 'A' + name[i+1:]
                        elif char == "É":
                            name = name[:i] + 'E' + name[i+1:]
                        elif char == "É":
                            name = name[:i] + 'E' + name[i+1]
                        elif char == "Í":
                            name = name[:i] + 'I' + name[i + 1:]
                        elif char == "Ó":
                            name = name[:i] + 'O' + name[i + 1:]
                        elif char == "Ú":
                            name = name[:i] + 'U' + name[i + 1:]
                        i += 1

                    if oldname != name:
                        output.write("<category><pattern> * ")
                        output.write(name)
                        output.write(" * </pattern><template>")
                        output.write(url)
                        output.write(" </template></category>\n")

                        output.write("<category><pattern> * ")
                        output.write(name)
                        output.write(" </pattern><template>")
                        output.write(url)
                        output.write(" </template></category>\n")

                        output.write("<category><pattern> ")
                        output.write(name)
                        output.write(" * </pattern><template>")
                        output.write(url)
                        output.write(" </template></category>\n")

                elif x == 3:
                    name += j

                else:
                    x = 0
        f.close()
    output.write("</aiml>")
    output.close()


main()
