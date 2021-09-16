import ssl, urllib.request
from django.conf import settings


url = "https://raw.githubusercontent.com/SekaiTeam/cloudlet_engine/main/version.txt"

def check_version():
	context = ssl._create_unverified_context()
	response = urllib.request.urlopen(url, context=context)
	version_in_git = response.read().decode("utf-8").replace("\n", "")

	with open(f"{settings.BASE_DIR}/version.txt", "r") as file:
		version = "".join(file.readlines()).replace("\n", "")

	return version == version_in_git