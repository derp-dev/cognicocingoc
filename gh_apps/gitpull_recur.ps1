Get-ChildItem -Directory | ForEach-Object {
    Set-Location $_.FullName
    Write-Host "Pulling changes in $($_.Name)..."
    git pull
}
