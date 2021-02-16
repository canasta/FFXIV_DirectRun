# Running FFXIV without launcher
Powershell scripts for saving login infos and executing FFXIV client without launcher and login steps.

**DON'T USE THIS IN PUBLIC COMPUTER.**


# HOW TO USE(Executable or Python)
Save login information:
1. Execute `Release/directrun.exe`.
2. Click upper button "정보 저장" when FFXIV is running, then `command.directrun` file is created in same folder.(This file has **IMPORTANT INFORMATION** for login. **YOU MUST KEEP THIS FILE SAFE SO IT DOES NOT LEAK.**)

Execute FFXIV client:
1. Execute `Release/directrun.exe`.
2. Click lower button "클라이언트 실행"
3. FFXIV is executed.

# HOW TO USE(Powershell)
Save login information:
1. Execute `make_shortcut.ps1` when FFXIV is running.
2. `command.txt` file is created in same folder.(This file has **IMPORTANT INFORMATION** for login. **YOU MUST KEEP THIS FILE SAFE SO IT DOES NOT LEAK.**)

Execute FFXIV client:
1. Execute `directrun.ps1`.
2. FFXIV is executed.
