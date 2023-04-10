L = ["This is Asaf \n", "This is Chen \n", "This is Emily \n"]

with open("myfile.txt", "w") as file1:
	file1.write("Hello \n")
	file1.writelines(L)

#with open("myfile.txt", 'a') as file1:
	#file1.write("Today")


with open("myfile.txt", "r+") as file1:
	print(file1.read())
