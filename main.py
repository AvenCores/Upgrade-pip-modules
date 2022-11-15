from pkg_resources import working_set
from sys import platform,argv
from subprocess import call
from os import system

def linuxbanner():
	print("""██╗   ██╗███╗   ██╗██╗██╗  ██╗
██║   ██║████╗  ██║██║╚██╗██╔╝
██║   ██║██╔██╗ ██║██║ ╚███╔╝ 
██║   ██║██║╚██╗██║██║ ██╔██╗ 
╚██████╔╝██║ ╚████║██║██╔╝ ██╗
 ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝                            
	""")

def windowsbanner():
	print("""██╗    ██╗██╗███╗   ██╗██████╗  ██████╗ ██╗    ██╗███████╗
██║    ██║██║████╗  ██║██╔══██╗██╔═══██╗██║    ██║██╔════╝
██║ █╗ ██║██║██╔██╗ ██║██║  ██║██║   ██║██║ █╗ ██║███████╗
██║███╗██║██║██║╚██╗██║██║  ██║██║   ██║██║███╗██║╚════██║
╚███╔███╔╝██║██║ ╚████║██████╔╝╚██████╔╝╚███╔███╔╝███████║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚══════╝                                                                                 
	""")

if '--rootupd' in argv:
	system('clear')
	system("sudo pip3 install --upgrade pip")
	system("for i in $(pip list -o | awk 'NR > 2 {print $1}'); do sudo pip install -U $i; done")
	system('clear')
	linuxbanner()
	print("Обновление модулей прошло успешно!")
	exit()

if '--nonrootupd' in argv:
	system('clear')
	system("pip3 install --upgrade pip")
	system("for i in $(pip list -o | awk 'NR > 2 {print $1}'); do pip install -U $i; done")
	system('clear')
	linuxbanner()
	print("Обновление модулей прошло успешно!")
	exit()

if '--winntupd' in argv:
	system('cls')
	packages = [dist.project_name for dist in working_set]
	call("pip install --upgrade " + ' '.join(packages), shell=True)
	system('clear')
	windowsbanner()
	print("Обновление модулей прошло успешно!")
	exit()

def rootupdate():
	system('clear')
	system("sudo pip3 install --upgrade pip")
	system("for i in $(pip list -o | awk 'NR > 2 {print $1}'); do sudo pip install -U $i; done")
	system('clear')
	linuxbanner()
	print("Обновление модулей прошло успешно!")
	exit()

def nonrootupdate():
	system('clear')
	system("pip3 install --upgrade pip")
	system("for i in $(pip list -o | awk 'NR > 2 {print $1}'); do pip install -U $i; done")
	system('clear')
	linuxbanner()
	print("Обновление модулей прошло успешно!")
	exit()

if platform == "linux" or platform == "linux2" or platform == "unix":
	system('clear')
	linuxbanner()
	menu = input("1 - Запустить обновление с ROOT правами\n2 - Запустить обновление от обычного Пользователя\n\n0 - Выход\n")
	if menu == "1": rootupdate()
	if menu == "2": nonrootupdate()
	if menu == "0": exit()

elif platform == "win32":
	system('cls')
	packages = [dist.project_name for dist in working_set]
	call("pip install --upgrade " + ' '.join(packages), shell=True)
	system('clear')
	windowsbanner()
	print("Обновление модулей прошло успешно!")
	exit()