#!/usr/bin/node

length_arr = process.argv.length
let new_arr = []

if (process.argv.length <= 3)
{
	console.log(0);
}
for (let i = 0; i< length_arr; i++)
{
	if (i >= 2)
	{

		new_arr.push(process.argv[i])
	}
}
sorted_list = new_arr.sort()
console.log(sorted_list.slice(-2, -1)[0])

