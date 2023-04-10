file1 = open("my_file.txt", "w")
L = ["This is asaf \n", "This is chen \n", "This is emi"]
file1.writelines(L)
file1.close()