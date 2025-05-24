schemas_get_request={
    "summary_schema_message": {
        "type": "object",
            "properties": {
                "message": {"type": "string"}
            },
            "required": ["message"],
            "additionalProperties": False
    },
    "summary_schema_valid_result":{
        "type": "object",
            "properties": {
                "content": {"type": "string"},
                "source": {"type": "string"}
            },
            "required": ["content","source"],
            "additionalProperties": False
    },
    "summary_schema_error": {
        "type": "object",
            "properties": {
                "timestamp": {"type": "string"},
                "status": {"type": "number"},
                "error": {"type": "string"},
                "path": {"type": "string"}
            },
            "required": ["timestamp", "status", "error", "path"],
            "additionalProperties": False
    }
}