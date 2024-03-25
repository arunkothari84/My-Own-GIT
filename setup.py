
#!/usr/bin/env python3

from setuptools import setup

setup (name = 'ugit',
    version = '1.0',
    packages = ['ugit'],
    entry_points = {
        'console_scripts' : [
            'ugit = ugit.cli:main'
        ]
    },
    options={
        'build_scripts': {
            'executable': 'python',
            'include_path': ['C:\\Python37\\Scripts']  # Adjust this path according to your Python installation
        }
    }
)