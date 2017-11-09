n = gets.to_i
inputs = gets.chomp.split(" ").map(&:to_i).sort!
if n == 1 and inputs[0] == 0
	puts 1
	exit
end

if n == 2 and (inputs[0] !=1 or inputs[1] !=1)
	puts 0
	exit
end

if n%2 == 1 and inputs[0] != 0
	puts 0
	exit
end

(n % 2).step(n-1,2) { |i|
	# print "i=", i+1, "\n"
	# p inputs[i+1]
	if inputs[i] != inputs[i+1] or inputs[i] != i+1
		puts 0
		exit
	end
}

puts 2**(n/2) % (10**9+7)