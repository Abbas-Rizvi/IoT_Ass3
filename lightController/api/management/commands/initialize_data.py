# yourapp/management/commands/initialize_data.py
from django.core.management.base import BaseCommand
from api.models import Mode, State

# used to initialize data for the mode and state
# only needed on first run
class Command(BaseCommand):
    help = 'Initialize data for the light controller'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Initializing data...'))

        # Create the Mode object with a specific primary key
        mode, created = Mode.objects.get_or_create(id=1, defaults={'name': 'auto'})
        if not created:
            self.stdout.write(self.style.SUCCESS('Mode object with ID 1 already exists.'))

        # Create the Mode object with a specific primary key
        state, created = State.objects.get_or_create(id=1, defaults={'name': 'on'})
        if not created:
            self.stdout.write(self.style.SUCCESS('Mode object with ID 1 already exists.'))

        self.stdout.write(self.style.SUCCESS('Data initialized successfully'))
