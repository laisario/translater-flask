from flask import Blueprint
import json
from models.history_model import HistoryModel


history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/", methods=["GET"])
def index():
    translation_history_str = HistoryModel.list_as_json()
    translation_history_json = json.loads(translation_history_str)
    return translation_history_json, 200
