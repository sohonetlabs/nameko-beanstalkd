from setuptools import setup

setup(
    name='nameko-beanstalkd',
    version='0.1.0',
    url='https://github.com/sohonet/nameko-beanstalkd/',
    py_modules=['nameko_beanstalkd'],
    dependency_links=['git+https://git@github.com/sohonetlabs/nameko.git@master#egg=nameko-2.3.2'],
    install_requires=[
        "nameko==2.3.2",
        "beanstalkc"
    ],
    description='Beanstalkd dependency for nameko services',
)
