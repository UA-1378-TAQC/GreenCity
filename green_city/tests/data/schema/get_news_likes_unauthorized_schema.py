unauthorized_schema = {
    "type": "object",
    "properties": {
        "timestamp": {"type": "string"},
        "status": {"type": "integer", "enum": [401]},
        "error": {"type": "string", "enum": ["Unauthorized"]},
        "path": {"type": "string"}
    },
    "required": ["timestamp", "status", "error", "path"]
}
