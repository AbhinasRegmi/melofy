from melofy.models.user_model import create_all, remove_all


def apply_all() -> None:
    """
    Apply all the migrations i.e create all database.
    """
    create_all()


def unapply_all() -> None:
    """
    Delete all the database tables.
    """
    remove_all()