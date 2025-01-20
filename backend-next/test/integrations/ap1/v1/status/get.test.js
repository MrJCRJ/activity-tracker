
url = 'http://localhost:3000'

test('GET to /api/v1/status', async () => {
  const response = await fetch(`${url}/api/v1/status`);
  expect(response.status).toBe(200);

})