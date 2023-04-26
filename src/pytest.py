# -*- coding: utf-8 -*-
"""pytest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/birkenkrahe/ce31695940043f3e572fc085902a7d9e/pytest.ipynb

## Hello world program

Let's begin with some relentless digital globalism: It is said that
the 'hello world' program brings luck, so that's going to be our first
program:
"""

print("hello, world")

"""## A `datetime` program

Source: Barry (2016):50

-   Here's the code:
"""

from datetime import datetime

odds = [ 1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,
         33,35,37,39,41,43,45,47,49,51,53,55,57,59]

right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute.")

"""-   The first line imports a pre-existing functionality from Python's
    *standard library*, which contains a large stock of pre-built and high
    quality (i.e. safe and fast) reusable code so that you won't have to
    write it yourself.

-   Specifically, we request the submodule `datetime` from the `datetime`
    module, which works out the current time.

## Reusable functions + Modules = Standard Library

Source: Barry (2016):52

Each library only has to be called once in a `*Python*` session.

### `os`: Interacting with the OS

The `os` module provides a platform-independent way to interact with the
operating system:

1.  The `getwcd` function in `os` returns your current working directory
2.  The `getenv` function in `os` returns the value of `$HOME`
3.  The `os.environ` function returns environment variables
4.  Calling the functions inside `print` passes them to the REPL and
    returns the output here:
"""

import os, sys
print(os.getcwd())
print(os.getenv('HOME'))
print(os.environ) 
print(sys.version)
print(sys.platform)

