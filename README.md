# Data_Engineering
ETL with Beautiful Soup and Pandas

Install MySQL 
https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04

```
$ sudo apt update
$ sudo apt install mysql-server
$ sudo mysql_secure_installation
```
How to start your MySQL session?

```$ mysql -h localhost -u root -p```

How to reset your password?
https://askubuntu.com/questions/1029177/error-1698-28000-access-denied-for-user-rootlocalhost-at-ubuntu-18-04

```
sudo mysql -u root
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'test';
```
