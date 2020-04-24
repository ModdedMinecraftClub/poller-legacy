using System;
using System.Collections.Generic;
using System.Linq;
using Dapper;
using MySql.Data.MySqlClient;

namespace ModdedMinecraftClub.Poller.Library
{
    public class DatabaseConnection : IDisposable
    {
        private readonly MySqlConnection _connection;

        public DatabaseConnection()
        {
            _connection = new MySqlConnection(Helper.GetConnectionString());
        }

        #region Query

        public bool DoesTableExist(string name)
        {
            const string sql =
                "SELECT count(*) FROM information_schema.TABLES WHERE TABLE_NAME = @name;";
            
            var q = _connection.Query<int>(sql, new { name }).ToList();
            
            return q[0] != 0;
        }

        public IEnumerable<Server> GetEnabledServers()
        {
            const string sql =
                "select serverId, serverIp, serverPort from server where enabled = 1;";

            return _connection.Query<Server>(sql);
        }

        #endregion

        #region Execute

        public void InsertPings(IEnumerable<Ping> pings)
        {
            const string sql =
                "insert into pings (serverId, pingTime, playersOnline, playersMax) VALUES (@serverId, @pingTime, @playersOnline, @playersMax);";

            _connection.Execute(sql, pings);
        }

        #endregion

        public void Dispose()
        {
            _connection.Dispose();
        }
    }
}