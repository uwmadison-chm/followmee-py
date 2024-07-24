import logging

from followmee_py.rest_adapter import RestAdapter

class FollowMeeApi:
    def __init__(
            self,
            api_key: str,
            hostname: str = "www.followmee.com",
            ssl_verify: bool = True,
            logger: logging.Logger = None,
    ):
        self._rest_adapter = RestAdapter(api_key, hostname, ssl_verify, logger)

    