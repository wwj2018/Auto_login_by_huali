2021-09-19

脚本在两个目录上
python_files包含脚本和其他安装包
Autohotkey同上

Python使用方法：
1、	下载安装google chrome（测试的版本为93.x.x.x）
2、	下载chromedriver（93.x.x.x）
3、	将chromedriver放到C:\Program Files\Google\Chrome\Application
4、	配置chromedriver和python环境变量
5、	编辑main.py中的论坛、校园网账号密码；编辑wifi.bat路径
![image](https://github.com/wwj2018/Auto_login_by_huali/blob/master/Pictures/1.png)
6、	测试运行


Autohotkey使用方法：
1、	下载安装Autohotkey
2、	编辑文件中的AHK.ahk文件
3、	修改AHK.ahk中对应的天翼客户端文件与wifi.bat路径
![image](https://github.com/wwj2018/Auto_login_by_huali/blob/master/Pictures/2.png
4、	修改鼠标位置到天翼客户端的“登陆”按钮位置（与屏幕分辨率相关，可能需要重启机子）
调整例子：MouseMove, 960, 580
960 → 860 向左调整（向右则反之）
580 → 480 向上调整（向下则反之）
5、	等待时间根据自身的电脑情况适当调整，最后测试运行
