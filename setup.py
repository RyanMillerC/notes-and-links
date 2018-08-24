from setuptools import setup

setup(
    name='markdowncreator',
    version='0.1',
    packages=['markdowncreator'],
    install_requires=[
        'conlog==1.1.3',
        'docopt==0.6.2',
        'encase==1.1'
    ],
    entry_points={
        'console_scripts': [
            'markdowncreator = markdowncreator.__init__:main'
        ]
    }
)
