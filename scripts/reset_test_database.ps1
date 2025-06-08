# Resets the test database by replacing it with a predefined version
Remove-Item -Path "$PSScriptRoot\..\database\db.sqlite"
Write-Host "Removed db.sqlite from \database . "
Copy-Item -Path "$PSScriptRoot\..\test_databases_read_only\db.sqlite" -Destination "$PSScriptRoot\..\database"
Write-Host "Copied db.sqlite from \test-databases_read_only to \database ."
Write-Host "Database reset successfully."
