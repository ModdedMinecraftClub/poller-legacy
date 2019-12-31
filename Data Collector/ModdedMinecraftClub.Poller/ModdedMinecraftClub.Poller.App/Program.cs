using System;
using System.Collections.Generic;
using ModdedMinecraftClub.Poller.Library;

namespace ModdedMinecraftClub.Poller.App
{
    class Program
    {
        static void Main(string[] args)
        {
            using var db = new DatabaseConnection();

            var tablesExist = db.DoesTableExist("server") && db.DoesTableExist("pings");

            if (tablesExist == false)
            {
                throw new DatabaseTablesNotFoundException();
            }
            
            var activeServers = db.GetEnabledServers();

            var poller = new Library.Poller(activeServers);

            var pings = poller.Poll();

            db.InsertPings(pings);
        }
    }
}