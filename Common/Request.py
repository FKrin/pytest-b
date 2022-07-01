# @Author: fankang
# @Time: 2022/6/25 16:27

"""
封装request

"""
import os
import random
import requests
import Common.Consts
from requests_toolbelt import MultipartEncoder

from Common.Log import MyLog as log


class Request:

    def get_request(self, url, data, header=None):
        """
        Get请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        try:
            if data is None:
                response = requests.get(url=url, headers=header, verify=False)
            else:
                response = requests.get(url=url, params=data, headers=header, verify=False)
            log.info(url)
            log.info(header)
            log.info(data)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            log.error(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            log.error(e)
            return ()

        handled_response = response_handle(response)
        return handled_response

    def post_request(self, url, data, header=None):
        """
        Post请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        try:
            if data is None:
                response = requests.post(url=url, headers=header, verify=False)
            else:
                response = requests.post(url=url, params=data, headers=header, verify=False)
            log.info(url)
            log.info(header)
            log.info(data)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            log.error(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            log.error(e)
            return ()

        handled_response = response_handle(response)
        return handled_response

    def post_request_multipart(self, url, data, header, file_parm, file, f_type):
        """
        提交Multipart/form-data 格式的Post请求
        :param url:
        :param data:
        :param header:
        :param file_parm:
        :param file:
        :param type:
        :return:
        """
        try:
            if data is None:
                response = requests.post(url=url, headers=header, verify=False)
            else:
                data[file_parm] = os.path.basename(file), open(file, 'rb'), f_type

                enc = MultipartEncoder(
                    fields=data,
                    boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
                )

                header['Content-Type'] = enc.content_type
                response = requests.post(url=url, params=data, headers=header, verify=False)
            log.info(url)
            log.info(header)
            log.info(data)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            log.error(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            log.error(e)
            return ()

        handled_response = response_handle(response)
        return handled_response

    def put_request(self, url, data, header):
        """
        Put请求
        :param url:
        :param data:
        :param header:
        :return:
        """
        try:
            if data is None:
                response = requests.put(url=url, headers=header, verify=False)
            else:
                response = requests.put(url=url, params=data, headers=header, verify=False)
            log.info(url)
            log.info(header)
            log.info(data)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            log.error(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            log.error(e)
            return ()

        handled_response = response_handle(response)
        return handled_response

def response_handle(response):
    time_consuming = response.elapsed.microseconds / 1000

    Common.Consts.STRESS_LIST.append(time_consuming)

    response_dicts = dict()
    response_dicts['code'] = response.status_code
    try:
        response_dicts['body'] = response.json()
    except Exception as e:
        log.error(e)
        response_dicts['body'] = ''
    response_dicts['time_consuming'] = time_consuming

    log.info(response_dicts)
    return response_dicts
