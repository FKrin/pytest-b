# @Author: fankang
# @Time: 2022/6/25 17:33
import allure

from Logic.Contract import Position


class TestPosition:

    @allure.feature('Contract')
    @allure.story('Position')
    def test_get_position(self, account):
        """
            用例描述：获取用户合约持仓
        """
        if account is True:
            position = Position.Position()
            position.get_position()

