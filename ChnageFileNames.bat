@echo off
set /p SRC="Enter source folder path: "
set /p DST="Enter destination folder path: "
set /p DRY="Dry run? (y/n): "
set DRY_ARG=
if /I "%DRY%"=="y" set DRY_ARG=--dry-run

py "C:\Users\chase\Documents\roms\GC Games" --source "%SRC%" --dest "%DST%" --ext ".iso"  %DRY_ARG%
pause