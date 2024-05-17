from datetime import datetime,timedelta, date
# apollo_pristani = datetime.fromisoformat("1969-07-21T18:54:00")

# retezec = "1. 5. 2024, 18:38"
# print(datetime.strptime(retezec, "%d. %m. %Y, %H:%M"))

apollo_start = datetime(1969, 7, 16, 14, 32)
print(apollo_start)                                 # základní zadání úkolu

#apollo_start = "7 / 16 / 1969"
apollo_start_am = apollo_start.strftime("%m/%d/%Y")
print(apollo_start_am)                                 # výstup s lomítkama v americké verzi


#Satelit Solar Orbiter start  10.2.2020 v 5:03  - urči den v týdnu/ kolik času od jeho startu uplynulo

orbiter_start_day = datetime(2020, 2, 10, 5, 3)
den_v_tydnu = orbiter_start_day.weekday()
print(f"Solar Orbiter odstartoval v {den_v_tydnu}")

den_v_tydnu = orbiter_start_day.strftime("%A")           
print(f"Solar Orbiter odstartoval v {den_v_tydnu}")


aktualni_cas = datetime.now()
cas_od_startu = aktualni_cas - orbiter_start_day
print(cas_od_startu)


