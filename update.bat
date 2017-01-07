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

echo.
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
echo https://twentysix26.github.io/Red-Docs/red_install_windows/#software
PAUSE
GOTO end

:gitmessage
echo Git is either not installed or not in the PATH environment variable. Install it again and add it to PATH like shown in the picture
echo https://twentysix26.github.io/Red-Docs/red_install_windows/#software
PAUSE

:updatebot
if exist bot.py (
del bot.py
)
start /WAIT bitsadmin.exe /transfer "Downloading bot.py" /priority HIGH https://raw.githubusercontent.com/PlanetTeamSpeakk/DiscordSelfBot/master/bot.py %~dp0\bot.py
if not exist extensions (
mkdir extensions
)
if exist extensions\owner.py (
del extensions\owner.py
)
start /WAIT bitsadmin.exe /transfer "Downloading owner.py" /priority HIGH https://raw.githubusercontent.com/PlanetTeamSpeakk/DiscordSelfBot/master/extensions/owner.py %~dp0\extensions\owner.py
if exist extensions\copypastas.py (
del extensions\copypastas.py
)
start /WAIT bitsadmin.exe /transfer "Downloading copypastas.py" /priority HIGH https://raw.githubusercontent.com/PlanetTeamSpeakk/DiscordSelfBot/master/extensions/copypastas.py %~dp0\extensions\copypastas.py
if exist extensions\general.py (
del extensions\general.py
)
start /WAIT bitsadmin.exe /transfer "Downloading general.py" /priority HIGH https://raw.githubusercontent.com/PlanetTeamSpeakk/DiscordSelfBot/master/extensions/general.py %~dp0\extensions\general.py
if exist extensions\serverinfo.py (
del extensions\serverinfo.py
)
start /WAIT bitsadmin.exe /transfer "Downloading serverinfo.py" /priority HIGH https://raw.githubusercontent.com/PlanetTeamSpeakk/DiscordSelfBot/master/extensions/serverinfo.py %~dp0\extensions\serverinfo.py
if exist extensions\useful.py (
del extensions\useful.py
)
start /WAIT bitsadmin.exe /transfer "Downloading useful.py" /priority HIGH https://raw.githubusercontent.com/PlanetTeamSpeakk/DiscordSelfBot/master/extensions/useful.py %~dp0\extensions\useful.py

:end