import os	# To get the system path and handle files input and output.

def rename_files():
	# (1) get file names, from a folder/system path.
	file_list = os.listdir(r"/home/matrix/git_projects/Python101_Udacity/secret_message/prank/")
	print(file_list)

	# (2) for each file, rename filename, by removing any numerical part using translate function
#	print("Current Working Directory is: " + os.getcwd())
	saved_path = os.getcwd()
	os.chdir(r"/home/matrix/git_projects/Python101_Udacity/secret_message/prank/")

	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)

rename_files();
