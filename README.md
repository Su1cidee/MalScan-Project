# MalScan – Advanced Malware Analysis Tool

MalScan is a Python-based malware analysis system designed to combine the efficiency of local execution with the comprehensive detection capabilities of cloud-based scanning. It integrates directly into the Windows operating system, allowing users to scan files via the right-click context menu. The tool communicates with the VirusTotal API to perform multi-engine malware detection and automatically generates detailed reports summarizing results, detections.

---

## 1. Overview

Traditional antivirus software offers convenience and real-time protection but is often resource-intensive and limited to signature-based detection. Conversely, online platforms such as VirusTotal provide high detection accuracy but require manual file uploads.  
MalScan bridges this gap by offering a hybrid solution: a lightweight, context-menu-based malware scanner that leverages the VirusTotal API for cloud-assisted detection while maintaining the speed and simplicity of a native desktop application.

---

## 2. Key Features

- **Multi-Engine Detection:** Integrates with VirusTotal to verify files against multiple antivirus engines.  
- **Context Menu Integration:** Allows direct scanning of files through the Windows right-click interface.  
- **Automated Reporting:** Generates structured, plain-text reports containing detection ratios, flagged engines, and timestamps.  
- **Batch Processing:** Supports scanning of multiple files in sequence.  
- **Lightweight Design:** No heavy dependencies or background processes.  
- **Error Handling:** Includes mechanisms for handling invalid API keys, network issues, and quota limits.  
- **Installer and Uninstaller Modules:** Provides seamless integration and complete uninstallation without residual data.  

---

## 3. System Architecture

MalScan follows a modular architecture to ensure maintainability and scalability.
| Module                          | Description                                                                                               |
|---------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Scan Module**                 | Handles file selection, hash computation, and interaction with the context menu.                          |
| **API Integration Module**      | Manages authentication, rate limiting, request queuing, and response parsing for VirusTotal API calls.    |
| **Report Generation Module**    | Produces structured text reports stored locally under the user directory.                                 |
| **Installer/Uninstaller Module**| Registers or removes MalScan from the Windows environment, including registry entries and shortcuts.      |

## 4. Technical Specifications

**Programming Language:** Python 3.10 or higher  
**Libraries:** `requests`, `hashlib`, `os`, `sys`, `pymsgbox`  
**Operating System:** Windows 10 or later  
**External Service:** VirusTotal API v2  
**Packaging Tool:** NSIS (Nullsoft Scriptable Install System)  

---

## 5. Installation

### Using the Installer
1. Download `MalScan_Installer.exe` from the project’s Releases section.  
2. Run the installer and follow the setup instructions.  
3. Once installation is complete, right-click any file and select:  
   - **Scan with MalScan (Compare with database)**, or  
   - **Upload to MalScan (New scan)**  

### Running from Source
```bash
git clone https://github.com/Su1cidee/MalScan.git
cd MalScan
pip install -r requirements.txt
python MalScan.py <filepath> <Scan|Upload>
```
When first executed, MalScan will prompt for a **VirusTotal Public API Key**, which is stored securely under:
```
C:\Users\<username>\vt_public_api
```

---

## 6. Testing Summary

Comprehensive unit testing was conducted to ensure the stability and correctness of each module.  
The following table summarizes the key test cases and outcomes.

| Test ID | Description | Objective | Expected Result | Status |
|----------|--------------|------------|----------------|--------|
| TC01     | Scan single file    | Verify functionality of Scan Module | File scanned and result retrieved | Pass |
| TC02     | Batch file scan     | Validate multiple file handling | All files scanned sequentially | Pass |
| TC03     | Upload file            | Verify upload to VirusTotal | Successful upload and response received | Pass |
| TC04     | API key authentication | Validate secure communication | Valid key accepted, invalid key rejected | Pass |
| TC05     | API quota exceeded     | Ensure stability under limits | Requests queued or retried; error logged | Pass |
| TC06     | Report generation | Confirm report creation | Report generated with detection summary | Pass |
| TC09     | Uninstallation | Validate clean removal | All files and registry entries removed | Pass |

---

## 7. Results

MalScan successfully integrates VirusTotal’s scanning capabilities into a standalone Windows application. The system performed reliably in both single-file and batch scanning scenarios. Reports were generated accurately, and error-handling mechanisms ensured resilience against API and network-related issues.

---

## 8. Future Enhancements

The following improvements are planned for subsequent versions of MalScan:

- Integration of AI/ML-based behavioral detection models.
- Advanced sandboxing for dynamic malware analysis.
- Cloud synchronization of reports and logs.
- Multi-language user interface support.
- Offline scanning mode with automatic synchronization.
- Real-time alerts for high-risk detections.
- Predictive risk scoring for unknown or obfuscated malware.

---

## 9. Author

**Shezan Merajuddin Shaikh**  
Malware Analysis and Reverse Engineering Enthusiast  
GitHub: [https://github.com/Su1cidee](https://github.com/Su1cidee)

---

MalScan demonstrates how an API-driven malware scanning system can combine transparency, performance, and usability — delivering an efficient and practical solution for modern malware analysis.

