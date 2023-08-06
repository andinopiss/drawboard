#include<stdio.h>
int mai(){
    int a[100],i=0,n;
    printf("enter the numbers of element in array");
    scanf("%d,&n");
    int b;
    printf("Enter number to find in array");
    scanf("%d",&b);
    for(i=0;i<n;i++){
        printf("Enter %d element of array",i+1);
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++){
        if(a[i]==b){
            printf("The number is present at place %d",i+1);
        }
    }
}