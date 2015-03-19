#include <iostream>
using namespace std;

#define TOT 1000

struct primi_t{
int num[TOT];
int c;
};

int main(){
int s=5;
primi_t primi;
primi.num[0]=2;
primi.num[1]=3;
primi.c=2;
int k=3;
bool primo;
while (primi.c<TOT){
	k+=2;
primo=true;
for (int i=0;i<primi.c;i++)
		if(0==k%primi.num[i]){
		primo=false;
		break;
		}
if (primo){
primi.num[primi.c++]=k;	
s+=k;
}
}
cout<<s<<endl;
return 0;
}
