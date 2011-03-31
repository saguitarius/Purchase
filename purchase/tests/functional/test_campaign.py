from purchase.tests import *

class TestCampaignController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='campaign', action='index'))
        # Test response...
