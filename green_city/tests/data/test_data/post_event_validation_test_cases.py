post_event_validation_test_cases = [
    # Scenario 1: Invalid Title
    {
        "name": "empty_title",
        "payload": {"title": ""},
        "expected_errors": [
            {"name": "title", "message": "must not be blank"},
            {"name": "title", "message": "Size must be between 1 and 70 after decoding"}
        ]
    },

    # Scenario 2: Invalid Description
    {
        "name": "empty_description",
        "payload": {"description": ""},
        "expected_errors": [
            {"name": "description", "message": "must not be blank"},
            {"name": "description",
             "message": "Description must be at least 10 characters long (excluding leading / trailing spaces) and must not contain consecutive spaces."},
            {"name": "description", "message": "size must be between 10 and 63206"}
        ]
    },


    # Scenario 3: Invalid Date Validation
    {
        "name": "past_start_date",
        "payload": {"datesLocations": [{"startDate": "2020-05-27T15:00:00Z", "finishDate": "2027-05-27T17:00:00Z"}]},
        "expected_errors": [
            {"message": "Start date must be in future and before finish date"}
        ]
    },

    # Scenario 4: Invalid Coordinates
    #  {
    #     "name": "invalid_coordinates",
    #     "payload": {
    #         "coordinates": {
    #             "latitude": 9999,
    #             "longitude": 9999
    #         }
    #     },
    #     "expected_errors": [
    #         {
    #             "message": "The coordinates field must not be empty"
    #         }
    #     ]
    # },

    # Scenario 5: Invalid URL Format
    # {
    #     "name": "invalid_url",
    #     "payload": {
    #         "onlineLink": "htp:/bad_url"
    #     },
    #     "expected_errors": [
    #         {
    #             "message": "Malformed URL. The string could not be parsed."
    #         }
    #     ]
    # },

    # Scenario 6: Empty Tags Validation
    {
        "name": "empty_tags",
        "payload": {"tags": []},
        "expected_errors": [
            {"name": "tags", "message": "must not be empty"}
        ]
    }
]
