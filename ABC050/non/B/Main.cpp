#include <iostream>
using namespace std;

int main()
{
	int n, m, p, x;
	int result = 0;
	cin >> n;
	int t[n];

	for (int i = 0; i < n; i++)
	{
		cin >> t[i];
		result += t[i];
	}

	cin >> m;

	for (int i = 0; i < m; i++)
	{
		cin >> p >> x;

		cout << result - (t[p-1] - x) << endl;
	}

	return 0;
}