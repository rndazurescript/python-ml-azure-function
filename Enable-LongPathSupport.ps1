$registryPath = "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem"
$Name = "LongPathsEnabled"
$expectedValue = "1"

$currentValue=(Get-ItemProperty -Path $registryPath -Name $Name).$Name


if ($currentValue -ne $expectedValue){
  Write-Host "Enabling long path support"
  New-ItemProperty -Path $registryPath -Name $name -Value $expectedValue -PropertyType DWORD -Force | Out-Null
}
else{
  Write-Host "Long path support already activated"
}
