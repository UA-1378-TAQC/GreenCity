get_schema={
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

    
get_data = {
    "404_response_body":{
        "status": 404,
        "message":"Eco new doesn't exist by this id: 101"
    },
    "400_response_body":{
        "status": 400,
        "message": "Wrong ecoNewsId. Should be 'Long'"
    },
    "400_response_body_html":{
        "status": 400,
        "error": "Bad Request",
        "path": "/eco-news/%25/summary"
    },  
    "401_response_body":{
        "status": 401,
        "error": "Unauthorized",
        "path": "/eco-news/1/summary"
    },
    "200_response_body":{
        "status": 200,
        "content": "<p>My Test Eco News My Test Eco News</p>",
        "source": ""
    }
}