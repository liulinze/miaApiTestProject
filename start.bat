@echo 正在执行环境路径初始化...
@cd tools
@python envPathInsert.py
@cd ..
@echo 开始执行测试框架...
:执行框架测试
@python console.py
:执行完毕
@echo.
@echo 测试框架执行完毕，请按任意键退出！ & pause>nul
exit