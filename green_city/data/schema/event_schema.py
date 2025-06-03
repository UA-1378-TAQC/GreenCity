EVENT_201 = {"type": "object",
            "required": [
                "id", "title", "organizer", "creationDate", "description",
                "dates", "tags", "titleImage", "additionalImages", "type",
                "isRelevant", "likes", "dislikes", "countComments", "eventRate",
                "currentUserGrade", "open", "isSubscribed", "isFavorite", "isOrganizedByFriend"
            ],
            "properties": {
                "id": {"type": "integer"},
                "title": {"type": "string"},
                "organizer": {
                    "type": "object",
                    "required": ["id", "name", "organizerRating", "email"],
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"},
                        "organizerRating": {"type": ["number", "null"]},
                        "email": {"type": "string", "format": "email"}
                    }
                },
                "creationDate": {"type": "string", "format": "date"},
                "description": {"type": "string"},
                "dates": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["startDate", "finishDate", "onlineLink"],
                        "properties": {
                            "startDate": {"type": "string", "format": "date-time"},
                            "finishDate": {"type": "string", "format": "date-time"},
                            "onlineLink": {"type": "string", "format": "uri"},
                            "id": {"type": ["integer", "null"]},
                            "event": {"type": ["string", "null"]},
                            "coordinates": {"type": ["object", "null"]}
                        }
                    }
                },
                "tags": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["id", "nameUa", "nameEn"],
                        "properties": {
                            "id": {"type": "integer"},
                            "nameUa": {"type": "string"},
                            "nameEn": {"type": "string"}
                        }
                    }
                },
                "titleImage": {"type": "string"},
                "isRelevant": {"type": "boolean"},
                "likes": {"type": "integer"},
                "dislikes": {"type": "integer"},
                "countComments": {"type": "integer"},
                "eventRate": {"type": "number"},
                "currentUserGrade": {"type": ["number", "null"]},
                "open": {"type": "boolean"},
                "isSubscribed": {"type": "boolean"},
                "isFavorite": {"type": "boolean"},
                "isOrganizedByFriend": {"type": "boolean"}
            }
            }