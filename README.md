使用SQL server作为数据库，更改配置即可使用，初版未修改，已实现输入条码后自动查询，查询后自动清屏功能。仅提供源文件，请自行打包。（无源数据库，自行设计）
python打包命令：
Pyinstaller -F py_word.py 打包exe
 
Pyinstaller -F -w py_word.py 不带控制台的打包
 
Pyinstaller -F -w -i chengzi.ico py_word.py 打包指定exe图标打包
