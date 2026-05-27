@echo off
REM opc-starter-kit Installer for Windows
REM Copies the skill to your project's .codebuddy/skills/ directory.
REM
REM Usage:
REM   install.bat                    current directory
REM   install.bat C:\my-project      specific project
REM   install.bat --global           global (~/.comate/skills/)

setlocal enabledelayedexpansion

set SKILL_NAME=opc-starter-kit
set SKILL_SRC=%~dp0

echo ==========================================
echo   opc-starter-kit Installer
echo   AI Startup Discipline Checkpoint
echo ==========================================
echo.

if /i "%~1"=="--help" goto :help
if /i "%~1"=="-h" goto :help
if /i "%~1"=="--global" goto :global
if /i "%~1"=="-g" goto :global

REM Check source
if not exist "%SKILL_SRC%SKILL.md" (
    echo [ERROR] SKILL.md not found.
    echo Run this script from the opc-starter-kit repository root.
    exit /b 1
)

REM Project install
set TARGET_DIR=%cd%
if not "%~1"=="" set TARGET_DIR=%~1

if not exist "%TARGET_DIR%" (
    echo [ERROR] '%TARGET_DIR%' does not exist.
    exit /b 1
)

set DEST=%TARGET_DIR%\.codebuddy\skills\%SKILL_NAME%
if exist "%DEST%" rmdir /s /q "%DEST%"
xcopy /e /i /q "%SKILL_SRC%" "%DEST%"
echo [OK] Installed to: %DEST%
echo.
echo Done! Open your AI tool in '%TARGET_DIR%' and type: opc
echo.
echo For other platforms (Cursor, Windsurf, etc.),
echo see references/tool-adaptations.md
goto :eof

:global
set DEST=%USERPROFILE%\.comate\skills\%SKILL_NAME%
if exist "%DEST%" rmdir /s /q "%DEST%"
xcopy /e /i /q "%SKILL_SRC%" "%DEST%"
echo [OK] Global install to: %DEST%
echo Done! Type 'opc' in any Comate project.
goto :eof

:help
echo Usage: install.bat [OPTIONS] [TARGET_DIR]
echo.
echo Options:
echo   --global, -g   Global install (%%USERPROFILE%%\.comate\skills\)
echo   --help, -h     Show this help
echo.
echo Examples:
echo   install.bat                   current directory
echo   install.bat C:\my-project     specific project
echo   install.bat --global          global install
echo.
echo For other platforms, see references/tool-adaptations.md
goto :eof
