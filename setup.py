import ez_setup
ez_setup.use_setuptools()

import os

# disables creation of .DS_Store files inside tarballs on Mac OS X
os.environ['COPY_EXTENDED_ATTRIBUTES_DISABLE'] = 'true'
os.environ['COPYFILE_DISABLE'] = 'true'

def autosetup():
	from setuptools import setup, find_packages
	return setup(
		name			= "cairo-sketchpad",
		version			= "0.1",
		
		include_package_data = True,
		zip_safe		= False,
		packages		= find_packages(),
		
		entry_points	= {
			'console_scripts': [
				'cairo-sketchpad = cairo-sketchpad.app:main',
			]
		},
	)

if(__name__ == '__main__'):
	dist = autosetup()
