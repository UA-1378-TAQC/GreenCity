EVENT_COMMENT_201 = {
    "type": "object",
    "required": [
        "id",
        "author",
        "text",
        "createdDate",
        "additionalImages"
    ],
    "properties": {
        "id": {"type": "integer"},
        "author": {
            "type": "object",
            "required": ["id", "name", "profilePicturePath"],
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "profilePicturePath": {"type": ["string", "null"]},
            },
            "additionalProperties": False,
        },
        "text": {"type": "string", "minLength": 1, "maxLength": 8000},
        "createdDate": {"type": "string"},
        "additionalImages": {
            "type": "array",
            "items": {"type": "string"},
        },
    },
    "additionalProperties": False,
}

EVENT_COMMENT_400 = {
    "type": "array",
    "minItems": 1,
    "items": {
        "type": "object",
        "required": ["name", "message"],
        "properties": {
            "name": {"type": "string"},
            "message": {"type": "string"},
        },
        "additionalProperties": False,
    },
}

EVENT_COMMENT_401 = {
    "type": "object",
    "required": ["timestamp", "status", "error", "path"],
    "properties": {
        "timestamp": {"type": "string"},
        "status": {"type": "integer", "enum": [401]},
        "error": {"type": "string", "enum": ["Unauthorized"]},
        "path": {"type": "string"},
    },
    "additionalProperties": False,
}

EVENT_COMMENT_404 = {
    "type": "object",
    "required": ["message"],
    "properties": {
        "message": {"type": "string"},
    },
    "additionalProperties": False,
}
