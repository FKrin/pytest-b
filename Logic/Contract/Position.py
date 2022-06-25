# @Author: fankang
# @Time: 2022/6/25 17:44
from Common import Request
from Conf import Config


class Position:
    def __init__(self):
        self.request = Request.Request()
        self.config = Config

    def get_position(self):
        reuqest_url = "https://derivatives.bitmarttest.com/api/v1/ifcontract/userPositions"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": self.config.Config.VALUE_AUTHORIZATION,
            "X-BM-CLIENT": "WEB"
        }
        position = self.request.get_request(reuqest_url, None, headers)
        print(position)