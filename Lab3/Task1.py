count=0
def divide(arr):

    if len(arr)<=1:
        return arr
    else:
        mid=len(arr)//2
        arr1=divide(arr[:mid])
        arr2=divide(arr[mid:])

        return sol(arr1,arr2)

def sol(arr1,arr2):
    global count
    i,j=0,0
    final=[]
    while i<len(arr1) or j<len(arr2):
        
        if i>=len(arr1) and j<len(arr2):
            final.extend(arr2[j:])
            count+=1
            j+=1

        elif j>=len(arr2) and i<len(arr2):
            final.append(arr1[i])
            i+=1
        else:
            if arr1[i]<arr2[j]:
                final.append(arr[i])
                i+=1
            else:
                final.append(arr2[j])
                count+=1
                j+=1
    return final

input_file= open('Lab3/input1.txt', 'r')
output_file= open('Lab3/output1.txt', 'w')
#Lab3/input1.txt

n=int(input_file.readline())
arr=list(map(int,input_file.readline().strip().split()))

final=divide(arr)
print(final)
print(count)