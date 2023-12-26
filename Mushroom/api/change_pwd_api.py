import requests
from Mushroom.global_vars import soft_id, error_codes


def changePwd(login_name, login_pwd_new, super_pwd):
    api_url = "http://api.1wxyun.com/?type=13"

    # 构造请求参数
    params = {
        "Softid": soft_id,
        "UserName": login_name,
        "NewUserPwd": login_pwd_new,
        "SupPwd": super_pwd,
    }

    try:
        # 发送登录请求
        response = requests.post(api_url, data=params, timeout=5)

        # 检查响应状态码
        if response.status_code == 200:
            if error_codes.get(response.text) is None:
                return True, ""
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
