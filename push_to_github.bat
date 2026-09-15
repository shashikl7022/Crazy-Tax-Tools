@echo off
title Push Crazy Tax Tools to GitHub
color 0b
echo ======================================================================
echo           CRAZY TAX TOOLS - PUSH TO GITHUB WORKSTATION
echo ======================================================================
echo.
echo Target Repository: https://github.com/shashikl7022/Crazy-Tax-Tools
echo.

set PATH=C:\Users\MOJB-D085-Shashidhar\AppData\Local\Programs\Git\cmd;%PATH%
cd /d "C:\Users\MOJB-D085-Shashidhar\.gemini\antigravity\scratch\Crazy-Tax-Tools"

echo Checking Git status...
git status -s

echo.
echo [1/2] Pushing latest code to GitHub (main branch)...
echo If prompted, please click "Authorize" or sign in with your GitHub account in the browser.
echo.
git push -u origin main --force

if %errorlevel% equ 0 (
    echo.
    echo ======================================================================
    echo [SUCCESS] All files successfully uploaded to GitHub!
    echo.
    echo [2/2] Opening your live website:
    echo https://shashikl7022.github.io/Crazy-Tax-Tools/
    echo ======================================================================
    start https://shashikl7022.github.io/Crazy-Tax-Tools/
) else (
    echo.
    echo [ERROR] Push failed. If authentication failed, you can also upload files
    echo directly via your browser at:
    echo https://github.com/shashikl7022/Crazy-Tax-Tools/upload/main
    start https://github.com/shashikl7022/Crazy-Tax-Tools/upload/main
)

echo.
pause
