# import datetime                 #as dt
# print(datetime.datetime.now())  #print(dt.datetime.now())

from datetime import datetime, timedelta, date
print(datetime.now())
print(datetime.today())
print(date.today())

muj_udaj = datetime(2024, 5, 1, 13, 00)
print(muj_udaj)
# print(muj_udaj.weekday())        # počítá od 0 / pondělí je 0 / rozmezí 0-6
# print(muj_udaj.isoweekday())     # podítá od 1 / pondělí je 1 /rozmezí 1-7

# 1.5.2024
print(muj_udaj.isoformat())
print(muj_udaj.strftime("%Y"))      
#  "%Y" je znak pro ROK / "%d" den / "%M" znamená minuta / "%m" je označení pro měsíc / "%S" sekunda / "%H" hodina
print(muj_udaj.strftime("%H: %M, %d. %m. %Y"))
print(muj_udaj.strftime("%A"))

import locale

# locale.setlocale(locale.LC_TIME, 'cs_CZ.UTF-8') # iOS

locale.setlocale(locale.LC_TIME, 'cz.UTF-8') # Windows?
print(locale.setlocale(locale.LC_TIME, 'cz.UTF-8'))

# retezec_iso = "2024-05-01T13:00:00"
# print(datetime.fromisoformat(retezec_iso))

# retezec = "1. 5. 2024, 18:38"
# print(datetime.strptime(retezec, "%d. %m. %Y, %H:%M"))   # tečky a čárky mezi datumama musí odpovídat zadání

dnes = datetime.today()
vcera = dnes - timedelta(days=1)
print(dnes, vcera)

datum_narozeni = datetime(1982, 6, 10)
print(datum_narozeni)
print(datetime.today() - datum_narozeni)

hodnota_timedelta = timedelta(days=10_000, hours=23, seconds=3)
print(hodnota_timedelta)


