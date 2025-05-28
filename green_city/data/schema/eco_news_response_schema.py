eco_news_response_schema = {
    "type": "object",
    "required": ["page", "currentPage", "totalPages", "totalElements"],
    "properties": {
        "page": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "title", "creationDate", "tagsEn", "author"],
                "properties": {
                    "id": {"type": "integer"},
                    "title": {"type": "string"},
                    "creationDate": {"type": "string", "format": "date-time"},
                    "tagsEn": {"type": "array", "items": {"type": "string"}},
                    "tagsUa": {"type": "array", "items": {"type": "string"}},
                    "author": {
                        "type": "object",
                        "required": ["id", "name"],
                        "properties": {
                            "id": {"type": "integer"},
                            "name": {"type": "string"}
                        }
                    }

                }
            }
        },
        "currentPage": {"type": "integer"},
        "totalPages": {"type": "integer"},
        "totalElements": {"type": "integer"},
        "first": {"type": "boolean"},
        "last": {"type": "boolean"},
        "hasNext": {"type": "boolean"},
        "hasPrevious": {"type": "boolean"}
    }
}
