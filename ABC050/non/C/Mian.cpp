#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
int main()
{
	int n, count;
	cin >> n;
	int a[n];

	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}

	sort(a, a+n);

	if (n % 2 == 1)
	{
		count = 0;
			for (int i = 1; i < n - 1; i += 2)
			{
				if (a[i] - a[i + 1] == 0)
				{
					count++;
					// cout << count << endl;
				}else{
					break;
				}
			}
	}else{
		count = 0;
			for (int i = 0; i < n - 1; i += 2)
			{
				if (a[i] - a[i + 1] == 0)
				{
					count++;
				}else{
					break;
				}
			}
	}

	if (count == n/2 && n%2 == 0)
	{
		cout << pow(2, n/2) << endl;
	}
	else if (count == (n - 1)/2 && n%2 == 1)
	{
		cout << pow(2, (n-1)/2) << endl;
	}
	else{
		cout << 0 << endl;
	}

	return 0;
}
