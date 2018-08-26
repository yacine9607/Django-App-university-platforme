#include<stdio.h>
#include<string.h>
#include<stdlib.h>



int main(){
int a,b, a0,b0,p,q,r,s,cnouveay_r,nouveau_s,quotient;
 scanf("%d", &a);
 scanf("%d", &b);

# On sauvegarde les valeurs de a et b.
a0 = a;
b0 = b;
 
# Initialisations. On laisse invariant p*a0 + q*b0 = a et  r*a0 + s*b0 = b.
p = 1;
q = 0;
r = 0;
s = 1;

# La boucle principale:
while (b!=0){
    c = a%b;
    quotient = a%b;
    a = b;
    b = c;
    nouveau_r = p - quotient * r;
    nouveau_s = q - quotient * s;
    p = r;
    q = s;
    r = nouveau_r;
    s = nouveau_s;
}
# Affiche le résultat.
printf ("%d %d ",&a0,&b0);
}
