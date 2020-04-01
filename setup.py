from setuptools import setup

setup(
    name = 'manuf',
    packages = ['manuf'],
    version = '2.0.1',
    description = 'Parser library for Wireshark\'s OUI database',
    author = 'Ke Tian',
    url = 'https://github.com/ktian-zingbox/manuf/',
    license = 'Apache License 2.0 or GPLv3',
    keywords = ['manuf', 'mac address', 'networking'],
    entry_points = {
        'console_scripts': [
            'manuf=manuf.manuf:main'
        ],
    },
    package_data = {
        'manuf': ['manuf']
    },
)

