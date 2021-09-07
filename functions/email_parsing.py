# def get_email_list_parsing(accounts_for_parsing_raw):
#     email_list = []
#     email_list_for_send_email = []
#     email_list_for_message = str(email_list).replace("[", "").replace("]", "").replace("',", "\n").replace(" '", "").replace("'", "")
#     accounts_for_parsing = accounts_for_parsing_raw.text.replace(" ", "").replace(".", ",").split(",")
#     len_accounts_for_parsing = len(accounts_for_parsing)
#     n = 0
#     while n < len_accounts_for_parsing:
#         url_from_request = "/musician?permalink=" + accounts_for_parsing[n] + "&fields=profile,stats,email"
#         data_json = connect_beatstars_com(url_from_request=url_from_request)
#         try:
#             user_id = str(accounts_for_parsing_raw.from_user.id)
#             email = data_json['response']['data']['email']
#             user_name = data_json["response"]["data"]["profile"]["display_name"]
#             user_type = data_json['response']['data']['profile']['user_type']
#             user_stats_followers = data_json['response']['data']['stats']['followers']
#             user_stats_plays = data_json['response']['data']['stats']['plays']
#             user_stats_tracks = data_json['response']['data']['stats']['tracks']
#             user_stats_following = data_json['response']['data']['stats']['following']
#         except KeyError:
#             n += 1
#         bot.send_message(accounts_for_parsing_raw.from_user.id,
#                          'email: ' + str(email) +
#                          '\nuser_type: ' + str(user_type) +
#                          '\nuser_followers: ' + str(user_stats_followers) +
#                          '\nuser_plays: ' + str(user_stats_plays) +
#                          '\nuser_tracks: ' + str(user_stats_tracks) +
#                          '\nuser_following: ' + str(user_stats_following) +
#                          '\nuser_id: ' + str(user_id)
#                          )
#         email_for_send_email = "<tr><td style=\"width: 25%;\">" + user_name + "</td><td style=\"width: 25%;\">" + email + "</td></tr>"
#         email_list.append(email)
#         email_list_for_send_email.append(email_for_send_email)
#         n += 1
#     if len(email_list) > 5:
#         send_message_telegram(user_id=user_id, text="Результатов больше 10, список емейлов будет отправлен на почту")
#         send_message_email(text=str(email_list_for_send_email))
#     else:
#         send_message_telegram(user_id=user_id, text=str(email_list))
from functions.connect_beatstars_com import connect_beatstars_com

raw_users_list = []
raw_emails_list = []


def get_email_list_parsing(users):
    accounts_for_parsing = users.replace(" ", "").replace(".", ",").split(",")
    n = 0
    while n < len(accounts_for_parsing):
        url_from_request = "/musician?permalink=" + accounts_for_parsing[n] + "&fields=profile,stats,email"
        data_json = connect_beatstars_com(url_from_request=url_from_request)
        user_email = data_json['response']['data']['email']
        raw_users_list.append(accounts_for_parsing[n])
        raw_emails_list.append(user_email)
        n += 1
    return raw_users_list, raw_emails_list
