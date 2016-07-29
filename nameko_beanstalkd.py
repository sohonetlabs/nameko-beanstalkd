import beanstalkc
from nameko.extensions import DependencyProvider

BEANSTALKD_KEY = 'BEANSTALKD'


class Beanstalkd(DependencyProvider):
    def __init__(self, key=None):
        self.key = key
        self._client = None

    def setup(self):
        """Set up config params for the connection."""
        config = self.container.config.get(BEANSTALKD_KEY, {})
        self.host = config.get(self.key, {}).get('HOST', '0.0.0.0')
        self.port = config.get(self.key, {}).get('PORT', 11300)

    def start(self):
        """Set up the connection to beanstalkd."""
        self._client = self.client(
            host=self.host,
            port=self.port
        )

    def stop(self):
        """Close the connection when services stop."""
        self._client.close()
        self._client = None

    def kill(self):
        """Close the connection when services are killed."""
        self._client.close()
        self._client = None

    def get_dependency(self, worker_ctx):
        """Return the client."""
        return self._client

    def client(self, host, port):
        return beanstalkc.Connection(
            host=host,
            port=int(port)
        )
