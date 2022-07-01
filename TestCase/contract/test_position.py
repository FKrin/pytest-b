# @Author: fankang
# @Time: 2022/6/25 17:33
import allure
import pytest

from Logic.Contract import Position


@allure.feature('Contract')
class TestPosition:

    @allure.story('Position')
    def test_get_position(self, account):
        """
            用例描述：获取用户合约持仓
        """
        with allure.step("1.获取用户持仓"):
            if account is True:
                position = Position.Position()
                position.verify_get_position()


