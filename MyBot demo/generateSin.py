import requests as requests


def main():

    output2 = open("sintomas.aiml", "w+")
    output2.write("<aiml version=\"1.0.1\" encoding=\"UTF-8\">\n")
    for i in range(ord('A'), ord('Z') + 1):

        f = open(chr(i)+".txt", "r")

        print(i)

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

                    id = ""
                    it = 0
                    enfermedadhtml = requests.get("https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=ES&Expert=" + newurl)
                    #print(enfermedadhtml.text)
                    for _ in enfermedadhtml.text:
                        if enfermedadhtml.text[it] == "D":
                            if enfermedadhtml.text[it:it+28] == "Disease_HPOTerms.php?lng=ES&":
                                it2 = it+28
                                while "0" > enfermedadhtml.text[it2] or "9" < enfermedadhtml.text[it2]:
                                    it2 += 1
                                while "0" <= enfermedadhtml.text[it2] <= "9":
                                    id += enfermedadhtml.text[it2]
                                    it2 += 1
                        it += 1

                    #print(id)

                    name = name.upper()

                    output2.write("<category><pattern> * ")
                    output2.write("SINTOMAS * " + name)
                    output2.write(" * </pattern><template>")
                    output2.write(id)
                    output2.write(" </template></category>\n")

                    output2.write("<category><pattern> * ")
                    output2.write(" SINTOMAS " + name)
                    output2.write(" * </pattern><template>")
                    output2.write(id)
                    output2.write(" </template></category>\n")

                    output2.write("<category><pattern> * ")
                    output2.write("SINTOMAS * " + name)
                    output2.write(" </pattern><template>")
                    output2.write(id)
                    output2.write(" </template></category>\n")

                    output2.write("<category><pattern> * ")
                    output2.write("SINTOMAS " + name)
                    output2.write(" </pattern><template>")
                    output2.write(id)
                    output2.write(" </template></category>\n")

                    output2.write("<category><pattern> ")
                    output2.write("SINTOMAS * " + name)
                    output2.write(" * </pattern><template>")
                    output2.write(id)
                    output2.write(" </template></category>\n")

                    output2.write("<category><pattern> ")
                    output2.write("SINTOMAS " + name)
                    output2.write(" * </pattern><template>")
                    output2.write(id)
                    output2.write(" </template></category>\n")

                    output2.write("<category><pattern> * ")
                    output2.write("SINTOMAS * " + name)
                    output2.write(" * </pattern><template>")
                    output2.write(id)
                    output2.write(" </template></category>\n")

                    output2.write("<category><pattern> * ")
                    output2.write("SINTOMAS " + name)
                    output2.write(" * </pattern><template>")
                    output2.write(id)
                    output2.write(" </template></category>\n")

                    output2.write("<category><pattern> * ")
                    output2.write("SINTOMAS * " + name)
                    output2.write(" </pattern><template>")
                    output2.write(id)
                    output2.write(" </template></category>\n")

                    output2.write("<category><pattern> * ")
                    output2.write("SINTOMAS " + name)
                    output2.write(" </pattern><template>")
                    output2.write(id)
                    output2.write(" </template></category>\n")

                    output2.write("<category><pattern> ")
                    output2.write("SINTOMAS * " + name)
                    output2.write(" * </pattern><template>")
                    output2.write(id)
                    output2.write(" </template></category>\n")

                    output2.write("<category><pattern> ")
                    output2.write("SINTOMAS * " + name)
                    output2.write(" * </pattern><template>")
                    output2.write(id)
                    output2.write(" </template></category>\n")

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
                        output2.write("<category><pattern> * ")
                        output2.write("SINTOMAS * " + name)
                        output2.write(" * </pattern><template>")
                        output2.write(id)
                        output2.write(" </template></category>\n")

                        output2.write("<category><pattern> * ")
                        output2.write(" SINTOMAS " + name)
                        output2.write(" * </pattern><template>")
                        output2.write(id)
                        output2.write(" </template></category>\n")

                        output2.write("<category><pattern> * ")
                        output2.write("SINTOMAS * " + name)
                        output2.write(" </pattern><template>")
                        output2.write(id)
                        output2.write(" </template></category>\n")

                        output2.write("<category><pattern> * ")
                        output2.write("SINTOMAS " + name)
                        output2.write(" </pattern><template>")
                        output2.write(id)
                        output2.write(" </template></category>\n")

                        output2.write("<category><pattern> ")
                        output2.write("SINTOMAS * " + name)
                        output2.write(" * </pattern><template>")
                        output2.write(id)
                        output2.write(" </template></category>\n")

                        output2.write("<category><pattern> ")
                        output2.write("SINTOMAS " + name)
                        output2.write(" * </pattern><template>")
                        output2.write(id)
                        output2.write(" </template></category>\n")

                        output2.write("<category><pattern> * ")
                        output2.write("SINTOMAS * " + name)
                        output2.write(" * </pattern><template>")
                        output2.write(id)
                        output2.write(" </template></category>\n")

                        output2.write("<category><pattern> * ")
                        output2.write("SINTOMAS " + name)
                        output2.write(" * </pattern><template>")
                        output2.write(id)
                        output2.write(" </template></category>\n")

                        output2.write("<category><pattern> * ")
                        output2.write("SINTOMAS * " + name)
                        output2.write(" </pattern><template>")
                        output2.write(id)
                        output2.write(" </template></category>\n")

                        output2.write("<category><pattern> * ")
                        output2.write("SINTOMAS " + name)
                        output2.write(" </pattern><template>")
                        output2.write(id)
                        output2.write(" </template></category>\n")

                        output2.write("<category><pattern> ")
                        output2.write("SINTOMAS * " + name)
                        output2.write(" * </pattern><template>")
                        output2.write(id)
                        output2.write(" </template></category>\n")

                        output2.write("<category><pattern> ")
                        output2.write("SINTOMAS * " + name)
                        output2.write(" * </pattern><template>")
                        output2.write(id)
                        output2.write(" </template></category>\n")

                elif x == 3:
                    name += j

                else:
                    x = 0
        f.close()
    output2.write("</aiml>")
    output2.close()


main()
