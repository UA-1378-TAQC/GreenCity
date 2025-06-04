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


def update_event_dto_request(event_id):
    return {
        "id": event_id,
        "title": "Updated Event Title",
        "description": "Updated Description",
        "datesLocations": [
            {
                "startDate": "2033-05-27T15:00:00Z",
                "finishDate": "2033-05-27T17:00:00Z",
                "onlineLink": "http://test.example.com"
            }
        ],
        "tags": ["Social"],
        "open": True
    }
