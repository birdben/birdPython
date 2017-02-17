## 安装elasticsearch

因为Python2和Python3共存，所以这里使用pip3安装elasticsearch

```
$ pip3 install elasticsearch
```

## 使用crontab定时发送邮件

每天10点定时执行sendmail.py脚本，这里也是用python3来运行

```
01 10 * * * /usr/bin/python3 /data0/task/sendmail.py > /dev/null 2>&1
```