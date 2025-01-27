import { Client } from 'pg'

async function query(queryObject) {
  let client
  try {
    client = await getNewClient()
    const result = await client.query(queryObject)
    return result
  } catch (error) {
    console.error('Error connecting to the database', error)
    throw error
  } finally {
    await client.end()
  }

}

async function getNewClient() {
  const client = new Client({
    host: process.env.POSTGRES_HOST,
    port: process.env.POSTGRES_PORT,
    user: process.env.POSTGRES_USER,
    password: process.env.POSTGRES_PASSWORD,
    database: process.env.POSTGRES_DB,
    ssl: process.env.NODE_ENV === 'production' ? true : false,
  })

  await client.connect()
  return client
}


export default {
  query,
  getNewClient

}