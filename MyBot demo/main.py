import requests as requests
import aiml as aiml

url = "https://api.telegram.org/bot971944218:AAFopNJLebUC3hXHF9PG8LnywpeN8gu2zSY"
li = "<li>"


# create func that get chat id
def get_chat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id


# create function that get message text
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text


# create function that get last_update
def last_update(req):
    response = requests.get(req + "/getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]  # get last record message update


# create function that let bot send message to user
def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url + "/sendMessage", data=params)
    return response


def get_id_sintomes(idmalaltia):
    id = ""
    it = 0
    enfermedadhtml = requests.get("https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=ES&Expert=" + idmalaltia)
    # print(enfermedadhtml.text)
    for _ in enfermedadhtml.text:
        if enfermedadhtml.text[it] == "D":
            if enfermedadhtml.text[it:it + 28] == "Disease_HPOTerms.php?lng=ES&":
                it2 = it + 28
                while "0" > enfermedadhtml.text[it2] or "9" < enfermedadhtml.text[it2]:
                    it2 += 1
                while "0" <= enfermedadhtml.text[it2] <= "9":
                    id += enfermedadhtml.text[it2]
                    it2 += 1
        it += 1
    return id


def getsintomes(idsintoma):

    sintoma = ""
    it = 0
    b = 0

    sintomeshtml = requests.get("https://www.orpha.net/consor/cgi-bin/Disease_HPOTerms.php?lng=ES&data_id=" + idsintoma + "&Typ=Pat&diseaseType=Pat&from=rightMenu")
    numerosintomes = 10
    for _ in sintomeshtml.text:
        if numerosintomes > 0:
            if b == 0:
                if sintomeshtml.text[it] == "M":
                    if sintomeshtml.text[it:it+13] == "Muy frecuente":
                        b = 1
                        it2 = it+13
                        sintoma += "SINTOMAS \n"
                        s = ""
                        while sintomeshtml.text[it2:it2+4] != li:
                            it2 += 1
                        it2 += 4
                        while sintomeshtml.text[it2] != "<":
                            s += sintomeshtml.text[it2]
                            it2 += 1
                        numerosintomes -= 1
                        sintoma += s + "\n"

                        itaux = it2

                        while sintomeshtml.text[itaux:itaux+7] != "<footer" and numerosintomes > 0:
                            s = ""
                            while sintomeshtml.text[it2:it2 + 4] != li:
                                it2 += 1
                            it2 += 4
                            while sintomeshtml.text[it2] != "<":
                                s += sintomeshtml.text[it2]
                                it2 += 1
                            itaux = it2 + 1
                            sintoma += s + "\n"
                            numerosintomes -= 1
        it += 1
    return sintoma


# create main function for navigate or reply message back
def main():
    bot = aiml.Kernel()
    bot.learn("std-startup.xml")
    bot.respond("load aiml b")

    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id + 1 == update["update_id"]:
            message = get_message_text(update).lower()
            messagebot = bot.respond(message)
            if messagebot == "":
                send_message(get_chat_id(update), "Lo siento, no te entendí")
            elif "0" <= messagebot[0] <= "9":
                fullmessage = "https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=ES&Expert=" + messagebot
                send_message(get_chat_id(update), "Aqui tienes informacion: \n" + fullmessage)
            elif messagebot[0] == "s" and messagebot[1] == "-":
                idsintoma = get_id_sintomes(messagebot[2:])
                if messagebot[2:] == "":
                    send_message(get_chat_id(update), "Lo siento, no dispongo informacion sobre los sintomas de esta enfermedad")
                else:
                    sintomes = getsintomes(idsintoma)
                    if sintomes == "":
                        send_message(get_chat_id(update),"Lo siento, no dispongo informacion sobre los sintomas de esta enfermedad")
                    else:
                        textsintomes = sintomes + "\n Mas informacion en el siguiente enlace: \n https://www.orpha.net/consor/cgi-bin/Disease_HPOTerms.php?lng=ES&data_id=" + idsintoma + "&Typ=Pat&diseaseType=Pat&from=rightMenu"
                        send_message(get_chat_id(update), textsintomes)
            else:
                send_message(get_chat_id(update), messagebot)
            update_id += 1


# call the function to make it reply
main()
