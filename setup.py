import distutils.extension
from setuptools import setup, find_packages

setup(
    name='uibcdf_tools',
    version='0.1',
    author='UIBCDF Lab',
    author_email='uibcdf@gmail.com',
    package_dir={'uibcdf_tools': 'uibcdf_tools'},
    packages=find_packages(),
    package_data={'uibcdf_tools': []},
    url='http://uibcdf.org',
    download_url ='https://github.com/uibcdf/UIBCDF_tools',
    license='MIT',
    description="doc to be written",
    long_description="long doc to be written",
)
