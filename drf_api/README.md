# sqlaudit




## Build Setup
```
<!-- ```bash
# Clone project
git clone https://github.com/Rob-Bao/sqlaudit.git

# Install dependencies
# Install Redis
yum -y install redis


## install python 3.6.0
安装python3.6可能使用的依赖
# yum install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel

下载python3.6编译安装
到python官网下载https://www.python.org
下载最新版源码，使用make altinstall，如果使用make install，在系统中将会有两个不同版本的Python在/usr/bin/目录中。这将会导致很多问题，而且不好处理。
# wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz
# tar -xzvf Python-3.6.0.tgz -C  /tmp
# cd  /tmp/Python-3.6.0/
把Python3.6安装到 /usr/local 目录
# ./configure --prefix=/usr/local
# make
# make altinstall

python3.6程序的执行文件：/usr/local/bin/python3.6
python3.6应用程序目录：/usr/local/lib/python3.6
pip3的执行文件：/usr/local/bin/pip3.6
pyenv3的执行文件：/usr/local/bin/pyenv-3.6

# 安装模块
pip3 install celery
pip3 install celery-with-redis
pip3 install pymysql
pip3 install Django
pip3 install django-auth-ldap
pip3 install django-celery
pip3 install django-cors-headers
pip3 install django-filter
pip3 install djangorestframework
pip3 install djangorestframework-jwt
pip3 install python-ldap
pip3 install setuptools==40.8.0
pip3 install redis==2.10.6
 -->

# Run drf ,use 8900 port
python3 manage.py  makemigrations app
python3 manage.py  migrate
python3 manage.py  runserver 127.0.0.1:8890

# Run another program Celery
python3 manage.py celery worker --loglevel=info --beat

# 成功运行后，需要手动指定某个账号为超级用户，可以更改MySQL表进行操作，也可以命令授权。

```
