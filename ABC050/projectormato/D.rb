# 桁DPの解説
# http://pekempey.hatenablog.com/entry/2015/12/09/000603
# http://torus711.hatenablog.com/entry/20150423/1429794075
# 桁DPの問題まとめ
# http://hamayanhamayan.hatenablog.jp/entry/2017/04/23/212728
# まとめ
# https://qiita.com/259_Momone/items/86e90d17e4efe3b22433
# ちょっと違う解法
# http://beet-aizu.hatenablog.com/entry/2017/01/12/164738

n = gets.to_i
a = n.to_s(2).split("").map(&:to_i) #dpのiにあたる配列
result = 0 #結果
mod = 10**9+7
dp = Array.new(a.size+1, Array.new(3,0))#dpするやつ
dp.unshift([1,0,0])
# p dp, a, a.size
for i in 1..a.size
	if a[i-1] == 0
		dp[i][2] = (3*dp[i-1][2] + dp[i-1][1]) % mod
		dp[i][1] = dp[i-1][1]
		dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % mod
	else
		dp[i][2] = ( (3*dp[i-1][2]) + (dp[i-1][1]*2) ) % mod
		dp[i][1] = (dp[i-1][1] + dp[i-1][0]) % mod
		dp[i][0] = dp[i-1][0]
	end
end
# p dp
result = dp[-1][0..2].reduce(:+) % mod
puts result