"""Output on a Dell (Windows 10):

    : c:\Users\birkenkrahe\Downloads
    : C:\Users\birkenkrahe
    : environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\birkenkrahe\\AppData\\Roaming', 'CABAL_DIR': 'C:\\cabal', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'LCJVYZ1B3', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'DISPLAY': 'w32', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'EM_PARENT_PROCESS_ID': '17344', 'HOME': 'C:\\Users\\birkenkrahe', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\birkenkrahe', 'INSIDE_EMACS': '28.2,comint', 'LOCALAPPDATA': 'C:\\Users\\birkenkrahe\\AppData\\Local', 'LOGONSERVER': '\\\\LYON-DC01', 'NUMBER_OF_PROCESSORS': '16', 'ONEDRIVE': 'C:\\Users\\birkenkrahe\\OneDrive', 'ONEDRIVECONSUMER': 'C:\\Users\\birkenkrahe\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\Program Files (x86)\\Embarcadero\\Studio\\21.0\\bin;C:\\Users\\Public\\Documents\\Embarcadero\\Studio\\21.0\\Bpl;C:\\Program Files (x86)\\Embarcadero\\Studio\\21.0\\bin64;C:\\Users\\Public\\Documents\\Embarcadero\\Studio\\21.0\\Bpl\\Win64;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files\\PuTTY\\;C:\\Program Files\\dotnet\\;C:\\Program Files\\R\\R-4.2.2\\bin\\x64;c:\\Users\\birkenkrahe;C:\\Program Files\\Emacs\\emacs-28.2\\bin;c:\\Cygwin\\bin\\;C:\\Users\\birkenkrahe\\bin\\Strawberry\\c\\bin;C:\\Users\\birkenkrahe\\bin\\Strawberry\\perl\\site\\bin;C:\\Users\\birkenkrahe\\bin\\Strawberry\\perl\\bin;C:\\Program Files\\LLVM\\bin;C:\\Program Files\\Git\\cmd;C:\\Users\\birkenkrahe\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\;C:\\Users\\birkenkrahe\\AppData\\Local\\Programs\\Python\\Python311\\;C:\\Users\\birkenkrahe\\scoop\\shims;C:\\Users\\birkenkrahe\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Program Files (x86)\\mingw-w64\\i686-8.1.0-posix-dwarf-rt_v6-rev0\\mingw32\\bin;C:\\Program Files\\R\\R-4.1.2\\bin\\x64;C:\\Users\\birkenkrahe\\R\\win-library;C:\\Program Files (x86)\\Vim\\vim82\\;C:\\Users\\birkenkrahe\\scoop\\apps\\unzip\\6.00;C:\\Users\\birkenkrahe\\scoop\\apps\\7zip\\21.06;C:\\Users\\birkenkrahe\\scoop\\apps\\zip\\3.0;C:\\Program Files\\PuTTY;C:\\Program Files\\R1\\R-4.1.2\\bin;C:\\Program Files (x86)\\sqlite-tools-win32-x86-3360000;C:\\Program Files\\Emacs\\x86_64\\bin;C:\\Program Files (x86)\\mingw-w64\\i686-8.1.0-posix-dwarf-rt_v6-rev0\\mingw32\\bin;C:\\Program Files\\R\\R-4.2.2\\bin\\x64;C:\\ghcup\\bin;C:\\Users\\birkenkrahe\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Users\\birkenkrahe\\AppData\\Local\\Programs\\MiKTeX\\miktex\\bin\\x64\\;C:\\Users\\birkenkrahe\\AppData\\Local\\Programs\\MiKTeX\\miktex\\bin\\x64;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 141 Stepping 1, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '8d01', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\BIRKEN~1\\AppData\\Local\\Temp', 'TERM': 'emacs', 'TERMCAP': 'emacs:co#85:tc=unknown:', 'TMP': 'C:\\Users\\BIRKEN~1\\AppData\\Local\\Temp', 'UATDATA': 'C:\\Windows\\CCM\\UATData\\D9F8C395-CAB8-491d-B8AC-179A1FE1BE77', 'USERDNSDOMAIN': 'LYON.EDU', 'USERDOMAIN': 'LYONNET', 'USERDOMAIN_ROAMINGPROFILE': 'LYONNET', 'USERNAME': 'Birkenkrahe', 'USERPROFILE': 'C:\\Users\\birkenkrahe', 'VBOX_MSI_INSTALL_PATH': 'C:\\Program Files\\Oracle\\VirtualBox\\', 'WINDIR': 'C:\\Windows', 'ZES_ENABLE_SYSMAN': '1'})
    : 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)]
    : win32

Output on a Raspberry Pi (Linux):

    : /home/pi/Org
    : /home/pi
    : environ({'PWD': '/home/pi/Org', 'DISPLAY': ':0', 'TERM': 'dumb', 'TERMCAP': '', 'COLUMNS': '100', 'INSIDE_EMACS': '28.2,comint', 'PYTHONUNBUFFERED': '1', 'VTE_VERSION': '6203', 'VIRTUALENVWRAPPER_ENV_BIN_DIR': 'bin', 'VIRTUALENVWRAPPER_VIRTUALENV': '/home/pi/.local/bin/virtualenv', 'XDG_DATA_DIRS': '/usr/share/fkms:/usr/local/share:/usr/share/raspi-ui-overrides:/usr/share:/usr/share/gdm:/var/lib/menu-xdg:/usr/local/share:/usr/share:/var/lib/snapd/desktop', 'XDG_CONFIG_DIRS': '/etc/xdg', 'LC_ALL': 'en_US.UTF-8', 'XDG_VTNR': '1', 'VIRTUALENVWRAPPER_SCRIPT': '/home/pi/.local/bin/virtualenvwrapper.sh', 'GPG_AGENT_INFO': '/run/user/1000/gnupg/S.gpg-agent:0:1', '_LXSESSION_PID': '22383', 'VIRTUALENVWRAPPER_HOOK_DIR': '/home/pi/.virtualenvs', 'VIRTUALENVWRAPPER_PROJECT_FILENAME': '.project', 'CLUTTER_DRIVER': 'gles2', 'QT_ACCESSIBILITY': '1', 'SHELL': '/bin/bash', 'SSH_AUTH_SOCK': '/tmp/ssh-biXzzSVKDrWb/agent.22383', 'XDG_CONFIG_HOME': '/home/pi/.config', 'XAUTHORITY': '/home/pi/.Xauthority', 'LS_COLORS': 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:', 'XDG_CURRENT_DESKTOP': 'LXDE', 'LANG': 'en_US.UTF-8', 'XDG_RUNTIME_DIR': '/run/user/1000', 'XDG_MENU_PREFIX': 'lxde-pi-', 'PATH': '/home/pi/.local/bin:/home/pi/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games:/snap/bin:/snap/emacs/current/usr/bin', 'WINDOWPATH': '1', 'SAL_USE_VCLPLUGIN': 'gtk3', 'XDG_SESSION_ID': '1', 'XDG_SESSION_CLASS': 'user', '_': '/usr/bin/snap', 'LOGNAME': 'pi', 'QT_QPA_PLATFORMTHEME': 'qt5ct', 'COLORTERM': 'truecolor', 'DBUS_SESSION_BUS_ADDRESS': 'unix:path=/run/user/1000/bus', 'GTK_MODULES': 'gail:atk-bridge', 'COGL_DRIVER': 'gles2', 'HUSHLOGIN': 'FALSE', 'DESKTOP_SESSION': 'LXDE-pi', 'VIRTUALENVWRAPPER_PYTHON': '/usr/bin/python3', 'MOTD_SHOWN': 'pam', 'HOME': '/home/pi', 'SHLVL': '1', 'XDG_SESSION_TYPE': 'tty', 'SSH_AGENT_PID': '22434', 'XDG_SEAT': 'seat0', 'TEXTDOMAIN': 'Linux-PAM', 'WORKON_HOME': '/home/pi/.virtualenvs', 'USER': 'pi', 'LANGUAGE': 'en_US.UTF-8', 'MAIL': '/var/mail/pi', 'VIRTUALENVWRAPPER_WORKON_CD': '1', 'V3D_IGNORE_SCANOUT_USAGES': '1'})
    : 3.9.2 (default, Mar 12 2021, 04:06:34) 
    : [GCC 10.2.1 20210110]
    : linux

### `datetime`: accessing the computer clock's date

You can access the day, month and year values of the current date and
time separately by appending an *attribute* to the call:

1.  `import` the `datetime` library
2.  call the `datetime` module's `date.today()` function
3.  print the `day`, `month` and `year` attributes of the function
"""

