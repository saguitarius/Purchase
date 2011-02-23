from purchase.tests import *

class TestCatalogController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='catalog', action='index'))
        # Test response...
