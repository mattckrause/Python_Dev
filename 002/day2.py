#create an array
array = [1,2,3,4]

#Loop through each item and print it
arraylength = len(array)
i = 0
while i < arraylength:
    output = array[i]
    #to add the output variable to a string, we have to put in in the str() function
    print("test " + str(output))
    i = i+1
