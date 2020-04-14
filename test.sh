#!/bin/sh
echo "正在安装必要库"
echo "------------------------------------------------------------------";
yum -y install make zlib zlib-devel gcc-c++ libtool  openssl openssl-devel
echo "------------------------------------------------------------------";
echo "------------------------------------------------------------------";
cd /usr/local/src/
wget http://downloads.sourceforge.net/project/pcre/pcre/8.35/pcre-8.35.tar.gz
tar zxvf pcre-8.35.tar.gz
cd pcre-8.35
./configure
make && make install
echo "------------------------------------------------------------------";
echo "请查看这个pcre的版本";
pcre-config --version
echo "正在安装Nginx"
echo "------------------------------------------------------------------";
cd /usr/local/src/
wget http://nginx.org/download/nginx-1.16.1.tar.gz
tar zxvf nginx-1.16.1.tar.gz
cd nginx-1.16.1
./configure --prefix=/usr/local/webserver/nginx --with-http_stub_status_module --with-http_ssl_module --with-pcre=/usr/local/src/pcre-8.35
make
make install
echo "------------------------------------------------------------------";
echo "请审查！"
usr/local/webserver/nginx/sbin/nginx -v
/usr/sbin/groupadd www
/usr/sbin/useradd -g www www
cat /usr/local/webserver/nginx/conf/nginx.conf
echo "/usr/local/webserver/nginx/sbin/nginx -t #检查配置文件是否正确"
echo "/usr/local/webserver/nginx/sbin/nginx #启动Nginx"
echo "/usr/local/webserver/nginx/sbin/nginx -s reload            # 重新载入配置文件"
echo "/usr/local/webserver/nginx/sbin/nginx -s reopen            # 重启 Nginx"
echo "/usr/local/webserver/nginx/sbin/nginx -s stop              # 停止 Nginx"

