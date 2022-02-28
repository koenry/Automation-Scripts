[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Drawing") 
[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms") 
$ok = Get-date -Format "dddd"
$ok1 = Get-Date -Format "yyyy.MM.dd"
$ok2 = Get-Date -Format "yyyy-MM-dd"
$d1 = '2021-05-19'
$ts = New-TimeSpan -Start $d1 -End $ok2
$d2 = 14
$usr = 'user'
$vpn = 'vpn'
$site1 = ''
$site2 = ''
$site3 = ''
$site4 = ''
$site5 = ''
$site6 = ''
$site7 = ''
$site8 = ''
$site9 = ''

function login {

start($site1)
start-sleep 1
[System.Windows.Forms.SendKeys]::Sendwait($usr)
[System.Windows.Forms.SendKeys]::Sendwait("{TAB}")
Read-Host -NoNewLine 'Login and press any key...';
}

set-location ..\..\..\Desktop\      <# working directory set to Desktop. #>
<# Creates a folder of todays date and checks if its Monday-Friday to create the coresponding word documents and add a date to their names #>
if($ok -eq 'Monday') {
    $ok3 = New-Item -Name $ok1 -ItemType "directory"
    New-Item -Path $ok1 -Name "BCK_$ok2.docx"
    New-Item -Path $ok1 -Name "STO_$ok2.docx"
    login
    start($site2)
    start-sleep 0.5
    start($site8)
    start-sleep 0.5
    start($fsr)
    start-sleep 0.5
    start($site7)
    start-sleep 0.5
    start($site9)
}

elseif($ok -eq 'Tuesday') {
    $ok3 =  New-Item -Name $ok1 -ItemType "directory"
    New-Item -Path $ok1 -Name "BCK_$ok2.docx"
    New-Item -Path $ok1 -Name "BCH_$ok2.docx"
    login
    start($site2)
    start-sleep 0.5
    start($site3)
    start-sleep 0.5
    start($site9)
}
elseif($ok -eq 'Wednesday'){
    New-Item -Name $ok1 -ItemType "directory"
    New-Item -Path $ok1 -Name "BCK_$ok2.docx"
    login
    start($site2)
    start-sleep 0.5
    start($site9)
    }
    if($ts.Days -eq $d2) {
        New-Item -Path $ok1 -Name "CMR_$ok2.docx"
        start($site5)
        }
    elseif($ts.Days -eq $d2 * 2) {
        New-Item -Path $ok1 -Name "CMR_$ok2.docx"
        start($site5)
        }
    elseif($ts.Days -eq $d2 * 3) {
        New-Item -Path $ok1 -Name "CMR_$ok2.docx"
        start($site5)
        }
    elseif($ts.Days -eq $d2 * 4) {
        New-Item -Path $ok1 -Name "CMR_$ok2.docx" 
        start($site5)
        }       
            
elseif($ok -eq 'Thursday') {
    $ok3 = New-Item -Name $ok1 -ItemType "directory"
    New-Item -Path $ok1 -Name "BCK_$ok2.docx"
    login
    start($site2)
    start-sleep 0.5
    start($site4)
    start-sleep 0.5
    start($fsr)
    start-sleep 0.5
    start($site7)
    start-sleep 0.5
    start($site9)
}
elseif($ok -eq 'Friday') {
    $ok3 =  New-Item -Name $ok1 -ItemType "directory"
    New-Item -Path $ok1 -Name "BCK_$ok2.docx"
    login
    start($site2)
    start-sleep 0.5
    start($site9)
}


start-sleep 2

[System.Windows.Forms.SendKeys]::Sendwait("^{ESC}")
[System.Windows.Forms.SendKeys]::Sendwait($vpn)
start-sleep 0.5
[System.Windows.Forms.SendKeys]::Sendwait("{ENTER}")
start-sleep 1
[System.Windows.Forms.SendKeys]::Sendwait("{TAB}")
start-sleep 0.1
[System.Windows.Forms.SendKeys]::Sendwait("{ENTER}")
start-sleep 0.1
[System.Windows.Forms.SendKeys]::Sendwait("{TAB}")
start-sleep 0.1
[System.Windows.Forms.SendKeys]::Sendwait("{ENTER}")
start-sleep 0.1

<#  We connect to vpn from start menu > vpn > connect, using tab and enter to navigate withouth a mouse. I dont like leaving passwords in plain text so thats why we arent using 'rasdial' to login #>
start-sleep 4

[System.Windows.Forms.SendKeys]::Sendwait("{ENTER}")
start-sleep 1

if($ok -eq 'Monday') {
    Start-Process outlook
    start-sleep 1.2
    [System.Windows.Forms.SendKeys]::SendWait("^+6")
}

elseif($ok -eq 'Tuesday') {
    Start-Process outlook
    start-sleep 1.2
    [System.Windows.Forms.SendKeys]::SendWait("^+7")
}

elseif($ok -eq 'Wednesday') {
    Start-Process outlook
    start-sleep 1.2
    [System.Windows.Forms.SendKeys]::SendWait("^+9")
}

elseif($ok -eq 'Thursday') {
    Start-Process outlook
    start-sleep 1.2
    [System.Windows.Forms.SendKeys]::SendWait("^+8")
}

elseif($ok -eq 'Friday') {
    Start-Process outlook
    start-sleep 1.2
    [System.Windows.Forms.SendKeys]::SendWait("^+9")
}

<# checks what day it is and uses a macro created on outlook to start the coresponding email for that weekday #>