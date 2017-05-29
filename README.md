#aut-update hosts


- 每天12点自动跟新HOST文件，科学上网

- python 3.5

- crontab :
    ```
    crontab -e
    00 12 * * * python /var/www/html/py_hosts/copy_hosts.py >> /var/www/html/py_hosts/corntab_host.log
    :wq
    ```
- tip :
    - change yourself dir path in copy_hosts.py  line:39
    - not forget to change root




