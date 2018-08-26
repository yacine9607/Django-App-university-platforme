
#include<stdio.h>
#include<stdlib.h>
 
int main()
{
    char message[100], ch;
    int i,key;
    
    printf("Enter a message to encrypt: ");
    gets(message);
    printf("Enter key: ");
    scanf("%d", &key);
    
    for(i = 0; message[i] != '\0'; ++i){
        ch = message[i];
        
        if((ch >= 'a' && ch <= 'z')||(ch >= 'A' && ch <= 'Z')){
            ch = ch + key;
            
            if(ch > 'z'){
                ch = ch -26;
            }
            
            message[i] = ch;
     }else{
      printf("impossibe");
    }}
    
    printf("Encrypted message: %s", message);
  printf("\n");
  system("PAUSE");
    return 0;
}
