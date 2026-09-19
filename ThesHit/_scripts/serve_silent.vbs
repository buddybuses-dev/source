' Starts the ThesHit course web server with no visible window.
' Used by the "ThesHit-Course-Server" scheduled task (runs at logon).
Dim sh
Set sh = CreateObject("WScript.Shell")
sh.CurrentDirectory = "D:\ThesHit\ThesHit"
sh.Run """C:\Users\Mizgin2\AppData\Local\Python\pythoncore-3.14-64\python.exe"" -m http.server 8080 --bind 0.0.0.0", 0, False
