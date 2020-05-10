import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
#обработка данных и тарификация
IP = '192.168.250.3'
kf = 3  
tr= pd.read_csv('nfcapd.csv', skiprows=1, header=None)
tr.columns = ['time', 'src', 'dst', 'inbyte','outbyte']
tr = tr[np.logical_or(tr.src == IP, tr.dst == IP)]
tr.inbyte = tr.inbyte.apply(lambda row: int(row) if 'M' not in row else (int(float(row[:-1])*10**6)))
tr.time = tr.time.apply(lambda row: row[10:18])
outgoing = tr[tr.src == IP].inbyte.sum() / 10**6
ingoing =  tr[tr.dst == IP].inbyte.sum() / 10**6
bill = kf*(outgoing + ingoing)
print(f'Результат тарификации: {bill:0.1f} рублей')
#построение графика зависимости
def graphic(times, size, format=None, save_to=None):
    fig, ax = plt.subplots(figsize=[10,5])
    ax.plot(times, size)
    Format = DateFormatter("%H:%M")
    ax.xaxis.set_major_formatter(Format)
    plt.ylabel('Байт')
    plt.xlabel('Время')
    plt.show()
times = np.sort(tr.time.unique())
size = []
for time in times:
    size.append(tr.loc[tr.time == time, ['inbyte', 'outbyte']].sum().sum())
graphic(pd.to_datetime(times), size)

