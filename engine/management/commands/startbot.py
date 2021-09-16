from django.core.management.base import BaseCommand
from engine.bot import VKBot


class Command(BaseCommand):
    help = 'Start Cloudlet'
    
    def handle(self, *args, **options):
        current_bot = VKBot()