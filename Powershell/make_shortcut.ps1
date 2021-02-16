If (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))
{
	$arguments = "& '" + $myinvocation.mycommand.definition + "'"
	Start-Process powershell -Verb runAs -ArgumentList $arguments
	Break
}

$ffproc = Get-WmiObject win32_process -Filter {Name='ffxiv_dx11.exe'}

$command = $ffproc.CommandLine
if(!(Test-Path -Path ($PSScriptRoot + '/command.txt'))){
	New-Item ($PSScriptRoot + '/command.txt') -type file
}
Set-Content ($PSScriptRoot + '/command.txt') $command
