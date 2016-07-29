from setuptools import setup

setup(
    name='nameko-beanstalkd',
    version='0.1.2',
    url='https://github.com/sohonet/nameko-beanstalkd/',
    py_modules=['nameko_beanstalkd'],
    install_requires=[
        "nameko>=2.3.1",
        "beanstalkc"
    ],
    description='Beanstalkd dependency for nameko services',
)
