import json
import uuid

from Crypto.Cipher import ARC4
import base64
import requests
from Mushroom.global_vars import soft_id, error_codes

encryption_key = "9H2J8I1E4R2F"
decryption_key = "4G7G3Q7D6D9E"


def login(login_name, login_pwd):
    api_url = "http://api2.1wxyun.com/?type=11"

    # 构造请求参数
    params = {
        "Softid": soft_id,
        "UserName": login_name,
        "UserPwd": login_pwd,
        "Version": "1.0",
        "Mac": get_mac_address()
    }

    try:
        # 发送登录请求
        response = requests.post(api_url, data=params)

        # 检查响应状态码
        if response.status_code == 200:
            if error_codes.get(response.text) is None:
                print("Login success")
                return True, response.text
            else:
                print(error_codes.get(response.text))
                return False, error_codes.get(response.text)
        else:
            # 处理请求失败的情况
            print(f"Request failed with status code {response.status_code}")
            return False, "网络异常"
    except Exception as e:
        print("系统异常", e)
        return False, "网络异常"


def unbind(login_name, login_pwd):
    api_url = "http://api.1wxyun.com/?type=14"

    # 构造请求参数
    params = {
        "Softid": soft_id,
        "UserName": login_name,
        "UserPwd": login_pwd,
        "Type": "1",
        "Mac": get_mac_address()
    }

    try:
        # 发送登录请求
        response = requests.post(api_url, data=params, timeout=5)

        # 检查响应状态码
        if response.status_code == 200:
            if error_codes.get(response.text) is None:
                return True, response.text
            else:
                return False, error_codes.get(response.text)
        else:
            # 处理请求失败的情况
            print(f"Request failed with status code {response.status_code}")
            return False, "网络异常"
    except Exception as e:
        print("系统异常", e)
        return False, "网络异常"


def getNotice():
    try:
        # 发送登录请求
        response = requests.post("http://api2.1wxyun.com/?type=1", data={"Softid": soft_id})

        # 检查响应状态码
        if response.status_code == 200:
            if error_codes.get(response.text) is None:
                return response.text
            else:
                return ""
        else:
            # 处理请求失败的情况
            print(f"Request failed with status code {response.status_code}")
            return ""
    except Exception as e:
        print("系统异常", e)
        return ""


def getVersion():
    # 发送登录请求
    response = requests.post("http://api2.1wxyun.com/?type=3", data={"Softid": soft_id})
    # 检查响应状态码
    if response.status_code == 200:
        return response.text
    else:
        # 处理请求失败的情况
        print(f"Request failed with status code {response.status_code}")
        return None


def get_mac_address():
    mac = ''.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2 * 6, 2)][::-1])
    return mac


def rc4_encrypt(plaintext):
    cipher = ARC4.new(encryption_key.encode('utf-8'))
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    return base64.b64encode(ciphertext).decode('utf-8')


def rc4_decrypt(ciphertext):
    cipher = ARC4.new(decryption_key.encode('utf-8'))
    decrypted_text = cipher.decrypt(base64.b64decode(ciphertext)).decode('utf-8')
    return decrypted_text
