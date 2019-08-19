1、django版本2.2.4

2、创建新的环境，安装requirements包

3、在相关目录下开发自己的接口












正式上线配置：
1、
migrate  -- 迁移数据库
python manage.py createcachetable cache_table   -- 配置缓存表


2、MORE\mine\views.py 48行 取消注释  -- 验证码发送