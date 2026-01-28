
setlocal EnableDelayedExpansion

for /f "usebackq tokens=* delims=" %%L in ("requirements.txt") do (
    set "line=%%L"
    if not "!line!"=="" if not "!line:~0,1!"=="#" (
        rez-pip --install --release !line! --python-version _3.12.10 -e --extra-index-url https://download.pytorch.org/whl/cu126
    )
)

endlocal
