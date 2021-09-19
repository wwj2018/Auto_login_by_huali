sleep 10000
MouseClick,	left
MouseClick,	left
Run D:\Program Files (x86)\Chinatelecom_JSPortal\ESurfingClient.exe
MouseMove, 960, 580
sleep 24000
MouseClick,	left
send #r
sleep 500
send netsh interface set interface "VMnet1" enabled
send, {enter}
sleep 2000
send #r
sleep 500
send netsh interface set interface "VMnet1" disabled
send, {enter}
send #r
sleep 500
send C:\Users\Administrator\Desktop\HotPoint\wifi.bat
send, {enter}
sleep 1000
send, {enter}

