import sys
from os import path
import requests  # 导入requests库，用于发送HTTP请求

message = ""


def load_send():
    cur_path = path.abspath(path.dirname(__file__))
    if path.exists(cur_path + "/notify.py"):
        try:
            from notify import send
            return send
        except ImportError:
            return False
    else:
        return False


# 使用ipify API获取公网IP
def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org")
        if response.status_code == 200:
            return response.text  # 返回IP地址
        else:
            return "无法获取IP"
    except requests.RequestException:
        return "无法获取IP"


def main(login_results):
    global message
    public_ip = get_public_ip()  # 获取公网IP地址
    for result in login_results:
        # 假设输入格式是 username:port:panel:login_result
        try:
            username, port, panel, login_result = result.split(":")
            login_result = int(login_result)  # 将登录结果转换为整数
        except ValueError:
            message += f"输入格式错误: {result}\n"
            continue  # 跳过格式错误的数据

        # 根据登录结果构建消息内容
        if login_result == 1:
            message += f"用户：{username} 面板：{port} 端口：{panel} 登录成功 登录IP：{public_ip}\n"
        else:
            message += f"用户：{username} 面板：{port} 端口：{panel} 登录失败 登录IP：{public_ip}\n"

    send = load_send()
    if callable(send):
        send("serv00&ct8", message)
    else:
        print("\n加载通知服务失败")


if __name__ == "__main__":
    login_results = sys.argv[1:]
    main(login_results)
