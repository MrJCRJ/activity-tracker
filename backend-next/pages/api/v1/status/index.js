import database from 'infra/database';

async function status(req, res) {
  const updateAt = new Date().toISOString();

  const resultPostgresVersion = await database.query('show server_version;');
  const postgresVersion = resultPostgresVersion.rows[0].server_version;

  const resultConectMax = await database.query('show max_connections;');
  const conectMax = resultConectMax.rows[0].max_connections;

  const databaseName = process.env.POSTGRES_DB;
  const resultConectUsed = await database.query({
    text: "SELECT count(*)::int FROM pg_stat_activity WHERE datname = $1;",
    values: [databaseName]
  });
  const conectUsed = resultConectUsed.rows[0].count;

  res.status(200).json({
    status: 'ok',
    updated_at: updateAt,
    database: {
      version: postgresVersion,
      conect_max: parseInt(conectMax),
      conect_used: conectUsed,
    }
  });
}

export default status;