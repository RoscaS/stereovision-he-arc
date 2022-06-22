from setuptools import find_packages
from setuptools import setup


setup(
    name='HeArcStereovision',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'bottle==0.12.18',
        'bottle-websocket==0.2.9',
        'Eel==0.12.2',
        'future==0.18.2',
        'gevent==1.4.0',
        'gevent-websocket==0.10.1',
        'greenlet==0.4.15',
        'numpy==1.22.0',
        'opencv-contrib-python==4.1.2.30',
        'progressbar==2.5',
        'whichcraft==0.6.1',
    ]
)
