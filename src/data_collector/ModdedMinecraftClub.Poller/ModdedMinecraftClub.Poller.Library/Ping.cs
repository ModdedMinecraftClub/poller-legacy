using System;

namespace ModdedMinecraftClub.Poller.Library
{
    public class Ping
    {
        public int ServerId { get; set; }
        public DateTime PingTime { get; set; }
        public int PlayersOnline { get; set; }
        public int PlayersMax { get; set; }
    }
}