# import json
from src.models.history_model import HistoryModel
import json


# Req. 7
def test_request_history():
    expected = [
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        },
    ]
    json_list = HistoryModel.list_as_json()
    json_converted = json.loads(json_list)
    for dicionario in json_converted:
        dicionario.pop("_id", None)
    print(">>>>>>>>>>>", json_converted, "<<<<<<<<<<<<<<<")
    assert json_converted == expected
