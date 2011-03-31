from purchase.tests import *

class TestAppController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='app', action='index'))
        # Test response...
