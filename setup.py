from setuptools import setup

setup(
    name='nameko-beanstalkd',
    version='0.1.0',
    url='https://github.com/sohonet/nameko-beanstalkd/',
    py_modules=['nameko_beanstalkd'],
    install_requires=[
        "nameko>=2.0.0",
        "beanstalkc"
    ],
    description='Beanstalkd dependency for nameko services',
)
