#######################################
### file to analyse my cadence data ###
#######################################

datavector,time_between_rotation = [], []


with open("../inputdata/CadenceData.txt") as file:
    for line in file:
        datavector.append(line)

    ppm = int(datavector[0])
    datavector.pop(0)

dataset = list(map(int, datavector))

for i in range(len(dataset)):
    if int(dataset[i]) == 0:
        counter += 1
        print("test")
    elif dataset[i] == 1:
        time_between_rotation.append(20*counter+1)
        counter = 0
    print(time_between_rotation)
