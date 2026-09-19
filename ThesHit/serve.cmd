@echo off
REM Launch the offline ThesHit course site (LAN-accessible for phone/tablet).
REM Local:  http://localhost:8080/_site/
REM Phone:  http://<this-PC-LAN-IP>:8080/_site/   (same Wi-Fi)
cd /d "%~dp0"
echo.
echo   ThesHit offline course
echo   This PC:  http://localhost:8080/_site/
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"IPv4"') do echo   Phone:   http://%%a:8080/_site/  (trim spaces)
echo   (Ctrl+C to stop)
echo.
python -m http.server 8080 --bind 0.0.0.0
