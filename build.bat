@echo off
setlocal

set "XELATEX=xelatex"
if exist "C:\Users\zkbot\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe" (
  set "XELATEX=C:\Users\zkbot\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe"
)

if not exist "%~dp0output" mkdir "%~dp0output"

if "%1"=="" (
  call :build thesis_template
  if errorlevel 1 exit /b 1
  call :merge_cover
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
move /y "%~1.pdf" "%~dp0output\" >nul
del /q "%~1.aux" "%~1.log" 2>nul
exit /b 0

:merge_cover
echo Merging cover page ...
python "%~dp0merge_cover.py"
exit /b 0
