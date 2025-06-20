import re
import platform

def is_wsl():
    """Return True if operating in Windows Subsystem for Linux (WSL)"""
    return "WSL" in platform.uname().release

def to_posix(path):
    """Converts absolute Windows path to absolute POSIX path."""
    str_path = str(path).replace('\\','/')
    match = re.match(r"^([A-Za-z]):/(.*)", str_path)
    if match:
        drive_letter = match.group(1).lower()
        rest = match.group(2)
        formatted_path = f"/mnt/{drive_letter}/{rest}"
        return formatted_path
    
    return str_path

def to_windows(path):
    """Converts absolute POSIX path to absolute Windows path."""
    str_path = str(path).replace('\\','/')
    match = re.match(r"^/mnt/([a-z])/([^:]*)", str_path)
    if match:
        drive_letter = match.group(1).upper()
        rest = match.group(2).replace('/','\\')
        formatted_path = f"{drive_letter}:\\{rest}"
        return formatted_path
    
    return str_path