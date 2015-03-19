#include <iostream>
using namespace std;

#define TOT 1000

struct primi_t{
int num[TOT];
int c;
};

bool primo (primi_t &p,int x){
	for (int i=0;i<p.c;i++)
		if(0==x%p.num[i]){
		return false;
		}
p.num[p.c++]=x;
return true;
}

int main(){
int s=5;
primi_t primi;
primi.num[0]=2;
primi.num[1]=3;
primi.c=2;
int k=3;
while (primi.c<TOT){
	k+=2;
	if(primo(primi,k))
		s+=k;
}
cout<<s<<endl;
return 0;
}
