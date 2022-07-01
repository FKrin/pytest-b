# @Author: fankang
# @Time: 2022/6/30 14:47
from Common.Request import Request
from Conf.Config import Config

class Ifcontract():

    def __init__(self):
        self.request = Request()

    def user_positions(self, headers=None, data=None):
        request_url = Config.TEST_WEB_FUTURES_HOST + "api/v1/ifcontract/userPositions"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_AUTHORIZATION,
            "X-BM-CLIENT": "WEB"
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, None, headers)
        return rsp
