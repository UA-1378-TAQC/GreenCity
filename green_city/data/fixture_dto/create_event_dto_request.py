create_event_dto_request = {
        "title": "Test Event",
        "description": "Test description with enough length",
        "open": True,
        "datesLocations": [{
            "startDate": "2026-05-27T15:00:00Z",
            "finishDate": "2027-05-27T17:00:00Z",
            "coordinates": {
                "latitude": 40.7128,
                "longitude": -74.0060
            },
            "onlineLink": "https://example.com"
        }],
        "tags": ["Social"]
    }