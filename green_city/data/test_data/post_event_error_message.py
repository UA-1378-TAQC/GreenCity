import copy

from green_city.data.fixture_dto.create_event_dto_request import create_event_dto_request

post_event_test_data = {
    "empty_title": {
        "payload": dict(
            copy.deepcopy(create_event_dto_request),
            title=""
        ),
        "expected_errors": [
            {"name": "title", "message": "must not be blank"},
            {"name": "title", "message": "Size must be between 1 and 70 after decoding"}
        ]
    },

    "empty_description": {
        "payload": dict(
            copy.deepcopy(create_event_dto_request),
            description=""
        ),
        "expected_errors": [
            {"name": "description", "message": "must not be blank"},
            {"name": "description",
             "message": "Description must be at least 10 characters long (excluding leading / trailing spaces) and must not contain consecutive spaces."},
            {"name": "description", "message": "size must be between 10 and 63206"}
        ]
    },

    "past_start_date": {
        "payload": dict(
            copy.deepcopy(create_event_dto_request),
            datesLocations=[{
                "startDate": "2020-05-27T15:00:00Z",
                "finishDate": "2027-05-27T17:00:00Z",
                "coordinates": {
                    "latitude": 40.7128,
                    "longitude": -74.0060
                },
                "onlineLink": "https://example.com"
            }]
        ),
        "expected_errors": [
            {"message": "Start date must be in future and before finish date"}
        ]
    },

    "invalid_coordinates": {
        "payload": dict(
            copy.deepcopy(create_event_dto_request),
            datesLocations=[{
                "startDate": "2026-05-27T15:00:00Z",
                "finishDate": "2027-05-27T17:00:00Z",
                "coordinates": {
                    "latitude": 9999,
                    "longitude": 9999
                },
                "onlineLink": "https://example.com"
            }]
        ),
        "expected_errors": [
            {"message": "The coordinates field must not be empty"}
        ]
    },

    "invalid_url": {
        "payload": dict(
            copy.deepcopy(create_event_dto_request),
            datesLocations=[{
                "startDate": "2026-05-27T15:00:00Z",
                "finishDate": "2027-05-27T17:00:00Z",
                "coordinates": {
                    "latitude": 40.7128,
                    "longitude": -74.0060
                },
                "onlineLink": "htp:/bad_url"
            }]
        ),
        "expected_errors": [
            {"message": "Malformed URL. The string could not be parsed."}
        ]
    },

    "empty_tags": {
        "payload": dict(
            copy.deepcopy(create_event_dto_request),
            tags=[]
        ),
        "expected_errors": [
            {"name": "tags", "message": "must not be empty"}
        ]
    }
}
