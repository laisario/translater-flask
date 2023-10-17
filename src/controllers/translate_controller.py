from flask import Blueprint, render_template, request

# from deep_translator import GoogleTranslator
from models.language_model import LanguageModel

# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    text_to_translate = (
        request.form.get("text-to-translate") or "O que deseja traduzir"
    )
    translate_from = request.form.get('translate-from') or 'pt'
    translate_to = request.form.get('translate-to') or 'en'
    translated = 'Tradução'
    languages= LanguageModel.list_dicts()
    return languages
    # return render_template(
    #     "index.html",
    #     languages=languages,
    #     text_to_translate=text_to_translate,
    #     translate_from=translate_from,
    #     translate_to=translate_to,
    #     translated=translated
    # )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    raise NotImplementedError
