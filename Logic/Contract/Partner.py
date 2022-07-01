# @Author: fankang
# @Time: 2022/6/25 17:44
import pytest

from Api.teams.futures.operator import Operator
from Common import Request
from Common.Verify import Verify


class Partner:
    def __init__(self):
        self.request = Request.Request()
        self.operator = Operator()
        self.verify = Verify()

    def admin_agent_create(self, invitees_user_id, back_rate, business_id, language, agent_name):
        """
        管理站-新增代理商
        :param invitees_user_id: 邀请成为代理商用户cid
        :param back_rate: 一级代理返佣比例
        :param business_id: 商务id
        :param language: 国家
        :param agent_name: 代理名称
        :return:
        """
        request_data = {
            "inviteesUserId": invitees_user_id,
            "backRate": str(back_rate),
            "businessId": business_id,
            "language": language,
            "agentName": agent_name
        }
        rsp = self.operator.agent_create(data=request_data)
        return rsp

    def verify_admin_agent_create(self, invitees_user_id, back_rate, business_id, language,
                                  agent_name):
        """
        校验新增代理商是否成功
        :param invitees_user_id: 邀请成为代理商用户cid
        :param back_rate: 一级代理返佣比例
        :param business_id: 商务id
        :param language: 国家
        :param agent_name: 代理名称
        :return:
        """
        act_rsp = self.admin_agent_create(invitees_user_id, back_rate, business_id, language, agent_name)
        del act_rsp['body']['requestId']

        self.verify.verify_return_code(act_rsp['code'], 200)

        # todo check request_body
        if back_rate > 100 or back_rate < 0:
            exp_rsp = {'msg': 'User does not exist', 'errno': 'InvalidInviteesUserId', 'code': 40015, 'success': False}
        else:
            exp_rsp = {'msg': 'User does not exist', 'errno': 'InvalidInviteesUserId', 'code': 40015, 'success': False}
        self.verify.verify_return_body(act_rsp['body'], exp_rsp)

    def admin_user_list_info(self, cid):
        """
        管理站-新增代理商前获取用户信息
        :param cid: 用户cid
        :return:
        """
        request_data = {
            "cid": cid
        }
        rsp = self.operator.user_list_info(data=request_data)
        return rsp

    def verify_user_list_info(self, cid):
        """
        校验获取用户信息接口
        :param cid: 用户cid
        :return:
        """
        act_rsp = self.admin_user_list_info(cid)

        # todo how to find user is valid ？
        if cid == 0:
            exp_rsp = {"code": 0, "msg": "Success", "data": [], "errorData": None, "success": True}
        else:
            exp_rsp = {"code": 0, "msg": "Success", "data": [{"accountInfo": {"cid": "21759451", "userId": 4223336,
                                                                              "mainId": 0,
                                                                              "loginName": "1partner2@tempmail.cn",
                                                                              "userType": 0, "userTypeId": None,
                                                                              "userTypeName": "", "remark": "",
                                                                              "bindGoogle": "F", "bindPhone": "F",
                                                                              "bindEmail": "T", "userStatus": 1,
                                                                              "userStatusEnabled": "T",
                                                                              "tradeStatusEnabled": "T",
                                                                              "depositFiatEnabled": "T",
                                                                              "withdrawFiatEnabled": "T",
                                                                              "depositVirtualEnabled": "T",
                                                                              "withdrawVirtualEnabled": "T",
                                                                              "contractTransferEnabled": "T",
                                                                              "fiatTransferEnabled": "T",
                                                                              "otcTransferEnabled": "T",
                                                                              "otcTradeEnabled": "T",
                                                                              "contractTradeEnabled": "T",
                                                                              "subscribeEarnEnabled": "T",
                                                                              "redemptionEarnEnabled": "T",
                                                                              "fundTransferEnabled": "T",
                                                                              "leverRiskEnabled": "T",
                                                                              "internalWithdrawEnabled": "T",
                                                                              "switchJson": {"nftTradeEnabled": "T",
                                                                                             "nftOnShelfEnabled": "T",
                                                                                             "nftDepositEnabled": "T",
                                                                                             "nftWithdrawEnabled": "T"},
                                                                              "phone": "", "areaCode": "",
                                                                              "email": "1partner2@tempmail.cn",
                                                                              "userIntroNo": "3kgFmt",
                                                                              "registerTime": 1655103187000},
                                                              "kycInfo": {"kycLevel": 0, "kycStatus": 0, "country": "",
                                                                          "identityBackImageId": "",
                                                                          "identityFrontImageId": "",
                                                                          "identityHandheldImageId": "", "realName": "",
                                                                          "identityType": 0, "identityNo": "", "sex": 0,
                                                                          "birthday": ""}, "roleInfo": {"roleList": []},
                                                              "levelInfo": {"level": 1, "internalLevel": 10,
                                                                            "levelLimit": "不允许提现", "kycStatus": "INIT",
                                                                            "fiatKycStatus": None, "levelDesc": None},
                                                              "logInfo": {"latestLoginTimestamp": 1656582791000,
                                                                          "latestLoginIp": "10.253.241.121",
                                                                          "latestLoginEquipment": "WEB"},
                                                              "introUserTotal": 0}], "errorData": None, "success": True}

        self.verify.verify_return_code(act_rsp['code'], 200)
        self.verify.verify_return_body(act_rsp['body'], exp_rsp, hard_mode=False)


if __name__ == '__main__':
    p = Partner()
