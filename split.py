b_day = input ("Enter your birth day (dd mm yy) : ")
string = b_day.split()
dict = {
     "date": string[0],
     "month" : string[1],
     "year" : string[2]
}

it = []
for key , value in dict.items():
    it = it + [key +" " + value]
res = ", ".join(it)

print(res)