from django.core.management import BaseCommand
from core.models import User, Wallet


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.seed()

    def seed(self):
        # Create User
        user = User.objects.create(first_name="Test", last_name="User")

        # Create Wallet and assign to user
        Wallet.objects.create(user_id=user.id, name="Test Wallet")
