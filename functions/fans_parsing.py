from functions.connect_beatstars_com import connect_beatstars_com


def get_fans_list_for_parsing(track_url: str):
    track_id = track_url.split("-")[1]
    url_from_request = ('https://main.v2.beatstars.com/fans/track/?id=' + str(track_id) + '&list_limit=1000')
    print(url_from_request)
    data_json = connect_beatstars_com(url_from_request=url_from_request)
    data_list = data_json['response']['data']['list']
    n = 0
    while len(data_list) > n:
        try:
            permalink = data_json['response']['data']['list'][n]['musician']['permalink']
            users.append(permalink)
            n += 1
        except:
            n += 1
    return users


users = []
