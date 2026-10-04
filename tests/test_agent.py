from fastapi.testclient import TestClient
from review.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'review this diff', **{'payload': {'diff': 'image: api:latest'}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["findings"] == ["latest_tag"]
    refused = client.post("/agent/run", json={"goal": 'merge this pull request'}).json()
    assert refused["refused"] is True