import datetime
print(datetime.date.today())  
print(datetime.date.today().day)
print(datetime.date.today().month)  
print(datetime.date.today().year)

"""### `time`: accessing the computer clock's time

The standard library's `time` module allows us to access the current
time in variable format:

1.  `import` the `time` library
2.  Call the `strftime` function
3.  Specify the 24-hour format with the string `"%H:%M"`
4.  Save the time in a variable `t` and `print` it:
"""

import time
t = time.strftime("%H:%M hrs")
print(t)

"""To display the current day of the week and before/after noon:


"""

print(time.strftime("It's %A %p"))

"""### `html`: converting to and from HTML encoded text

You can encode all angle brackets in HTML code using the `escape`
function from the `html` module, or you can un-encode HTML using the
`unescape` function:

1.  `import` the `html` module
2.  encode angle brackets around HTML tags with `escape`
3.  un-encode HTML to the original using uni codes:
"""

import html
e = html.escape(
    "This HTML fragment contains a <script>script</script> tag.")
print(e) 
u = html.unescape("I &heart; Python's &lt;standard library&gt;.")
print(u) ## results in a Unicode Encode Error

"""Desired output:

    : This HTML fragment contains a &lt;script&gt;script&lt;/script&gt; tag.
    : I ♥ Python's <standard library>.

## References

-   Paul Barry (2016). Head First Python (2e). O'Reilly.
-   Jason M. Kinser (2022). Modeling and Simulation in Python. CRC Press.
-   Park and Miller (1988). Random number generators: Good ones are hard to
    find. CACM:1192-1201.
"""