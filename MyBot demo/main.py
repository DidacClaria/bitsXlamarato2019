import requests as requests
import aiml as aiml

url = "https://api.telegram.org/bot1044048944:AAGJZOVrUUThYIcEfkd0IwBdPnYSIsQ7jHs"


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
                send_message(get_chat_id(update), "no entendí, parsero")
            elif "0" <= messagebot[0] <= "9":
                fullmessage = "https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=ES&Expert=" + messagebot
                send_message(get_chat_id(update), "Aqui tienes informacion: \n" + fullmessage)
            else:
                send_message(get_chat_id(update), messagebot)
            update_id += 1


# call the function to make it reply
main()
