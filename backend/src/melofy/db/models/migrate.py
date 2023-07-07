from melofy.db.models.user_model import create_all_user, remove_all_user


def apply_all() -> None:
    """
    Apply all the migrations i.e create all database.
    """
    create_all_user()


def unapply_all() -> None:
    """
    Delete all the database tables.
    """
    remove_all_user()