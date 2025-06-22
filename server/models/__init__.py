from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .show import Show
from .episode import Episode
from .guest import Guest
from .appearance import Appearance

__all__ = ["db", "User", "Show", "Episode", "Guest", "Appearance"]
