'''
marks = [45,78,88,86,77]
avg = (sum(marks)/500)*100

marks2 = [75,98,88,86,77]
avg2 = (sum(marks2)/500)*100

print(avg, avg2)
'''
marks = [45,78,88,86,77]
marks2 = [75,98,88,86,77]
def percent(marks):
    return ((sum(marks)/(len(marks)*100))*100)

print(percent(marks), percent(marks2))