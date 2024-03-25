from abc import ABC, abstractmethod

# Абстрактний клас підписки
class Subscription(ABC):
    def __init__(self, monthly_fee, min_subscription_period, channels):
        self.monthly_fee = monthly_fee
        self.min_subscription_period = min_subscription_period
        self.channels = channels

    @abstractmethod
    def get_info(self):
        pass

# Конкретні класи підписок
class BasicSubscription(Subscription):
    def get_info(self):
        return f"Basic Subscription: \nMonthly Fee: {self.monthly_fee}\nMinimum Subscription Period: {self.min_subscription_period} months\nChannels: {', '.join(self.channels)}\n"

class PremiumSubscription(Subscription):
    def get_info(self):
        return f"Premium Subscription: \nMonthly Fee: {self.monthly_fee}\nMinimum Subscription Period: {self.min_subscription_period} months\nChannels: {', '.join(self.channels)}\nHD Streaming\n"

# Фабричний метод для створення підписок
class SubscriptionFactory(ABC):
    @abstractmethod
    def create_subscription(self):
        pass

class WebSite(SubscriptionFactory):
    def create_subscription(self):
        return BasicSubscription(monthly_fee=10, min_subscription_period=6, channels=["Channel A", "Channel B", "Channel C"])

class MobileApp(SubscriptionFactory):
    def create_subscription(self):
        return PremiumSubscription(monthly_fee=20, min_subscription_period=12, channels=["Channel A", "Channel B", "Channel C", "Channel D"])

class ManagerCall(SubscriptionFactory):
    def create_subscription(self):
        return PremiumSubscription(monthly_fee=25, min_subscription_period=12, channels=["Channel A", "Channel B", "Channel C", "Channel D", "Channel E"])

# Використання фабричного методу
def main():
    subscription_factories = {
        "WebSite": WebSite(),
        "MobileApp": MobileApp(),
        "ManagerCall": ManagerCall()
    }

    for subscription_type, factory in subscription_factories.items():
        subscription = factory.create_subscription()
        print(f"{subscription_type} Subscription Info:\n{subscription.get_info()}")

if __name__ == "__main__":
    main()