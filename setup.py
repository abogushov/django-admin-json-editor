import os
import re

from setuptools import setup


project_path = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(project_path, 'README.md'), 'r') as fout:
    README = fout.read()


version_file = os.path.join(project_path, 'django_admin_json_editor', 'version.py')

if os.path.exists(version_file):
    with open(version_file, 'r') as fout:
        version_text = fout.read()
        version = re.compile(r'.*__version__ = \'(.*?)\'', re.S).match(version_text).group(1)
else:
    version = 'dev'

# allow setup.py to be run from any path
os.chdir(project_path)

requirements = [
    'Django',
]

setup_requires = [
    'pytest-runner',
]

test_requirements = [
    'pytest',
    'pytest-django',
]

setup(
    name='django-admin-json-editor',
    version=version,
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
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=requirements,
    test_suite='tests',
    setup_requires=setup_requires,
    tests_require=test_requirements,
)
