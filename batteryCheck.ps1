Write-Host "Battery config to default html viewer"
$dirName = 'batteryReports'
$fullName = './' + $dirName + '/battery-report-' + $(get-date -f yyyy-MM-dd) + '.html'
mkdir $dirName
powercfg /batteryreport /output $fullName
invoke-item $fullName
Read-Host -Prompt "Press Enter to exit"
