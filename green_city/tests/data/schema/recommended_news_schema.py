recommended_news_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "creationDate": {"type": "string", "format": "date-time"},
            "imagePath": {"type": ["string", "null"]},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "content": {"type": "string"},
            "shortInfo": {"type": ["string", "null"]},
            "author": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"}
                },
                "required": ["id", "name"]
            },
            "tags": {
                "type": "array",
                "items": {"type": "string"}
            },
            "tagsUa": {
                "type": "array",
                "items": {"type": "string"}
            },
            "likes": {"type": "integer"},
            "dislikes": {"type": "integer"},
            "countComments": {"type": "integer"},
            "hidden": {"type": "boolean"}
        },
        "required": [
            "creationDate", "imagePath", "id", "title", "content",
            "shortInfo", "author", "tags", "tagsUa",
            "likes", "dislikes", "countComments", "hidden"
        ]
    }
}
