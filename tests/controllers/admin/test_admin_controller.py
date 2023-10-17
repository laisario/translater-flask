from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test):
    user = {"name": "Peter", "level": "admin", "token": "token_secreto123"}
    UserModel.drop()
    HistoryModel.drop()
    UserModel(user).save()
    history = HistoryModel(
        {
            "text_to_translate": "Hello, I like coca",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ).save()
    result = app_test.delete(
        f"/admin/history/{history.id}",
        headers={
            "Authorization": "token_secreto123",
            "User": "Peter",
        },
    )
    assert result.status_code == 204
