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
                "email": {"type": ["string", "null"]},
            },
            "required": ["id", "name", "email"],
            "additionalProperties": False,
        },
        "creationDate": {"type": "string"},
        "description": {"type": "string"},
        "dates": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "startDate": {"type": "string"},
                    "finishDate": {"type": "string"},
                    "onlineLink": {"type": ["string", "null"]},
                    "id": {"type": ["integer", "null"]},
                    "event": {"type": ["string", "null"]},
                    "coordinates": {
                        "type": "object",
                        "properties": {
                            "latitude":  {"type": "number"},
                            "longitude": {"type": "number"},
                        },
                        "required": ["latitude", "longitude"],
                        "additionalProperties": True,
                    },
                },
                "required": ["startDate", "finishDate", "coordinates"],
                "additionalProperties": False,
            },
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "nameUa": {"type": "string"},
                    "nameEn": {"type": "string"},
                },
                "required": ["id", "nameUa", "nameEn"],
                "additionalProperties": False,
            },
        },
        "titleImage": {"type": ["string", "null"]},
        "additionalImages": {"type": ["array", "null"], "items": {"type": "string"}},
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
        "isOrganizedByFriend": {"type": "boolean"},
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
        "isRelevant",
    ],
    "additionalProperties": False,
}

EVENT_PAGE_SCHEMA = {
    "type": "object",
    "required": ["page", "totalElements", "currentPage"],
    "properties": {
        "page": {"type": "array", "items": EVENT_SCHEMA},
        "totalElements": {"type": "integer"},
        "currentPage": {"type": "integer"},
        "totalPages": {"type": ["integer", "null"]},
        "hasNext": {"type": ["boolean", "null"]},
        "hasPrevious": {"type": ["boolean", "null"]},
        "first": {"type": ["boolean", "null"]},
        "last": {"type": ["boolean", "null"]},
    },
    "additionalProperties": True,
}

EVENT_404_SCHEMA = {
    "type": "object",
    "required": ["message"],
    "properties": {
        "message": {"type": "string"},
    },
    "additionalProperties": True,
}

EVENT_400_SCHEMA = {
    "type": "object",
    "required": ["message"],
    "properties": {
        "message": {"type": "string"},
    },
    "additionalProperties": True,
}
