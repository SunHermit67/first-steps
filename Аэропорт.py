def sorted_key(a):
    return a[0]

k = 210
containers = [0] * k
passengers_matrix = []
f = open('Аэропорт.txt')

for i in range(987):
    nums = str(f.readline())
    nums = nums.split()
    passengers_matrix.append([int(nums[0]),int(nums[1])])
    passengers_matrix = sorted(passengers_matrix,key=sorted_key)

counter = 0
temporary_last_order = []
last_order = 0

for time in range(1,1441):
    if containers.count(-1)>0:
        for x in range(containers.count(-1)):
            containers[containers.index(-1)] = 0
                
    if containers.count(time)>0:
        for x in range(containers.count(time)):
            containers[containers.index(time)] = -1
            
    for index in range(987):
        if passengers_matrix[index][0] == time and containers.count(0) > 0:
            counter += 1
            temporary_last_order.append(containers.index(0))
            containers[containers.index(0)] = passengers_matrix[index][1]
    if temporary_last_order != []:
        last_order = min(temporary_last_order)
        temporary_last_order = []
    else:
        temporary_last_order.append(last_order)
        
print(counter, temporary_last_order)
