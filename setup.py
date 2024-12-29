import setuptools

long_description = \
	"This library allows for easy manipulation of Super Mario Maker 2 save files."

setuptools.setup(
	name = "SMM2",
	version = "0.0.0",
	description = "Python library for manipulating Super Mario Maker 2 save files",
	long_description = long_description,
	author = "Mario Possamato",
	author_email = "mariopossamato@gmail.com",
	url = "https://github.com/pormonto/SMM2_Library",
	packages = [
		"SMM2"
	],
	install_requires = ["pycryptodome", "capstone", "keystone-engine"]
)
