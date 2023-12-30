from ..db import db
from dataclasses import dataclass

@dataclass
class Relaxed_fit(db.Model):
    __tablename__ = "relaxed_fit"
    __allow_unmapped__ = True

    id : int
    # uniq_id : str
    fabric : str
    idealfor : str

    id = db.Column(db.Integer,  autoincrement=True, primary_key=True)
    # uniq_id = db.Column(db.String, db.ForeignKey('all_products.uniq_id'), unique=True)
    fabric = db.Column(db.String)
    idealfor = db.Column(db.String)

@dataclass
class Regular_fit(db.Model):
    __tablename__ = "regular_fit"
    __allow_unmapped__ = True

    id : int
    # uniq_id : str
    fabric : str
    idealfor : str

    id = db.Column(db.Integer,  autoincrement=True, primary_key=True)
    # uniq_id = db.Column(db.String, db.ForeignKey('all_products.uniq_id'), unique=True)
    fabric = db.Column(db.String)
    idealfor = db.Column(db.String)