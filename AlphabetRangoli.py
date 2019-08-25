#You are given an integer,N                                                         ----c----
#Your task is to print an alphabet rangoli of size N.
#(Rangoli is a form of Indian folk art based on creation of patterns.)
#size 3 --c-b-c--
#       c-b-a-b-c
#       --c-b-c--
#       ----c----
import string
def print_rangoli(size):
    alphabets=string.ascii_lowercase
    alphabets=alphabets[0:size] #taking requried chars in alphabets
    for i in range(size-1,-1,-1):
        temp=''
        temp+='-'*(i*2)
        for k in range(size-i):
            temp=temp+alphabets[size-1-k]+'-'
        temp=temp[0:-1]
        dup_first_last=temp[0:-1]
        result=temp+dup_first_last[::-1]
        print(result)
    for i in range(1,size):
        temp=''
        temp+='-'*(i*2)
        for k in range(size-i):
            temp=temp+alphabets[size-1-k]+'-'
        temp=temp[0:-1]
        dup_first_half=temp[0:-1]
        result=temp+dup_first_half[::-1]
        print(result)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)