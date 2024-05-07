def Selection_Sort(marks):
    for i in range(len(marks)):

        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(marks)):
            if marks[min_idx] > marks[j]:
                min_idx = j

        # Swap the minimum element with the first element
        marks[i], marks[min_idx] = marks[min_idx], marks[i]

    print("Marks of students after performing Selection Sort on the list : ")
    for i in range(len(marks)):
        print(marks[i])

# Function for displaying top five marks

def top_five_marks(a):
    print("Top five score are : ")
    cnt = len(a)

    if cnt < 5:
        start, stop = cnt - 1, -1  # stop set to -1 as we want to print the 0th element
    else:
        start, stop = cnt - 1, cnt - 6

    for i in range(start, stop, -1):
        print(" {0:.2f}".format(a[i]), end="\n")


            #or

            
#def top_five_marks(marks):
    #print("Top",len(marks),"Marks are : ")
    #print(*marks[::-1], sep="\n")

#<---------------------------------------------------------------------------------------->


marks=[]
n = int(input("Enter number of students whose marks are to be displayed : "))
print("Enter marks for",n,"students (Press ENTER after every students marks): ")
for i in range(0, n):
    ele = int(input())
    marks.append(ele)  # adding the element

print("The marks of",n,"students are : ")
print(marks)

flag=1;

Selection_Sort(marks)
top_five_marks(marks)
