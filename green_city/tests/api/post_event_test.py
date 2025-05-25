from jsonschema import validate
from green_city.tests.data.schema.event_schema import EVENT_SCHEMA
import green_city.src.util.logging_config
import logging

logger = logging.getLogger(__name__)

def test_create_event(create_event):
    event_data = create_event

    validate(instance=event_data, schema=EVENT_SCHEMA)




