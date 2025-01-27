import migrationRunner from 'node-pg-migrate';
import { join } from 'node:path';
import database from 'infra/database';

export default async function migrations(req, res) {
  const allowedMethods = ["GET", "POST"];
  if (!allowedMethods.includes(req.method)) {
    return res.status(405).json({ erro: `Method "${req.method}" not allowed` });
  }

  let dbClient;
  try {
    dbClient = await database.getNewClient();
    const defaultMigrationOptions = {

      dbClient: dbClient,
      dryRun: true,
      dir: join("infra", "migrations"),
      direction: "up",
      verbose: true,
      migrationsTable: "migrations",

    }
    if (req.method === "POST") {
      const migratedMigrations = await migrationRunner({
        ...defaultMigrationOptions,
        dryRun: false,
      })

      if (migratedMigrations.length > 0) {
        return res.status(201).json(migratedMigrations);
      }
      return res.status(200).json(migratedMigrations);
    }

    if (req.method === "GET") {
      const pendingMigrations = await migrationRunner(defaultMigrationOptions)
      return res.status(200).json(pendingMigrations);
    }

  } catch (error) {
    console.error("Error running migrations", error);
    return res.status(500).json({ erro: "Error running migrations" });
  } finally {
    await dbClient.end();
  }

}