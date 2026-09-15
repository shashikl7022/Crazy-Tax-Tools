@echo off
title Push Crazy Tax Tools to GitHub
echo ========================================================
echo Pushing Crazy Tax Tools to https://github.com/shashikl7022/Crazy-Tax-Tools
echo ========================================================
echo.

set PATH=C:\Users\MOJB-D085-Shashidhar\AppData\Local\Programs\Git\cmd;%PATH%
cd /d "C:\Users\MOJB-D085-Shashidhar\.gemini\antigravity\scratch\Crazy-Tax-Tools"

echo Checking Git status...
git status

echo.
echo Pushing to GitHub (A browser window may open to verify your GitHub login)...
git push -u origin main --force

if %errorlevel% equ 0 (
    echo.
    echo ========================================================
    echo SUCCESS! All files have been pushed to your GitHub repo.
    echo.
    echo Opening GitHub Pages Settings in your browser...
    echo In GitHub Pages Settings:
    echo 1. Set Branch to 'main' and folder to '/ (root)'
    echo 2. Click 'Save'
    echo 3. Your website will be live at:
    echo    https://shashikl7022.github.io/Crazy-Tax-Tools/
    echo ========================================================
    start https://github.com/shashikl7022/Crazy-Tax-Tools/settings/pages
) else (
    echo.
    echo An error occurred during push. Please check your internet connection or GitHub credentials.
)

echo.
pause
