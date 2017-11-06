#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
int main()
{
	int n; // countはやめてみる
	cin >> n;
	int a[n];

	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}

	sort(a, a+n);

	for (int i = n % 2; i < n - 1; i += 2) // これさえあれば
	{
		if (a[i] - a[i + 1] != 0) // 合わなかったときだけ判定すればいい
		{
			cout << 0 << endl;
			exit(0);
		}
	}
	// 求めたい数は2の(n/2)乗
	// n = 2n' の時のn/2と n = 2n'+1 の時の(n-1/2)は同義なので省略
	long long result = 1;
	for (int i = 0; i < n/2; ++i)
	{
		result *= 2;
		result %= 1000000007;
	}
	cout << result << endl;
	return 0;
}
