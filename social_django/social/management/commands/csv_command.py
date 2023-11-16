import csv
from django.core.management.base import BaseCommand
from social.models import Category

class Command(BaseCommand):
    help = 'Cargar datos desde un archivo CSV a un modelo específico'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Ruta al archivo CSV')

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                Category.objects.create(name=row[0], description=row[1])

        self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente desde el archivo CSV.'))

