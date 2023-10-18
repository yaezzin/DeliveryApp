from typing import Any
from django.core.management import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Checking if the database is empty"

    def handle(self, *args, **options):
        try:
            if not User.objects.exists():
                self.stdout.write("empty")
            else:
                self.stdout.write("not empty")
        except Exception as e:
            self.stdout.write(f"An error occurred: {str(e)}")
