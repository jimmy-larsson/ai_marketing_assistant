from django.core.management.base import BaseCommand, CommandError
import os
import json
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Import mock data from JSON files in the provided directory'

    def add_arguments(self, parser):
        parser.add_argument('directory', type=str, help='Path to directory containing mock JSON files.')

    def handle(self, *args, **kwargs):
        directory = kwargs['directory']
        if not os.path.isdir(directory):
            raise CommandError(f"{directory} is not a valid directory")

        for filename in os.listdir(directory):
            if filename.endswith(".json"):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    model_name = filename[:-5]  # Remove ".json" from filename to get the model name
                    self.stdout.write(self.style.SUCCESS(f'Importing {model_name}...'))
                    call_command('loaddata', filepath)

        self.stdout.write(self.style.SUCCESS('Mock data imported successfully'))
