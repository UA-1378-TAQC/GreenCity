TAGS_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "languageCode": {"type": ["string", "null"]}
        },
        "required": ["id", "name"]
    }
}

TAGS_ERROR_MESSAGE_SCHEMA = {
    "type": "object",
    "properties": {
        "message": {"type": "string"}
    },
    "required": ["message"],
    "additionalProperties": False
}
