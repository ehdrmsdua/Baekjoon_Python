N = int(input())

total_list = []
for i in range(0, N):
    class_list = input().split()
    class_list = [str(class_list[0]), int(class_list[1]), int(class_list[2]), int(class_list[3])]
    total_list.append(class_list)

total_list.sort(key=lambda x:(-x[3],-x[2],-x[1]))
print(total_list[0][0],total_list[-1][1],sep='\n')