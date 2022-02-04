from setuptools import setup

with open("requirements.txt") as f:
    requirements = [c.strip() for c in f.readlines()]

setup(
    name='WagonIntroToDS',
    version='1.0',
    install_requires=requirements,
    description='Wagon Intro to Data Science'
)
