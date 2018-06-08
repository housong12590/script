FROM ubuntu:16.04


# 使用阿里云的Ubuntu镜像
RUN echo '\n\
deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse\n\
deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse\n\
deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse\n\
deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse\n\
deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse\n'\
> /etc/apt/sources.list

#COPY vhosts.conf /etc/nginx/conf.d/vhosts.conf

#COPY . /opt/crm

#WORKDIR /opt/crm

#RUN apt-get update \
#    && yes | apt-get install python

RUN apt-get update && yes | apt-get install nodejs

RUN node


#RUN npm install -g cnpm --registry=https://registry.npm.taobao.org \
#    && cnpm install \
#    && cnpm run build

#COPY ./dist /opt/crm/dist
#COPY docker-entrypoint.sh /opt/crm
#COPY text_script.py /opt/crm

#RUN rm /etc/nginx/conf.d/default.conf \
#  && cd /opt/crm \
#  && chmod +x docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]
