schema_all_news = {
    "type": "object",
    "properties": {
        "page": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "title": {
                        "type": "string"
                    },
                    "content": {"type": "string"},
                    "shortInfo": {"type": ["string", "null"]},
                    "author": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "name": {"type": "string"}
                        }
                    },
                    "creationDate": {"type": "string"},
                    "imagePath": {"type": ["string", "null"]},
                    "source": {"type": ["string", "null"]},
                    "tagsUa": {"type": "array"},
                    "tagsEn": {"type": "array"},
                    "likes": {"type": "integer"},
                    "countComments": {"type": "integer"},
                    "countOfEcoNews": {"type": "integer"},
                    "favorite": {"type": "boolean"}
                },
                "required": ["id", "favorite"]
            }
        }
    },
    "required": ["page"]
}
