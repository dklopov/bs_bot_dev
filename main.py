import telebot

from classes.classes import Bot
from functions.email_parsing import get_email_list_parsing
from functions.email_parsing import raw_emails_list
from functions.email_parsing import raw_users_list
from functions.fans_parsing import users as fans_parsing_users
from functions.fans_parsing import get_fans_list_for_parsing
from functions.messages_adapter import messages_adapter
from functions.send_result import send_result_on_gmail
from functions.send_result import send_result_on_telegram
from users.pro_users import pro_users_email
from users.pro_users import pro_users_name

bot = telebot.TeleBot(Bot().get_token())

if __name__ == "__main__":
    @bot.message_handler(commands=["get_email"])
    def email(message):
        bot.send_message(message.from_user.id, 'Укажи имена битмейкеров/клиентов через запятую')
        users = message
        bot.register_next_step_handler(users, email_result)


    def email_result(users):
        receiver_id = users.from_user.id
        receiver_name = users.from_user.username

        if receiver_name in pro_users_name:
            bot.send_message(receiver_id, 'Собираю данные, результаты будут отправлены на почту указанную при оплате')
            print(users.text)
            get_email_list_parsing(users=users.text)
            message_to_send = messages_adapter(raw_users_list=raw_users_list, raw_emails_list=raw_emails_list, command="email", subscription_type='pro')
            send_result_on_gmail(message=message_to_send, receiver_email=pro_users_email[receiver_name])
            bot.send_message(receiver_id, 'Результаты отправлены на почту {}'.format(pro_users_email[receiver_name]))
        else:
            print(users.text)
            get_email_list_parsing(users=users.text)
            message_to_send = messages_adapter(raw_users_list=raw_users_list, raw_emails_list=raw_emails_list, command="email", subscription_type='free')
            send_result_on_telegram(message=message_to_send, receiver_id=receiver_id)

        raw_users_list.clear()
        raw_emails_list.clear()


    @bot.message_handler(commands=["get_fans_email"])
    def email(message):
        bot.send_message(message.from_user.id, 'Укажи ссылку на бит вида "https://www.beatstars.com/beat/pressure-8395689"')
        url = message
        bot.register_next_step_handler(url, fans_email)

    def fans_email(url):
        receiver_id = url.from_user.id
        receiver_name = url.from_user.username

        if receiver_name in pro_users_name:
            bot.send_message(receiver_id, 'Собираю данные, результаты будут отправлены на почту указанную при оплате.\nПримерное время выполнения 10 минут')
            fans_list = get_fans_list_for_parsing(track_url=url.text)
            get_email_list_parsing(users=fans_list)
            message_to_send = messages_adapter(raw_users_list=raw_users_list, raw_emails_list=raw_emails_list, command="email", subscription_type='pro')
            send_result_on_gmail(message=message_to_send, receiver_email=pro_users_email[receiver_name])
            bot.send_message(receiver_id, 'Результаты отправлены на почту {}'.format(pro_users_email[receiver_name]))
        else:
            message_to_send = 'Функция доступна только для PRO-подписки'
            send_result_on_telegram(message=message_to_send, receiver_id=receiver_id)

        raw_users_list.clear()
        raw_emails_list.clear()
        fans_parsing_users.clear()


    bot.polling(none_stop=True, interval=0)