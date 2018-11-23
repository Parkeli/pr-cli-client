from setuptools import setup


setup(
	name="pr-client",
	version="1.0",
	py_modules=["app.cli"],
	install_requires=[
		"pyserial",
		"Click",
        "python-firebase",
        "inputs",
	],
	entry_points='''
		[console_scripts]
		pr-client=app.cli:cli
	'''
)