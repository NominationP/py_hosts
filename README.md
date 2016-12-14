aut-update hosts

python 2.7

crontab :
    input:

        crontab -e
        00 12 * * * python /var/www/html/py_hosts/copy_hosts.py >> /var/www/html/py_hosts/corntab_host.log
        :wq






