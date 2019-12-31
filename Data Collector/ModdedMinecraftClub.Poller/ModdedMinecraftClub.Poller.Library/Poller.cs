using System;
using System.Collections.Generic;
using TraceLd.MineStatSharp;

namespace ModdedMinecraftClub.Poller.Library
{
    public class Poller
    {
        private readonly IEnumerable<Server> _servers;

        public Poller(IEnumerable<Server> servers)
        {
            _servers = servers;
        }

        public LinkedList<Ping> Poll()
        {
            var pings = new LinkedList<Ping>();
            
            foreach (var server in _servers)
            {
                var ms = new MineStat(server.ServerIp, (ushort)server.ServerPort);

                if (ms.ServerUp)
                {
                    var ping = new Ping
                    {
                        ServerId = server.ServerId,
                        PingTime = DateTime.Now,
                        PlayersOnline = int.Parse(ms.CurrentPlayers),
                        PlayersMax = int.Parse(ms.MaximumPlayers)
                    };

                    pings.AddFirst(ping);
                }
                else
                {
                    Console.WriteLine($"[{DateTime.Now}]Server {server.ServerIp}:{server.ServerPort} is down.");
                }
            }

            return pings;
        }
    }
}