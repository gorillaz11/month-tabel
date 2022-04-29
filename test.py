month_name="april"
days_name=["Mo","Tu","We","Th","Fr","Sa","Su"]
month_temps=[
[None, None, None, None, 4.0, 3.0, 2.0],
[8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0],
[2.0, 7.0, 6.0, 2.0, 4.0, 2.0, 3.0],
[8.0, 2.0, 6.0, 5.0, 10.0, 3.0, 2.0],
[8.0, 7.0, 6.0, 2.0, 3.0, 3.0, 2.0],


]
month_temps_1d=[]
for wi in range(5):
    for di in range(7):
        if month_temps[wi][di] !=None:
            month_temps_1d.append(month_temps[wi][di])
max_temps=max(month_temps_1d)
min_temps=min(month_temps_1d)


print("------------------------------------------------")
print(f"|{month_name:54}|   |")
print("------------------------------------------------")
for di in range(7):
    print(f"|{days_name[di]}",end="")
print("|  |")
print("------------------------------------------------")
date=1
#Rewrite code using if else
for wi in range(5):
    for di in range(7):
        if month_temps[wi][di] !=None:
            date_str=" " * 6 
        else:  
            date_str=date
            date+=1
        print(f"|{date_str:6}",end="")
        print("|  |")
    #code for week numbers
    for di in range(7):
        temp = f"|{month_temps[wi][di]:6.1f}" if month_temps[wi][di] !=None else " " * 7
        print(f"|{temp} ",end="")
    print("|  |")
    print("------------------------------------------------")
print(f"Max temp: {max_temps}")
print(f"Min temp: {min_temps}")