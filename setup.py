from setuptools import setup

setup(
    name='Pasvortilo',
    version='0.1',
    py_modules=['pasvortilo'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pasvortilo=pasvortilo:cli
    ''',
)
