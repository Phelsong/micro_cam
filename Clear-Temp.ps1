
$dir = Get-ChildItem $PSScriptRoot\temp\
foreach ($item in $dir) {
    try {
        # Write-Host "deleting {$item}"
        Remove-Item $item
    }
    catch [System.IO.IOException] {
        Write-Host 'An error occurred:'
        Write-Host $_.ScriptStackTrace
    }
}
