
url = 'http://localhost:3000'

test('GET to /api/v1/status', async () => {
  const response = await fetch(`${url}/api/v1/status`);
  expect(response.status).toBe(200);

  const responseBody = await response.json();
  expect(responseBody.status).toBe('ok');
  expect(responseBody.updated_at).toBeDefined();
  const parsedUpdatedAt = new Date(responseBody.updated_at).toISOString();
  expect(responseBody.updated_at).toEqual(parsedUpdatedAt);

  console.log(responseBody.database);
  expect(responseBody.database.version).toEqual('16.6');
  expect(responseBody.database.conect_max).toEqual(100);
  expect(responseBody.database.conect_used).toEqual(1);

})