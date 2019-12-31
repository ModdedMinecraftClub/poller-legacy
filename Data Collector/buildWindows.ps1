$ErrorActionPreference = "Stop"

Set-Location .\ModdedMinecraftClub.Poller
dotnet publish -c Release
Set-Location ..

function PrepareDir {
    param (
        [string]$dirName
    )
    
    if (Test-Path .\$dirName) {
        Set-Location .\$dirName
        
        Remove-Item * -Force -Recurse

        Set-Location ..
    } else {
        mkdir $dirName
    }
}

PrepareDir("Build")

[string]$source = ".\ModdedMinecraftClub.Poller\ModdedMinecraftClub.Poller.App\bin\Release\netcoreapp3.0\publish\*"

[string]$destination = ".\Build\"

Move-Item -Force $source -Destination $destination

Write-Output "`n`nDone."