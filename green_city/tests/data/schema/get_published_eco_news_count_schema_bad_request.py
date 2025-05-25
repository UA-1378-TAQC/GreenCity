BAD_REQUEST_SCHEMA = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "status": {"type": "integer"},
        "timestamp": {"type": "string"},
    },
    "required": ["message", "status", "timestamp"]
}