import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import telebot
from classes.classes import Bot
bot = telebot.TeleBot(Bot().get_token())


def send_result_on_gmail(message: str, receiver_email: str) -> None:
    """ Функция отправляет письмо на переданный в нее gmail"""
    server = 'smtp.gmail.com'
    user = 'beatstars.helper.bot@gmail.com'
    password = 'uvrlgsmxprnhodty'
    recipients = [receiver_email]
    sender = 'beatstars.helper.bot@gmail.com'
    subject = 'Результаты парсинга ' + str(datetime.date.today())

    html = message

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'beatstars_helper_bot <' + sender + '>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/'
    part_text = MIMEText(message, 'plain')
    part_html = MIMEText(html, 'html')
    msg.attach(part_text)
    msg.attach(part_html)
    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()


def send_result_on_telegram(message, receiver_id):
    text_for_message = message.replace("[", "").replace("]", "").replace("',", "\n").replace(" '", "").replace("'", "")
    bot.send_message(receiver_id, text_for_message)
    return text_for_message