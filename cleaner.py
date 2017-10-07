import os, shutil, time, stat 

def skip(file, ignore_dic):
	# Function for skiping files and folders that should not be delted
	for ignore in ignore_dic:
		if ignore in file:
			return True

def remShut(*args):
	# Function to remove folder that script has no permission to remove 
    func, path, _ = args # onerror returns a tuple containing function, path and exception info
    os.chmod(path, stat.S_IWRITE)
    os.remove(path)

def rem_in_cwd(ignore_dic, time_treshold):
	# Remove all files and folders in current working directory
	for entry in os.scandir('.'):
		if time.time() - os.path.getmtime(entry.name) > time_treshold:
			if not skip(entry.name, ignore_dic):
				if entry.is_file():
				    print("Odstraňujem súbor " + os.getcwd() + "\\" + entry.name)
				    os.remove(entry.name)
				if entry.is_dir():
					print("Odstraňujem priečinok " + os.getcwd() + "\\" + entry.name + " a všetok jeho obsah")
					shutil.rmtree(entry.name, onerror = remShut)

if __name__ == '__main__':
	os.chdir(os.path.dirname('C:\\') + "Users\\" + "dev\\" + "Downloads")
	# print(os.getcwd())
	ignore_dic = ['nemazat']
	# Files modified before this treshold will be deleted (86400 = one day in seconds) 
	time_treshold = 0
	rem_in_cwd(ignore_dic, time_treshold)