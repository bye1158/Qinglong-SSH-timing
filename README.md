#青龙面板定时SSH登录脚本，可serv00等定时登录保活并发送 Telegram 通知 （通用SSH登录）


1. **创建一个 Telegram Bot 并获取其 API Token。**
  - 获取用户或群组的Telegram Chat ID和Telegram Bot API Token。
2. **青龙面板**
  - 依赖管理--安装Linux依赖sshpass和jq
  - 脚本管理--创建serv00.sh、serv00.py、accounts.json文件并复制代码
  - 修改notify.py中TG_BOT_TOKEN与TG_USER_ID值。
  - 修改ACCOUNTS_JSON中的服务器信息

## 定时自动执行
  - 定时任务--创建任务--任务名（随意）--命令task serv00.sh--定时32 5 2 * *（北京时间每月第2日5时32分执行，可修改）


### 注意事项

- 确保在 `ACCOUNTS_JSON` 中正确配置每台服务器的信息，包括主机名、端口、用户名和密码。
- 定期检查青龙面板的执行结果和 Telegram 的通知，确保执行状态的进行。

