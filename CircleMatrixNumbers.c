/*Pattern Printing for input n=4 
                            4 4 4 4 4 4 4  
                            4 3 3 3 3 3 4   
                            4 3 2 2 2 3 4   
                            4 3 2 1 2 3 4   
                            4 3 2 2 2 3 4   
                            4 3 3 3 3 3 4   
                            4 4 4 4 4 4 4  
constraint 1<=n<=1000
*/ 
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    int k=0,n,num,var;
    scanf("%d", &n);
    num=2*n-1;
    var=(num/2);
    var+=1;
    int arr[num][num];
    for(int i=0;i<num;i++)
    {
        for(int j=0;j<num;j++)   arr[i][j]=0;
    }
    while(k!=(num/2+1))
    {
        for(int i=k;i<num-k;i++)
        {
            arr[k][i]=var;
            arr[i][k]=var;
            arr[i][num-k-1]=var;
            arr[num-k-1][i]=var;
        }
        var-=1;
        k+=1;
    }
    for(int i=0;i<num;i++)
    {
        for(int j=0;j<num;j++)
        {
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}
