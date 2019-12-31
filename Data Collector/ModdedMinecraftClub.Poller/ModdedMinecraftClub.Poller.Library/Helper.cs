using System;

namespace ModdedMinecraftClub.Poller.Library
{
    public static class Helper
    {
        // myApp.exe Server Port Username Password
        public static string GetConnectionString()
        {
            var args = Environment.GetCommandLineArgs();
            
            var connString = $"Server={args[1]};Port={args[2]};Database=poller;Uid={args[3]};Pwd={args[4]};";

            return connString;
        }
    }
}