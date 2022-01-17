def bilangan(values):
    output = list()
    output2 = list()
    for i in range(len(values)):
        for j in range(1,len(values)):
            jml = values[i] + values[j]
            if jml == 7:
                output.append(values[i])
    print(output)
    
    length = len(output)
    middle_index = length//2
    first_half = output[:middle_index]
    print(first_half)    
    second_half = output[middle_index:]
    print(second_half)
    output2.append(first_half)
    output2.append(second_half)    
    print(output2)    
                


nilai = list([3, 5, 2, -4, 8, 11])
bilangan(nilai)
