class SupportHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        pass

class LevelOneHandler(SupportHandler):
    def handle_request(self, request):
        if request == "technical_issue":
            print("Ваш запит про технічну проблему прийнято рівнем 1.")
        elif self.successor:
            self.successor.handle_request(request)
        else:
            print("На жаль, жоден рівень підтримки не може обробити ваш запит.")

class LevelTwoHandler(SupportHandler):
    def handle_request(self, request):
        if request == "billing_issue":
            print("Ваш запит про питання рахунку прийнято рівнем 2.")
        elif self.successor:
            self.successor.handle_request(request)
        else:
            print("На жаль, жоден рівень підтримки не може обробити ваш запит.")

class LevelThreeHandler(SupportHandler):
    def handle_request(self, request):
        if request == "complaint":
            print("Ваша скарга прийнята рівнем 3.")
        elif self.successor:
            self.successor.handle_request(request)
        else:
            print("На жаль, жоден рівень підтримки не може обробити ваш запит.")

class LevelFourHandler(SupportHandler):
    def handle_request(self, request):
        if request == "suggestion":
            print("Ваша пропозиція прийнята рівнем 4.")
        elif self.successor:
            self.successor.handle_request(request)
        else:
            print("На жаль, жоден рівень підтримки не може обробити ваш запит.")

if __name__ == "__main__":
    level_four_handler = LevelFourHandler()
    level_three_handler = LevelThreeHandler(level_four_handler)
    level_two_handler = LevelTwoHandler(level_three_handler)
    level_one_handler = LevelOneHandler(level_two_handler)

    level_one_handler.handle_request("technical_issue")
    level_one_handler.handle_request("billing_issue")
    level_one_handler.handle_request("complaint")
    level_one_handler.handle_request("suggestion")
    level_one_handler.handle_request("other_request")