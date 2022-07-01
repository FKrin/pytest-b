# @Author: fankang
# @Time: 2022/6/30 17:49
from Common.Request import Request
from Conf.Config import Config


class Operator():

    def __init__(self):
        self.request = Request()

    def user_info(self, headers=None, data=None):
        """
        代理商信息查询
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_WEB_HOST + "customer/user/info"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_AUTHORIZATION,
            "X-BM-CLIENT": "WEB"
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def userinvitecode_set(self, headers=None, data=None):
        """
        新增/修改用户邀请码
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_WEB_HOST + "customer/userinvitecode/set"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_AUTHORIZATION,
            "X-BM-CLIENT": "WEB"
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.post_request(request_url, body, headers)
        return rsp

    def agent_create(self, headers=None, data=None):
        """
        邀请代理商
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_WEB_HOST + "customer/agent/create"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_AUTHORIZATION,
            "X-BM-CLIENT": "WEB"
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.post_request(request_url, body, headers)
        return rsp

    def agent_confirm(self, headers=None, data=None):
        """
        代理商邀请确认
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_WEB_HOST + "customer/agent/confirm"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_AUTHORIZATION,
            "X-BM-CLIENT": "WEB"
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.post_request(request_url, body, headers)
        return rsp

    def agent_list(self, headers=None, data=None):
        """
        查询我的代理
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_WEB_HOST + "customer/agent/list"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_AUTHORIZATION,
            "X-BM-CLIENT": "WEB"
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def user_list(self, headers=None, data=None):
        """
        查询用户佣金
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_WEB_HOST + "customer/user/list"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_AUTHORIZATION,
            "X-BM-CLIENT": "WEB"
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def agent_modify(self, headers=None, data=None):
        """
        修改我的代理
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_WEB_HOST + "customer/agent/modify"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_AUTHORIZATION,
            "X-BM-CLIENT": "WEB"
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.post_request(request_url, body, headers)
        return rsp

    def sub_agent_list(self, headers=None, data=None):
        """
        子代理佣金查询
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_WEB_HOST + "customer/sub/agent/list"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_AUTHORIZATION,
            "X-BM-CLIENT": "WEB"
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def dashboard_user_rebate_list(self, headers=None, data=None):
        """
        仪表盘-直客佣金
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_WEB_HOST + "customer/dashboard/user/rebate/list"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_AUTHORIZATION,
            "X-BM-CLIENT": "WEB"
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def dashboard_agent_rebate_list(self, headers=None, data=None):
        """
        仪表盘-子代理佣金
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_WEB_HOST + "customer/dashboard/agent/rebate/list"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_AUTHORIZATION,
            "X-BM-CLIENT": "WEB"
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def dashboard_trade_count(self, headers=None, data=None):
        """
        仪表盘-交易次数
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_WEB_HOST + "customer/dashboard/trade/count"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_AUTHORIZATION,
            "X-BM-CLIENT": "WEB"
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def user_assetflow(self, headers=None, data=None):
        """
        返佣记录查询
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_WEB_HOST + "customer/user/assetflow"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_AUTHORIZATION,
            "X-BM-CLIENT": "WEB"
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp