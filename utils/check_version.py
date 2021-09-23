import ssl, urllib.request
from django.conf import settings


version_url = "https://raw.githubusercontent.com/SekaiTeam/cloudlet_engine/main/version.txt"
changelog_url = "https://raw.githubusercontent.com/SekaiTeam/cloudlet_engine/main/changelog.txt"

def requests(request_url):
	context = ssl._create_unverified_context()
	response = urllib.request.urlopen(request_url, context=context)
	return response.read().decode("utf-8")

def get_version():

	version_in_git = requests(version_url)

	with open(f"{settings.BASE_DIR}/version.txt", "r") as file:
		version = "".join(file.readlines())

	return version == version_in_git

def get_changelog():
	changelog_in_git = requests(changelog_url)
	return changelog_in_git
