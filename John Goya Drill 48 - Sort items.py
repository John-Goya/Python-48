#insertion sort

def sortNumbers(numberlist):
    for index in range(1,len(numberlist)):

        currentvalue = numberlist[index]
        position = index

        while position>0 and numberlist[position-1]>currentvalue:
            numberlist[position]=numberlist[position-1]
            position = position-1

        numberlist[position]=currentvalue
numberlist = [64, 45, 2, 13, 1, 998]
sortNumbers(numberlist)
print(numberlist)


def sortNumbers(numberlist2):
    for index in range(1,len(numberlist2)):

        currentvalue = numberlist2[index]
        position = index

        while position>0 and numberlist2[position-1]>currentvalue:
            numberlist2[position]=numberlist2[position-1]
            position = position-1

        numberlist2[position]=currentvalue
numberlist2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]
sortNumbers(numberlist2)
print(numberlist2)
