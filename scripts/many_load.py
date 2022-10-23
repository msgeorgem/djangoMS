import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unescoo.models import Category, State, Iso, Region, Site


def run():
    fhand = open('unescoo/load1.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[5])
        s, created = State.objects.get_or_create(name=row[6])
        i, created = Iso.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[7])
        n, created = Site.objects.get_or_create(name=row[0])
        y, created = Site.objects.get_or_create(year=row[1])
        la, created = Site.objects.get_or_create(latitude=row[3])
        lon, created = Site.objects.get_or_create(longitude=row[2])
        a, created = Site.objects.get_or_create(area_hectares=row[4])

        try:
            y = int(row[1])
        except:
            y = 0

        try:
            la = float(row[3])
        except:
            la = 0

        try:
            lon = float(row[2])
        except:
            lon = 0

        try:
            a = int(row[4])
        except:
            a = 0

        s = Site(name=n, year=y, latitude=la, longitude=lon, area_hectares=a, category=c, region=r, iso=i,
                 state=s)
        s.save()
