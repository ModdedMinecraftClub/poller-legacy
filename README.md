# poller
Minecraft server analytics collector.

Available at https://poller.moddedminecraft.club/.

// Table

## Data collector
Data collector is a C# app that collects data about the servers and inserts them into a MySQL database.

### Dependencies

#### If you want to build the data collector yourself:
- .NET Core SDK >=3.0 
- MySQL >=8.0

#### If you want to use pre-compiled binaries:
- .NET Core Runtime >=3.0 
- MySQL >=8.0

### Building the data collector
**This step can be skipped by downloading the latest pre-compiled binaries from [here](https://github.com/ModdedMinecraftClub/poller/releases).**

To build the data collector run the prepared `./Data Collector/buildLinux.sh` or `./Data Collector/buildWindows.ps1` (depending on your OS).

### Before running the data collector
1. Run the `prepare.sql` script to create the MySQL database and tables.
2. Populate the `server` table with servers you want the `poller` to poll. In the `enabled` column 0 means `false` and 1 `true`.

### Running the data collector
1. If you've built the data collector yourself go to `./Data Collector/Build`, otherwise go to the folder with the unzipped binaries that you've downloaded from the Releases page.
2. Run the `dotnet ModdedMinecraftClub.Poller.App.dll Server Port Username Password` command (replace each command line argument (Server, Port, Username, Password) with your own data).

## Web app
The web application presents the collected data to the user in a nice chart. It utilizes PHP for the back-end and JS/HTML/CSS for front-end.
