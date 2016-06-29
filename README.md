# nameko-beanstalkd

Beanstalkd dependency for nameko services

## Installation
```
pip install nameko-beanstalkd
```

## Usage ##

```python
from nameko.rpc import rpc
from nameko_beanstalkd import Beanstalkd


class MyService(object):
    name = "my_service"

    beanstalkd = Beanstalkd('development')

    @rpc
    def hello(self, name):
        self.beanstalk.put('bob')
        job = self.beanstalk.reserve()
        return "Hello, {}!".format(job.body)

```
To specify beanstalkd connection string you will need a config
```yaml
AMQP_URI: 'amqp://guest:guest@localhost'
BEANSTALKD:
 development:
   HOST: '127.0.0.1'
   PORT: 11300
```
