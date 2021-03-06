"""The application's Globals object"""

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

class Globals(object):
    """Globals acts as a container for objects available throughout the
    life of the application

    """

    def __init__(self, config):
        """One instance of Globals is created during application
        initialization and is available during requests via the
        'app_globals' variable

        """
        self.cache = CacheManager(**parse_cache_config_options(config))
        self.current_campaign_id = 0
        self.current_campaign_start_date = 0
        self.current_campaign_end_date = 0
        self.finished_active_campaign_id = 0
        self.finished_active_campaign_start_date = 0
        self.finished_active_campaign_end_date = 0
        self.user_id = 0
        self.user_group = 0
        self.user_view = 0
        self.current_section_id = 0