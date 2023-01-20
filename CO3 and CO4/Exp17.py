class time:
    def __init__(self, hour, minute, sec):
        self.__hour = hour
        self.__minute = minute
        self.__sec = sec

    def __add__(self, other):
        t3.__hour = self.__hour + other.__hour
        t3.__minute = self.__minute + other.__minute
        t3.__sec = self.__sec + other.__sec
        if t3.__sec > 59:
           t3.__sec -= 60
           t3.__minute += 1
        if t3.__minute > 59:
           t3.__minute -= 60
           t3.__hour += 1
        return str(t3.__hour) + ":" + str(t3.__minute) + ":" + str(t3.__sec)



h1 = int(input("Enter the hour: "))
m1 = int(input("Enter the minute: "))
s1 = int(input("Enter the second: "))
h2 = int(input("Enter the number of hours to be added: "))
m2 = int(input("Enter the number of minutes to be added: "))
s2 = int(input("Enter the number of seconds to be added: "))
t1 = time(h1, m1, s1)
t2 = time(h2, m2, s2)
t3= time(0,0,0)
print(t1 + t2)
