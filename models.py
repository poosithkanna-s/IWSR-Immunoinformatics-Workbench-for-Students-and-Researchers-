from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy as sqla

db=sqla()

class Analysis(db.Model):
    id=db.column(db.Integer, primary_key=True)
    kind=db.Column(db.String(20), nullable=False)
    input_text=db.column(db.Text, nullable=False)
    result_json=db.Column(db.Text, nullable=False)
    created_