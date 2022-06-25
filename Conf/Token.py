# @Author: fankang
# @Time: 2022/6/25 16:27
from Common import Request


class Token:
    def __init__(self):
        self.request = Request.Request()

    def get_token(self, email):
        """
        获取登录token
        :param email: 用户邮箱
        :return: token信息
        """
        request_url = "https://api.bitmarttest.com/user-center/token/login/test"
        request_data = {
            "loginName": email
        }
        response = self.request.post_request(request_url, request_data)
        try:
            if response.get('body').get('data').get('accessToken') is not None:
                return True, response['body']['data']['accessToken']
        except Exception as e:
            return False, f"Get Token Fail"


if __name__ == '__main__':
        t = Token()
        token = t.get_token("jhoifzw-gv@tempmail.cn")
        print(token)