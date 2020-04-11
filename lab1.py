import datetime
import csv
#исходящие и смс
with open('data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
           if row[1] =='933156729':
            time1 = row[0]
            duration1 = row[3]
            sms = row[4]
dtime1 = datetime.datetime.strptime(time1, '%Y-%m-%d %H:%M:%S')
if dtime1 < datetime.datetime(2020,1,1,00,30,00):
  outgoing=3*float(duration1)
  print('Стоимость исходящих звонков:',outgoing,'рублей')
if dtime1 > datetime.datetime(2020,1,1,00,30,00):
  outgoing=2*float(duration1)
  print('Стоимость исходящих звонков:',outgoing,'рублей')
sms_cost=(int(sms) - 50)*2
print('Стоимость смс:',sms_cost,'рублей')
#входящие
with open('data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
          if row[2] =='933156729':
              time2 = row[0]
              duration2 = row[3]
dtime2=datetime.datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')
if dtime2 < datetime.datetime(2020,1,1,00,30,00):
  incoming=0*float(duration2)
  print('Стоимость входящих звонков:',incoming,'рублей')
if dtime2 > datetime.datetime(2020,1,1,00,30,00):
  incoming=2*float(duration2)
  print('Стоимость входящих звонков:',incoming,'рублей')

