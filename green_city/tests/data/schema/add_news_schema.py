post_schema = {
    "201_schema": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "content": {"type": "string"},
            "shortInfo": {"type": "string"},
            "author": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"}
                },
                "required": ["id", "name"]
            },
            "creationDate": {"type": "string", "format": "date-time"},
            "imagePath": {"type": ["string", "null"]},
            "source": {"type": "string"},
            "tagsUa": {"type": "array"},
            "tagsEn": {"type": "array"},
            "likes": {"type": "integer"},
            "countComments": {"type": "integer"},
            "countOfEcoNews": {"type": "integer"},
            "favorite": {"type": "boolean"}
        },
        "required": ["id", "title", "content", "author", "creationDate", "source"]
    },
    "400_schema": {
        "type": "object",
        "properties": {
            "message": {"type": "string"}
        },
        "required": ["message"]
    },
    "401_schema": {
        "type": "object",
        "properties": {
            "timestamp": {"type": "string"},
            "status": {"type": "integer"},
            "error": {"type": "string"},
            "path": {"type": "string"}
        },
        "required": ["status", "error", "path"]
    }
}