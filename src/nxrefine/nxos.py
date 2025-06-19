import re
import platform

def is_wsl():
    """Return True if operating in Windows Subsystem for Linux (WSL)"""
    return "WSL" in platform.uname().release

def to_posix(path):
    """Converts absolute Windows path to absolute POSIX path."""
    path = path.replace('\\','/')
    match = re.match(r"^([A-Za-z]):/(.*)", path)
    if match:
        drive_letter = match.group(1).lower()
        rest = match.group(2)
        return f"/mnt/{drive_letter}/{rest}"
    
    raise ValueError("Invalid absolute path.")

def to_windows(path):
    """Converts absolute POSIX path to absolute Windows path."""
    match = re.match(r"^/mnt/([a-z])/([^:]*)", path)
    if match:
        drive_letter = match.group(1).upper()
        rest = match.group(2).replace('/','\\')
        return f"{drive_letter}:\\{rest}"
    
    raise ValueError("Invalid absolute path.")