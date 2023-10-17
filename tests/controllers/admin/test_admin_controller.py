from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test):
    user = {"name": "Peter", "level": "admin", "token": "token_secreto123"}
    UserModel.drop()
    HistoryModel.drop()
    UserModel(user).save()
    HistoryModel(
        {
            "text_to_translate": "Hello, I like coca",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ).save()
    app_test.delete(
        "/admin/history/1",
        headers={
            "Authorization": "token_secreto123",
            "User": "Peter",
        },
    )
