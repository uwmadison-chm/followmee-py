import logging
from typing import List

from followmee_py.models import DeviceInfo
from followmee_py.rest_adapter import RestAdapter

class FollowMeeApi:
    def __init__(
            self,
            api_key: str,
            username: str,
            hostname: str = "www.followmee.com",
            ssl_verify: bool = True,
            logger: logging.Logger = None,
    ):
        self._rest_adapter = RestAdapter(api_key, username, hostname, ssl_verify, logger)

    def get_all_devices(self) -> List[DeviceInfo]:
        ep_params = {"function": "devicelist"}
        result = self._rest_adapter.get(endpoint="info.aspx", ep_params=ep_params)
        return [DeviceInfo(**raw_data) for raw_data in result.data["Data"]]