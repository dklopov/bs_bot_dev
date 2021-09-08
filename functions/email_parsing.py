from functions.connect_beatstars_com import connect_beatstars_com


def get_email_list_parsing(users):
    accounts_for_parsing = users.replace(" ", "").replace(".", ",").split(",")
    n = 0
    while n < len(accounts_for_parsing):
        url_from_request = "/musician?permalink=" + accounts_for_parsing[n] + "&fields=profile,stats,email"
        data_json = connect_beatstars_com(url_from_request=url_from_request)
        try:
            user_email = data_json['response']['data']['email']
            raw_users_list.append(accounts_for_parsing[n])
            raw_emails_list.append(user_email)
            n += 1
        except KeyError:
            n += 1
    return raw_users_list, raw_emails_list


raw_users_list = []
raw_emails_list = []
