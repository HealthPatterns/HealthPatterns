from aid_vault.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    # id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # name: Mapped[str] = mapped_column(String, unique=False, nullable=False)