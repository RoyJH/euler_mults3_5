#Prints numbers, up to and including 1000, that are multiples of 3 or 5.
count = 0
while count <= 1000:
    if count % 3 == 0 and count % 5 == 0:
        print (str(count) + " Double Trouble")

    elif count % 3 == 0:
        print (count)

    elif count % 5 == 0:
        print (count)
    count += 1
