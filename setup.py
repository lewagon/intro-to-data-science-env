from setuptools import setup

REQUIRED_PACKAGES = [
    # link between env and content repos for binder
    'nbgitpuller==0.9.0',
    # don't really know what this is for
    'jupyter-offlinenotebook==0.1.0',
    # dataframes
    'numpy==1.18.4',
    'pandas==1.1.2',
    # viz
    'matplotlib==3.2.1',
    'seaborn==0.10.1',
    # request
    'urllib3==1.24.3']

setup(
    name='WagonIntroToDS',
    version='1.0',
    install_requires=REQUIRED_PACKAGES,
    description='Wagon Intro to Data Science'
)
