single_message_schema = {
    "type": "object",
    "properties": {"message": {"type": "string"}},
    "required": ["message"],
    "additionalProperties": False,
}

error_schema = {
    "type": "object",
    "properties": {
        "timestamp": {"type": "string"},
        "status": {"type": "number"},
        "error": {"type": "string"},
        "path": {"type": "string"},
    },
    "required": ["timestamp", "status", "error", "path"],
    "additionalProperties": False,
}
