def messages_adapter(raw_users_list: list, raw_emails_list: list, command: str, subscription_type: str) -> str:
    lists = []
    lists.append(raw_users_list)
    lists.append(raw_emails_list)
    lists_raw = list(map("::".join, zip(*lists)))
    if command == 'email':
        if subscription_type == 'free':
            message_to_send = raw_emails_list[0]
        else:
            message_to_send = str(lists_raw).replace("::", "</td>\n<td style=\"width: 50%;\">").replace("', '", "</td>\n</tr>\n<tr>\n<td style=\"width: 50%;\">").replace("['", "<tr>\n<td style=\"width: 50%;\">").replace("']", "</td>\n</tr>")
    return message_to_send