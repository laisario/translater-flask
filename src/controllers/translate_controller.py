from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel

from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    text_to_translate = (
        request.form.get("text-to-translate") or "O que deseja traduzir"
    )
    translate_from = request.form.get("translate-from", "pt")
    translate_to = request.form.get("translate-to", "en")
    languages = LanguageModel.list_dicts()

    if request.method == "POST":
        translated = GoogleTranslator(
            source=translate_from, target=translate_to
        ).translate(text_to_translate)
        translation_history = {
            "text_to_translate": text_to_translate,
            "translate_from": translate_from,
            "translate_to": translate_to,
        }
        history = HistoryModel(translation_history)
        history.save()
    else:
        translated = 'Tradução'
        
    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    translate_from = (
        request.form.get("translate-to") if request.method == "POST" else "en"
    )
    translate_to = (
        request.form.get("translate-from")
        if request.method == "POST"
        else "pt"
    )
    translated = (
        request.form.get("text-to-translate")
        if request.method == "POST"
        else "O que deseja traduzir"
    )
    text_to_translate = (
        GoogleTranslator(source=translate_to, target=translate_from).translate(
            translated
        )
        if request.method == "POST"
        else "Tradução"
    )
    languages = LanguageModel.list_dicts()

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )
