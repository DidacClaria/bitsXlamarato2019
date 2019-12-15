import requests as requests


def main():

    output = open("malalties.aiml", "w+")
    output.write("<aiml version=\"1.0.1\" encoding=\"UTF-8\">\n")
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
                elif x == 1:
                    url += j
                elif x == 2 and ord(j) == 62:
                    x = 3
                elif x == 3 and ord(j) == 60:
                    x = 4

                    aux = 0
                    newurl = ""

                    for char in url:
                        if char == "=" and aux == 0:
                            aux = 1
                        elif char == "=" and aux == 1:
                            aux = 2
                        elif aux == 2 and "0" <= char <= "9":
                            newurl += char
                        elif aux == 2 and char == "\n":
                            aux = 0

                    name = name.upper()
                    output.write("<category><pattern> * ")
                    output.write(name)
                    output.write(" * </pattern><template>")
                    output.write(newurl)
                    output.write(" </template></category>\n")

                    output.write("<category><pattern> * ")
                    output.write(name)
                    output.write(" </pattern><template>")
                    output.write(newurl)
                    output.write(" </template></category>\n")

                    output.write("<category><pattern> ")
                    output.write(name)
                    output.write(" * </pattern><template>")
                    output.write(newurl)
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
                        output.write(newurl)
                        output.write(" </template></category>\n")

                        output.write("<category><pattern> * ")
                        output.write(name)
                        output.write(" </pattern><template>")
                        output.write(newurl)
                        output.write(" </template></category>\n")

                        output.write("<category><pattern> ")
                        output.write(name)
                        output.write(" * </pattern><template>")
                        output.write(newurl)
                        output.write(" </template></category>\n")

                    #print("https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=ES&Expert=" + newurl)

                elif x == 3:
                    name += j

                else:
                    x = 0
        f.close()
    output.write("</aiml>")
    output.close()


main()
