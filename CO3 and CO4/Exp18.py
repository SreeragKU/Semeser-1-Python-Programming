class time:
    def __init__(self, hour, minute, sec):
        self.__hour = hour
        self.__minute = minute
        self.__sec = sec

    def __lt__(self, other):
        if self.__hour < other.__hour:
            return "t1 is smaller than t2"
        elif self.__hour == other.__hour:
            if self.__minute < other.__minute:
                return "m1 is smaller than m2"
            elif self.__minute == other.__minute:
                if self.__sec == other.__sec:
                    return "s1 is smaller than s2"
        else:
            return "t1 is greater than t2"


h1 = int(input("Enter the hour: "))
m1 = int(input("Enter the minute: "))
s1 = int(input("Enter the second: "))
h2 = int(input("Enter the number of hours to be added: "))
m2 = int(input("Enter the number of minutes to be added: "))
s2 = int(input("Enter the number of seconds to be added: "))
t1 = time(h1, m1, s1)
t2 = time(h2, m2, s2)
print(t1 < t2)
