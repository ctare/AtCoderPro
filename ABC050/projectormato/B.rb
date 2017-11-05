n = gets.to_i
inputs = gets.chomp.split(" ").map(&:to_i)
m = gets.to_i
drinks = (1..m).map{gets.chomp.split(" ").map(&:to_i)}
m.times { |i|
	tmp = inputs[drinks[i][0]-1]
	inputs[drinks[i][0]-1] = drinks[i][1]
	puts inputs.reduce(:+)
	inputs[drinks[i][0]-1] = tmp
}
