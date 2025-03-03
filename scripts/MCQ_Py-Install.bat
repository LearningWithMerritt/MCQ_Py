@echo off
set "LWM_PATH=%USERPROFILE%\LWM"

if not exist "%LWM_PATH%" (
    mkdir "%LWM_PATH%"
)

cd "%LWM_PATH%"

:: Clone repo only if it doesn't exist
if not exist "%LWM_PATH%\MCQ_Py" (
    git clone https://github.com/LearningWithMerritt/MCQ_Py.git
) else (
    echo Repository already exists. Skipping clone.
)



set "TARGET_FILE=%LWM_PATH%\MCQ_Py\run-MCQ_Py.ps1"
set "SHORTCUT_PATH=%USERPROFILE%\Desktop\MCQ_Py.lnk"

if not exist "%SHORTCUT_PATH%" (
    powershell -command "$WScriptShell = New-Object -ComObject WScript.Shell; $Shortcut = $WScriptShell.CreateShortcut('%SHORTCUT_PATH%'); $Shortcut.TargetPath = '%TARGET_FILE%'; $Shortcut.Save()"
    echo Shortcut created at %SHORTCUT_PATH%
) else (
    echo Shortcut already exists. 
)


