def test_get_activities_returns_expected_shape(client):
    # Arrange

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert payload

    sample_activity = next(iter(payload.values()))
    assert {"description", "schedule", "max_participants", "participants"}.issubset(
        sample_activity.keys()
    )
    assert isinstance(sample_activity["participants"], list)
