fobj=open("dravid.txt","r")
strike_rates = li
for line in fobj:
    columns=line.split()
    runs = int(columns[2])
    skills =int(columns[3])
    strike_rate = runs/balls*100
    strike_rates.append(string_rate)

import statistics as st
deviation=statistics.stdev(strike_rates)
print(deviation)
