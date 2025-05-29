error_event_schemas = {
    "400_validation_errors": {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "message": {"type": "string"}
            },
            "required": ["message"]
        }
    }
}
