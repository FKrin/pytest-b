# @Author: fankang
# @Time: 2022/6/30 17:14
from Common.Request import Request
from Conf.Config import Config


class Operator():

    def __init__(self):
        self.request = Request()

    def user_set(self, headers=None, data=None):
        """
        合约新增运营
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/user/set"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.post_request(request_url, body, headers)
        return rsp

    def agent_create(self, headers=None, data=None):
        """
        管理站新增代理商
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "/v1/api/operator/agent/create"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.post_request(request_url, body, headers)
        return rsp

    def user_list_info(self, headers=None, data=None):
        """
        管理站新增代理商时确认账户信息
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "admin/user-list/info"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}
        headers.update(headers)
        body.update(**data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def agent_list(self, headers=None, data=None):
        """
        查询我的代理
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/agent/list"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def agent_all_list(self, headers=None, data=None):
        """
        查询所有代理
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/agent/all/list"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def agent_rebate_list(self, headers=None, data=None):
        """
        查询佣金
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/agent/rebate/list"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def agent_rebate_describe(self, headers=None, data=None):
        """
        查询佣金明细
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/agent/rebate/describe"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def user_list(self, headers=None, data=None):
        """
        查询用户信息
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/user/list"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def user_list_export(self, headers=None, data=None):
        """
        导出代理信息excel
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/user/list/export"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def agent_user_transfer(self, headers=None, data=None):
        """
        用户转移
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/agent/user/transfer"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.post_request(request_url, body, headers)
        return rsp

    def agent_rebate_self_modify(self, headers=None, data=None):
        """
        用户自返佣修改
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/agent/rebate/self/modify"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.post_request(request_url, body, headers)
        return rsp

    def agent_modify(self, headers=None, data=None):
        """
        修改我的代理
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/agent/modify"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.post_request(request_url, body, headers)
        return rsp

    def data_query(self, headers=None, data=None):
        """
        商务查询
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/data/query"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
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
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/dashboard/user/rebate/list"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
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
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/dashboard/agent/rebate/list"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def dashboard_agent_trade_count(self, headers=None, data=None):
        """
        仪表盘-交易次数
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/dashboard/agent/trade/count"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def order(self, headers=None, data=None):
        """
        当前委托
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/order"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def order_history(self, headers=None, data=None):
        """
        历史委托
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/order/history"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def trade_history(self, headers=None, data=None):
        """
        历史成交
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/trade/history"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def order_position(self, headers=None, data=None):
        """
        当前持仓
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/order/position"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def assetflow_list(self, headers=None, data=None):
        """
        划转记录
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/assetflow/list"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def executeflag_get(self, headers=None, data=None):
        """
        执行任务开关状态
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/executeflag/get"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp

    def executeflag_modify(self, headers=None, data=None):
        """
        执行任务开关状态修改
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/executeflag/modify"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL": "/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.post_request(request_url, body, headers)
        return rsp

    def user_assetflow(self, headers=None, data=None):
        """
        返佣记录查询
        :param headers:
        :param data:
        :return:
        """
        request_url = Config.TEST_TREAMS_FUTURES_HOST + "operator/user/assetflow"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": Config.TEST_TEAMS_AUTHORIZATION,
            "X-BM-CLIENT": "TEAMS",
            "X-BM-SECOND-LEVEL-URL":"/agent/my-future-agent",
            "X-BM-DEVICE": "66c9c7edf2913a0506f007b70c8299ef",
        }
        body = {}

        headers.update(headers)
        body.update(data)
        rsp = self.request.get_request(request_url, body, headers)
        return rsp
