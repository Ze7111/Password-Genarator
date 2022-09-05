cd %~dp0
python3 %~dp0start.py
if %errorlevel% neq 0 cd %~dp0 python %~dp0app.py