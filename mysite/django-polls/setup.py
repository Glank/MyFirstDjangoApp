import os
from setuptools import setup

cur_dir = os.path.dirname(__file__)
readme_file = os.path.join(cur_dir, "README.rst")
readme_file = open(readme_file, 'r')
README = readme_file.read()
readme_file.close()

# allow setup.py to be run from any path
abs_path = os.path.abspath(__file__)
parent_dir = os.path.join(abs_path, os.pardir)
os.chdir(os.path.normpath(parent_dir))

setup(
    name='django-polls',
    version='0.1',
    packages=['polls'],
    include_package_data=True,
    license='BSD License', 
    description='A simple Django app to conduct Web-based polls.',
    long_description=README,
    url='https://github.com/Glank/MyFirstDjangoApp',
    author='Ernest Kirstein',
    author_email='glank314@gmail.com',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', 
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
