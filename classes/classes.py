class Bot:
    __bot_token = "1519614513:AAEjlL3GSEPtZG2Uln8luL0OCs7VaQ0H57I"  # prod
    # __bot_token = "1431872409:AAGYWjNLZUj2NbFJ0Z23DnUAz9ifqOA1CEQ"  # test

    def __str__(self):
        return "Класс содержит токен для подключения к боту, который я не покажу"

    def get_token(self):
        return self.__bot_token


class User:
    def __init__(self, user_name: str, user_id: int, user_subscription_type: str):
        self.user_id = user_id
        self.user_name = user_name
        self.user_subscription_type = user_subscription_type

    def __str__(self) -> str:
        return 'user_name: {}\nuser_id: {}\nuser_subscription_type: {}\n'.format(self.user_name, self.user_id, self.user_subscription_type)


class SubscriptionType:
    __free_subscription = {
        'start': 10,
        'health_check': 10,
        'donate': 10,
        'help': 10,
        'email': 10,
        'last_beat': 10,
        'beat_fans': 10
    }

    __pro_subscription = {
        'start': 100,
        'health_check': 100,
        'donate': 100,
        'help': 100,
        'trending_search': 100,
        'email': 100,
        'last_beat': 100,
        'beat_fans': 100,
        'beat_position': 100,
        'send_message_email': 100
    }

    def __init__(self, subscription_type):
        self.subscription_type = subscription_type

    def __str__(self):
        return 'user_subscription_type: {}'.format(self.subscription_type)

    def get_user_subscription_type_info(self):
        if self.subscription_type == 'free':
            return 'user_subscription_type: {}'.format(self.__free_subscription.keys())
        elif self.subscription_type == 'pro':
            return 'user_subscription_type: {}'.format(self.__pro_subscription.keys())
        else:
            return 'Несуществующий тип подписки'