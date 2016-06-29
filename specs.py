import eventlet
eventlet.monkey_patch()  # noqa (code before rest of imports)

import unittest
import mock

from nameko.containers import ServiceContainer
from nameko.testing.services import entrypoint_hook, dummy

from nameko_beanstalkd import Beanstalkd


class ExampleService(object):
    name = "exampleservice"

    beanstalkd = Beanstalkd('test')

    @dummy
    def write(self, value):
        self.beanstalkd.put(value)

    @dummy
    def read(self):
        job = self.beanstalkd.reserve()
        return job.body


class MockJob(object):
    def __init__(self, value):
        self.body = value


class BeanstalkdDependencySpec(unittest.TestCase):
    @mock.patch('nameko_beanstalkd.beanstalkc')
    def it_should_connect_to_the_server_on_setup(self, bs):
        container = ServiceContainer(ExampleService, {})
        container.start()

        assert bs.Connection.called

    @mock.patch('nameko_beanstalkd.beanstalkc')
    def it_should_destroy_connection_on_close(self, bs):
        container = ServiceContainer(ExampleService, {})
        container.start()

        assert bs.Connection.called

        container.stop()

        assert bs.Connection.return_value.close.called

    @mock.patch('nameko_beanstalkd.beanstalkc')
    def it_should_destroy_connection_on_kill(self, bs):
        container = ServiceContainer(ExampleService, {})
        container.start()

        assert bs.Connection.called

        container.kill()

        assert bs.Connection.return_value.close.called

    @mock.patch('nameko_beanstalkd.beanstalkc')
    def it_should_allow_method_calls_to_beanstalkd(self, bs):
        container = ServiceContainer(ExampleService, {})
        container.start()

        with entrypoint_hook(container, "write") as write:
            write("foobar")

        assert bs.Connection.return_value.put.called
        assert bs.Connection.return_value.put.call_args[0][0] == 'foobar'

        bs.Connection.return_value.reserve.return_value = MockJob('foobar')

        with entrypoint_hook(container, "read") as read:
            assert read() == "foobar"
