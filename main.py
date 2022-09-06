from os import system
from sys import platform
import pkg_resources
from subprocess import call

def clear():
	if platform == "linux" or platform == "linux2" or platform == "unix":
		system("clear")
	elif platform == "win32":
		system("cls")
	else:
		system("clear")

clear()
print("Обновление всех pip библиотек")
system("pip3 install --upgrade pip")
if platform == "linux" or platform == "linux2" or platform == "unix":
	system("for i in $(pip list -o | awk 'NR > 2 {print $1}'); do pip install -U $i; done")
elif platform == "win32":
	packages = [dist.project_name for dist in pkg_resources.working_set]
	call("pip install --upgrade " + ' '.join(packages), shell=True)
else:
	print("Неподдерживаемая система!")
	exit()

clear()
print("Обновление модулей прошло успешно!")
print("\nНажмите Enter чтобы закрыть")
input()
