from setuptools import setup

setup(
    name='xboomx',
    version='0.1dev',
    packages=['xboomx'],
scripts=['xboomx/bin/xboomx_sort.py',
         'xboomx/bin/xboomx_update.py',
         'xboomx/bin/xboomx'],
license='BSD',
long_description='wrapper for most common occurences in dmenu',
install_requires=[]
)
