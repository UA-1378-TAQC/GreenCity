UNAUTHORIZED_REQUEST_SCHEMA = {
    "type": "object",
    "properties": {
        "error": {"type": "string"},
        "status": {"type": "integer"}
    },
    "required": ["error", "status"]
}
