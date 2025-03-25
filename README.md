# phycalc[Unit]



# 开启gunicorn服务 

$cat /lib/systemd/system/gunicorn.service
```
# 描述
Description=gunicorn for django scientfic calc
# 在网络服务启动后再启动
After=network.target
 
[Service]
User=root
# 项目文件目录
WorkingDirectory=<dir>/phycalc/physol/
# gunicorn启动命令
ExecStart=/usr/bin/gunicorn  -w 2 physol.wsgi
# 错误重启
Restart=on-failure
 
[Install]
WantedBy=multi-user.target
```


# 在 /etc/nging/nginx.conf 中添加反向代理
```
        location / {
          proxy_pass http://127.0.0.1:8000;
          proxy_set_header Host $host;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
```

# 备用SELINUX设置，允许nginx访问网络

```
# setsebool -p httpd_can_network_connect 1
```



