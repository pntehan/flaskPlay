# flaskPlay
基于flask的视频，音频播放网站，前端代码均从youtube上寻找，后端逻辑是本人亲自编写
------
## 运行方法
git文件后在根目录打开终端，输入命令: python manage.py runserver，默认使用本机Ip，端口为80##
## 依赖包
主要包如下:
flask==1.0.2
flask-script==2.0.6
flask-sqlacodegen==1.1.6.1
flask-sqlalchemy==2.4.0
mysqlclient==1.4.2
## 数据文件
web目录下的static包含所需的全部数据文件，目前提供js,css,images的数据。
songs/目录下存放音频文件，存放要求:/songs/*/*.mp3，后端代码读取songs下所有文件夹作为专辑，文件夹内应只存放mp3文件。
movies/目录下存放视频文件，存放要求:/movies/*.mp3，后端代码读取movies下所有mp4文件
专辑与电影对应的图片存放于static/images中，名称与专辑名和电影名称一致
## MVC模式开发
本次网站是博主最近学习flask后自己开发，使用了MVC模式，在url的配置上使用了flask的Blueprint并且将端口映射和逻辑函数分离，
这使得每一个模块都简单易懂，方便后续的优化与修改
## 其他
本次操作比较粗糙，专注于MVC模式与html5的视音频播放，对于数据库部分并未细究，
数据库格式:
database==flaskplay
table==user(id int(5) primay key auto_increase not null, name varchar(255), pwd varchar(255), type int(1))
从数据库配置中可以看出，本来是想将用户分为普通用户和管理员两者，但尚未实现
## 后续优化
loading
