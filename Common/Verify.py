# @Author: fankang
# @Time: 2022/7/1 10:44
import pytest
from pactverify.matchers import Matcher, Like, EachLike, Enum, Term, PactVerify

from Common.Log import MyLog as log


class Verify:

    def verify_return_code(self, act_rsp, exp_rsp=200):
        """
        校验 response code
        :param act_rsp: 实际接口返回 code
        :param exp_rsp: 期望接口返回 code
        :return:
        """
        if act_rsp != exp_rsp:
            log.error(f"return code error,except: {exp_rsp},actually: {act_rsp}")
            pytest.fail(f"return code error,except: {exp_rsp},actually: {act_rsp}")
        log.info(f"return code check success.")

    def verify_return_body(self, act_rsp, exp_rsp, hard_mode=True, mach_mode=0):
        """
        校验response body
        :param act_rsp: 实际接口返回 body
        :param exp_rsp: 期望接口返回 body
        :param hard_mode: hard_mode = True时,实际返回key必须严格等于预期key;hard_mode = False时,实际返回key包含预期key即可
        :param mach_mode: 校验模式：
                                 0.Matcher，值匹配；
                                 1.Like，类型匹配；
                                 2.EachLike，类型匹配（数组类型）；
                                 3.Term，正则匹配；
                                 4.Enum，枚举匹配
        :return:
        """
        mach_modes = ['Matcher', 'Like', 'EachLike', 'Term', 'Enum']
        exp_formate = eval(mach_modes[mach_mode])(exp_rsp)
        m_verify = PactVerify(exp_formate, hard_mode=hard_mode)

        m_verify.verify(act_rsp)
        verify_result = m_verify.verify_result

        if verify_result is not True:
            log.error(m_verify.verify_info)
        else:
            log.info("return body check success.")

        assert verify_result is True


if __name__ == '__main__':
    v = Verify()
    v.verify_return_body([{"name", "lisi"}, {"age": 14}], [{"name", "lisi"}, {"age": 14}])
