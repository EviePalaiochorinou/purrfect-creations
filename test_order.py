from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_documents():
    response = client.get('/dashboard/')
    assert response.status_code == 200

# Ideally, here I would mock the Airtable Api Client in order to write more tests
# that do not make real calls to the external api. This way I can test if I get
# the responses I am expecting.