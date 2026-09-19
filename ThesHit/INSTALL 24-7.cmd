@echo off
setlocal
title ThesHit 24/7 installer

REM --- self-elevate to Administrator ---
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Ber om administrator-tilgang...
    powershell -Command "Start-Process -Verb RunAs -FilePath '%~f0'"
    exit /b
)

echo ============================================================
echo   ThesHit  -  setter opp 24/7 server
echo ============================================================
echo.

set VBS=D:\ThesHit\ThesHit\_scripts\serve_silent.vbs

echo [1/3] Aapner brannmur-port 8080...
netsh advfirewall firewall delete rule name="ThesHit 8080" >nul 2>&1
netsh advfirewall firewall add rule name="ThesHit 8080" dir=in action=allow protocol=TCP localport=8080
echo.

echo [2/3] Lager autostart (kjorer ved paalogging)...
schtasks /Create /TN "ThesHit-Course-Server" /TR "wscript.exe \"%VBS%\"" /SC ONLOGON /RL LIMITED /F
echo.

echo [3/3] Starter serveren naa...
start "" wscript.exe "%VBS%"
echo.

echo ============================================================
echo   FERDIG.
echo.
echo   Paa denne PC-en:  http://localhost:8080/_site/
echo.
echo   Neste: installer Tailscale (PC + mobil) for 4G-tilgang.
echo ============================================================
echo.
pause
