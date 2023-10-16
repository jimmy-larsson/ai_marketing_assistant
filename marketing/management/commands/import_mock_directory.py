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
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError as e:
                        self.stdout.write(self.style.ERROR(f'Invalid JSON format in {filename}: {e}'))
                        continue

                    model_name = filename[:-5]  # Remove ".json" from filename to get the model name
                    self.stdout.write(self.style.SUCCESS(f'Importing {model_name}...'))

                    # Loading the data into the Django model
                    try:
                        call_command('loaddata', filepath)
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'An error occurred while importing {model_name}: {e}'))
                        continue

        self.stdout.write(self.style.SUCCESS('Mock data imported successfully'))
