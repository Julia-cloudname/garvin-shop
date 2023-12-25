from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ Checkout app configuration"""
    name = 'checkout'

    def ready(self):
        import checkout.signals