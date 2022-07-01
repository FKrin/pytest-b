# @Author: fankang
# @Time: 2022/6/25 17:44
import pytest

from Api.web.futures.ifcontract import Ifcontract
from Common import Request
from Common.Verify import Verify


class Position:
    def __init__(self):
        self.request = Request.Request()
        self.ifcontract = Ifcontract()
        self.verify = Verify()

    def verify_get_position(self):
        position = self.ifcontract.user_positions()
        exp_rsp = {'errno': 'OK', 'message': 'Success', 'data': {'positions': [
            {'position_id': 614485746, 'account_id': 2008000000000170, 'contract_id': 1, 'hold_vol': '1000',
             'freeze_vol': '0', 'close_vol': '0', 'hold_avg_price': '1000', 'open_avg_price': '1000',
             'close_avg_price': '0', 'oim': '200.6', 'im': '6.543075570974803916', 'mm': '5',
             'realised_profit': '-194.456924429025196084', 'earnings': '-194.456924429025196084',
             'hold_fee': '194.056924429025196084', 'open_type': 1, 'position_type': 1, 'status': 1, 'errno': 0,
             'created_at': '2022-06-22T08:25:30.711634Z', 'updated_at': '2022-06-30T08:00:00.608613Z',
             'close_able_vol': '1000', 'liquidate_price': '999.056924429025196084'}]}, 'success': True}
        self.verify.verify_return_code(position['code'], 200)
        self.verify.verify_return_body(position['body'], exp_rsp)


if __name__ == '__main__':
    p = Position()
    p.verify_get_position()
