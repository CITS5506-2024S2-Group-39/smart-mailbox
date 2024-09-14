@ECHO OFF
SETLOCAL
PUSHD "%~DP0"

SET "GIT_BASH=%ProgramFiles%\Git\bin\bash.exe"

IF NOT EXIST "%GIT_BASH%" (
    ECHO [91m[ERROR][0m Bash executable not found at "%GIT_BASH%".
    ECHO [91m[ERROR][0m Please verify that Git for Windows is correctly installed.
    GOTO :EOF
)

"%GIT_BASH%" "%~n0.sh"
