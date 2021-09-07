from functions.email_parsing import get_email_list_parsing
from functions.email_parsing import raw_emails_list
from functions.email_parsing import raw_users_list
from functions.messages_adapter import messages_adapter

if __name__ == "__main__":
    a = get_email_list_parsing(users="mantra, hybrid factory")
    b = messages_adapter(raw_users_list=raw_users_list, raw_emails_list=raw_emails_list)
    print(b)
    # pass