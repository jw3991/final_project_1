import re
import csv
from sightings.models import Squirrel
from django.core.management import BaseCommand
from datetime import date
# from dateutil import parser


class Command(BaseCommand):
    help = 'Import squirrel data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']

        pattern = re.compile(r'(\d{2})(\d{2})(\d{4})')

        with open(path, 'rt') as fp:
            data0 = csv.reader(fp, dialect='excel')
            next(data0)
            Unique_ID = list()
            for row in data0:
                if row[2] in Unique_ID:
                    continue
                else:
                    month, day, year = pattern.match(row[5]).groups()
                    squirrel = Squirrel.objects.get_or_create(
                        Longitude=float(row[0]),
                        Latitude=float(row[1]),
                        Unique_Squirrel_ID=row[2],
                        Shift=row[4],
                        Date=date(int(year), int(month), int(day)),
                        Age=row[7],
                        Primary_Fur_Color=row[8],
                        Location=row[12],
                        Specific_Location=row[14],
                        Running=True if row[15].lower() == 'true' else False,
                        Chasing=True if row[16].lower() == 'true' else False,
                        Climbing=True if row[17].lower() == 'true' else False,
                        Eating=True if row[18].lower() == 'true' else False,
                        Foraging=True if row[19].lower() == 'true' else False,
                        Other_Activities=row[20],
                        Kuks=True if row[21].lower() == 'true' else False,
                        Quaas=True if row[22].lower() == 'true' else False,
                        Moans=True if row[23].lower() == 'true' else False,
                        Tail_Flags=True if row[24].lower() == 'true' else False,
                        Tail_Twitches=True if row[25].lower() == 'true' else False,
                        Approaches=True if row[26].lower() == 'true' else False,
                        Indifferent=True if row[27].lower() == 'true' else False,
                        Runs_From=True if row[28].lower() == 'true' else False
                    )
                    Unique_ID.append(row[2])
