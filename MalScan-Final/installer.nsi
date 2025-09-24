;Start
 
  !define MUI_PRODUCT "MalScan Scanner"
  !define MUI_FILE "MalScan"
  !define MUI_VERSION "1.0"
  !define MUI_BRANDINGTEXT "MalScan Scanner Version 1.0"
  CRCCheck On

  !include "${NSISDIR}\Contrib\Modern UI\System.nsh"
 
;---------------------------------
;General
 
  Name "MalScan"
  OutFile "MalScan_Installer.exe"
  ShowInstDetails "show"
  ShowUninstDetails "show"
 
  !define MUI_ICON "MalScan.ico"
  !define MUI_UNICON "MalScan.ico"
 
;--------------------------------
;Folder selection page
 
  InstallDir "$PROGRAMFILES\${MUI_PRODUCT}"
 
;--------------------------------
;Modern UI Configuration
 
  !define MUI_WELCOMEPAGE  
  !define MUI_LICENSEPAGE
  !define MUI_DIRECTORYPAGE
  !define MUI_ABORTWARNING
  !define MUI_UNINSTALLER
  !define MUI_UNCONFIRMPAGE
  !define MUI_FINISHPAGE  
 
;--------------------------------
;Language
 
  !insertmacro MUI_LANGUAGE "English"

;--------------------------------
;Data

  LicenseData "LICENCE"
 
;-------------------------------- 
;Installer Sections     
Section "Install"
 
;Add files
  SetOutPath "$INSTDIR"
 
  File "${MUI_FILE}.exe"
  File "LICENCE"
 
;create start-menu items
  CreateDirectory "$SMPROGRAMS\${MUI_PRODUCT}"
  CreateShortCut "$SMPROGRAMS\${MUI_PRODUCT}\Uninstall.lnk" "$INSTDIR\Uninstall.exe" "" "$INSTDIR\Uninstall.exe" 0
  CreateShortCut "$SMPROGRAMS\${MUI_PRODUCT}\${MUI_PRODUCT}.lnk" "$INSTDIR\${MUI_FILE}.exe" "" "$INSTDIR\${MUI_FILE}.exe" 0
 
;write uninstall information to the registry
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${MUI_PRODUCT}" "DisplayName" "${MUI_PRODUCT}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${MUI_PRODUCT}" "UninstallString" "$INSTDIR\Uninstall.exe"
  
;add context menu
  WriteRegStr HKCR "*\shell\Scan with MalScan (Compare with database) [FAST]\command" ""  "C:\Program Files (x86)\MalScan Scanner\MalScan.exe %1 Scan"
  WriteRegStr HKCR "*\shell\Upload to MalScan (New scan) [SLOW]\command" ""  "C:\Program Files (x86)\MalScan Scanner\MalScan.exe %1 Upload"
 
  WriteUninstaller "$INSTDIR\Uninstall.exe"
 
SectionEnd
 
;--------------------------------    
;Uninstaller Section  
Section "Uninstall"
 
;Delete Files 
  RMDir /r "$INSTDIR\*.*"    
 
;Remove the installation directory
  RMDir "$INSTDIR"
 
;Delete Start Menu Shortcuts
  Delete "$DESKTOP\${MUI_PRODUCT}.lnk"
  Delete "$SMPROGRAMS\${MUI_PRODUCT}\*.*"
  RmDir  "$SMPROGRAMS\${MUI_PRODUCT}"
 
;Delete Uninstaller And Unistall Registry Entries
  DeleteRegKey HKEY_LOCAL_MACHINE "SOFTWARE\${MUI_PRODUCT}"
  DeleteRegKey HKEY_LOCAL_MACHINE "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\${MUI_PRODUCT}"  
  DeleteRegKey HKEY_CLASSES_ROOT "*\shell\Scan with MalScan (Compare with database [FAST])"
  DeleteRegKey HKEY_CLASSES_ROOT "*\shell\Upload to MalScan (New scan [SLOW])"
 
SectionEnd
 
;Function that calls a messagebox when installation finished correctly
Function .onInstSuccess
  MessageBox MB_OK "You have successfully installed MalScan-Scanner. Right click any program to scan it with MalScan."
FunctionEnd
 
 
Function un.onUninstSuccess
  MessageBox MB_OK "You have successfully uninstalled MalScan-Scanner."
FunctionEnd
 
 
;eof