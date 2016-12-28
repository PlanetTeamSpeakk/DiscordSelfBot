@echo off
chcp 65001
echo.
pushd %~dp0

net session >nul 2>&1
if NOT %errorLevel% == 0 (
    echo This script NEEDS to be run as administrator.
    echo Right click on it ^-^> Run as administrator
    echo.
    PAUSE
    GOTO end
)

::Checking git and updating
git.exe --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO gitmessage
title Updating Bot...
echo Updating Bot...
git stash
git pull

echo.
title Updating requirements...
echo Updating requirements...
::Attempts to start py launcher without relying on PATH
%SYSTEMROOT%\py.exe --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO attempt
%SYSTEMROOT%\py.exe -3 -m pip install --upgrade -r requirements.txt
GOTO updatebot

::Attempts to start py launcher by relying on PATH
:attempt
py.exe --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO lastattempt
py.exe -3 -m pip install --upgrade -r requirements.txt
GOTO updatebot

::As a last resort, attempts to start whatever Python there is
:lastattempt
python.exe --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO pythonmessage
python.exe -m pip install --upgrade -r requirements.txt
GOTO updatebot

:pythonmessage
echo Couldn't find a valid Python ^>3.5 installation. Python needs to be installed and available in the PATH environment variable.
PAUSE
GOTO end

:gitmessage
echo Git is either not installed or not in the PATH environment variable. Install it again and add it to PATH like shown in the picture
PAUSE

:updatebot
del bot.py
title Downloading Bot.py
start /WAIT bitsadmin.exe /transfer "Downloading bot.py" /priority HIGH https://raw.githubusercontent.com/PlanetTeamSpeakk/DiscordSelfBot/master/bot.py %~dp0\bot.py

:end
