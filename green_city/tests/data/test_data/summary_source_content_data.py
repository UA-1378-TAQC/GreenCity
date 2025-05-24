data_get_request = {
    "404_response_body":{
        "status": 404,
        "message":"Eco new doesn't exist by this id: {0}"
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
        "content": "Some cool text here!!!",
        "source": "https://example.org/"
    }
}