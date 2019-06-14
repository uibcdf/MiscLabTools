import distutils.extension
from setuptools import setup, find_packages

setup(
    name='pytools_uibcdf',
    version='0.1',
    author='UIBCDF Lab',
    author_email='uibcdf@gmail.com',
    package_dir={'pytools_uibcdf': 'pytools_uibcdf'},
    packages=find_packages(),
    package_data={'pytools_uibcdf': []},
    url='http://uibcdf.org',
    download_url ='https://github.com/uibcdf/PyTools_uibcdf',
    license='MIT',
    description="doc to be written",
    long_description="long doc to be written",
)
