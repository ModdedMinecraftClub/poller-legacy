#!/bin/bash

set -e

cd ModdedMinecraftClub.Poller
dotnet publish -c Release
cd ..

if [ -d Build ]
then 
    cd Build
    rm -r *
    cd ..
else
    mkdir Build
fi

cp -r ModdedMinecraftClub.Poller/ModdedMinecraftClub.Poller.App/bin/Release/netcoreapp3.0/publish* Build/

printf "\n\nDone.\n"