@ECHO OFF
CD /D %~dp0
python setup.py bdist_wheel
pause