# @Author: fankang
# @Time: 2022/6/25 17:33
import allure
import pytest

from Logic.Contract.Partner import Partner


@allure.feature('Partner')
class TestPartner:

    @allure.story('admin agent create')
    @pytest.mark.parametrize(
        "invitees_user_id, back_rate, business_id, language, agent_name",
        [
            ["21759451", 101, 111, 'English', 'back rate over limit'],
            ["21759451", 99, 111, 'English', 'common']
        ]
    )
    def test_agent_create(self, invitees_user_id, back_rate, business_id, language, agent_name):
        """
            用例描述：创建代理
        """
        with allure.step("1.校验创建代理时确认用户信息"):
            partner = Partner()
            partner.verify_user_list_info(invitees_user_id)

        with allure.step("2.校验创建代理是否成功"):
            partner = Partner()
            partner.verify_admin_agent_create(invitees_user_id, back_rate, business_id, language, agent_name)
