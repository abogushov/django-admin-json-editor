import os
import re
from setuptools import setup


project_path = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(project_path, 'README.md'), 'r') as fout:
    README = fout.read()
with open(os.path.join(project_path, 'django_admin_json_editor', '__init__.py'), 'r') as fout:
    version_text = fout.read()

VERSION = re.compile(r'.*__version__ = \'(.*?)\'', re.S).match(version_text).group(1)

# allow setup.py to be run from any path
os.chdir(project_path)

setup(
    name='django-admin-json-editor',
    version=VERSION,
    packages=['django_admin_json_editor'],
    include_package_data=True,
    license='MIT License',
    description='A simple Django app to add JSON widget into Django Administration.',
    long_description=README,
    url='https://github.com/abogushov/django-admin-json-editor',
    author='Alexander Bogushov',
    author_email='abogushov@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=['Django'],
)
