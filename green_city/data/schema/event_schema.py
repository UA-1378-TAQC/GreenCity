EVENT_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "organizer": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "organizerRating": {"type": ["number", "null"]},
                "email": {"type": "string"}
            },
            "required": ["id", "name", "email"]
        },
        "creationDate": {"type": "string", "format": "date"},
        "description": {"type": "string"},
        "dates": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "startDate": {"type": "string", "format": "date-time"},
                    "finishDate": {"type": "string", "format": "date-time"},
                    "onlineLink": {"type": "string"},
                    "id": {"type": ["integer", "null"]},
                    "event": {"type": ["string", "null"]},
                    "coordinates": {
                        "type": "object",
                        "properties": {
                            "latitude": {"type": "number"},
                            "longitude": {"type": "number"},
                            "streetEn": {"type": "string"},
                            "streetUa": {"type": "string"},
                            "houseNumber": {"type": "string"},
                            "cityEn": {"type": "string"},
                            "cityUa": {"type": "string"},
                            "regionEn": {"type": "string"},
                            "regionUa": {"type": "string"},
                            "countryEn": {"type": "string"},
                            "countryUa": {"type": "string"},
                            "formattedAddressEn": {"type": "string"},
                            "formattedAddressUa": {"type": "string"}
                        },
                        "required": ["latitude", "longitude"]
                    }
                },
                "required": ["startDate", "finishDate", "coordinates"]
            }
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "nameUa": {"type": "string"},
                    "nameEn": {"type": "string"}
                },
                "required": ["id", "nameUa", "nameEn"]
            }
        },
        "titleImage": {"type": "string"},
        "additionalImages": {
            "type": "array",
            "items": {"type": "string"}
        },
        "type": {"type": "string"},
        "isRelevant": {"type": "boolean"},
        "likes": {"type": "integer"},
        "dislikes": {"type": "integer"},
        "countComments": {"type": "integer"},
        "eventRate": {"type": "number"},
        "currentUserGrade": {"type": ["integer", "null"]},
        "open": {"type": "boolean"},
        "isSubscribed": {"type": "boolean"},
        "isFavorite": {"type": "boolean"},
        "isOrganizedByFriend": {"type": "boolean"}
    },
    "required": [
        "id",
        "title",
        "organizer",
        "creationDate",
        "description",
        "dates",
        "tags",
        "open",
        "isRelevant"
    ]
}
