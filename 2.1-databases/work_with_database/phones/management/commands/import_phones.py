import csv
from django.core.management.base import BaseCommand
from phones.models import Phone

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone_data in phones:
            # Создаем новый объект Phone
            phone = Phone(
                name=phone_data['name'],
                price=phone_data['price'],
                image=phone_data['image'],
                release_date=phone_data['release_date'],
                lte_exists=phone_data['lte_exists']
            )
            # Сохраняем объект в базе данных
            phone.save()

        self.stdout.write(self.style.SUCCESS('Телефоны успешно импортированы!'))

