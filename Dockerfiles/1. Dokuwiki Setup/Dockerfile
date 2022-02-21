FROM ubuntu
MAINTAINER koenry
WORKDIR /var/www
ENV DEBIAN_FRONTEND=noninteractive 
RUN apt-get update -y &&\
  apt-get upgrade -y &&\
  apt-get install wget -y &&\
  apt-get install vim -y &&\
  apt-get install unattended-upgrades -y &&\
  apt-get install apache2  libapache2-mod-php php-xml -y &&\
  wget https://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz &&\
  tar xvf dokuwiki-stable.tgz &&\
  mv dokuwiki-*/ dokuwiki &&\
  chown -R www-data:www-data dokuwiki 
WORKDIR /etc/apache2
RUN sed -i 's!DocumentRoot /var/www/html!DocumentRoot /var/www/dokuwiki!g' sites-enabled/000*.conf &&\ 
  sed -i '/www[/]/{n;n;s/.*/        AllowOverride All/}' apache2.conf &&\
  a2enmod rewrite && \
  dpkg-reconfigure --priority=low unattended-upgrades && \
  unattended-upgrade -d -v --dry-run
EXPOSE 80/tcp
