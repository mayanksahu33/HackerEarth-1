#include <bits/stdc++.h>
#include <math.h>

using namespace std;



long long int read_int(){
	char r;
	bool start=false,neg=false;
	long long int ret=0;
	while(true){
		r=getchar();
		if((r-'0'<0 || r-'0'>9) && r!='-' && !start){
			continue;
		}
		if((r-'0'<0 || r-'0'>9) && r!='-' && start){
			break;
		}
		if(start)ret*=10;
		start=true;
		if(r=='-')neg=true;
		else ret+=r-'0';
	}
	if(!neg)
		return ret;
	else
		return -ret;
}

int main() {
	long long Q = read_int();
	for (long i=0;i<Q;i++){
		long long n = read_int();
		long long A[n+1];
		for (int l=0; l<n; l++){
			A[l] = read_int();
		}

		long max = -1;

		for (long j = 0; j<n; j++) {
			for (long k = j; k<n; k++ ) {
				if (abs(A[j] - A[k]) + abs(j -k) > max ) {
					max = abs(A[j] - A[k]) + abs(j -k);
				}
			}
		}
		cout << max << endl;
	}
}



