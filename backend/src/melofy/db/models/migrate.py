from melofy.models.user_model import create_all_user, remove_all_user
from melofy.models.music_model import create_all_music, remove_all_music


def apply_all() -> None:
    """
    Apply all the migrations i.e create all database.
    """
    create_all_user()
    create_all_music()


def unapply_all() -> None:
    """
    Delete all the database tables.
    """
    remove_all_user()
    remove_all_music()