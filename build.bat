@echo off
setlocal

set "XELATEX=xelatex"
if exist "C:\Users\zkbot\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe" (
  set "XELATEX=C:\Users\zkbot\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe"
)

if "%1"=="" (
  call :build thesis_template
  if errorlevel 1 exit /b 1
  echo Build finished.
  exit /b 0
)

call :build %1
exit /b %errorlevel%

:build
echo Building %~1.tex ...
"%XELATEX%" -interaction=nonstopmode -halt-on-error "%~1.tex"
if errorlevel 1 exit /b 1
"%XELATEX%" -interaction=nonstopmode -halt-on-error "%~1.tex"
if errorlevel 1 exit /b 1
exit /b 0
