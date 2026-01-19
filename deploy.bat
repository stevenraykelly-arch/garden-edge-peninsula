@echo off
echo ===================================================
echo   GARDEN EDGE - LOCAL BUILD & DEPLOY ASSISTANT
echo ===================================================
echo.

echo [1/3] Building site locally...
call npm run build
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Build failed. Please check the errors above.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo [2/3] Staging changes (including dist/)...
git add .
git add dist -f

echo.
echo [3/3] Committing and Pushing...
set /p commitMsg="Enter commit message: "
git commit -m "%commitMsg%"
git push origin main

echo.
echo ===================================================
echo   SUCCESS! Deployment triggered.
echo   Check https://localrankadvantage.shop in ~60s
echo ===================================================
pause
