from ..db import db
from dataclasses import dataclass
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON
from .fitting import Regular_fit, Relaxed_fit

@dataclass
class All_Products(db.Model):
    __tablename__ = "all_products"
    __allow_unmapped__ = True

    id : int
    uniq_id : str
    crawl_timestamp : datetime
    product_url : str
    product_name : str
    product_category_tree : str
    pid : str
    retail_price : str
    discounted_price : str
    image : str
    is_FK_Advantage_product : bool
    description : str
    product_rating : str
    overall_rating : str
    brand : str
    product_specifications : str

    id = db.Column(db.Integer,  autoincrement=True, primary_key=True)
    uniq_id = db.Column(db.String)
    crawl_timestamp = db.Column(db.DateTime)
    product_url = db.Column(db.String)
    product_name = db.Column(db.String)
    product_category_tree = db.Column(db.String)
    pid = db.Column(db.String)
    retail_price = db.Column(db.String)
    discounted_price = db.Column(db.String)
    image = db.Column(db.String)
    is_FK_Advantage_product = db.Column(db.Boolean)
    description = db.Column(db.String)
    product_rating = db.Column(db.String)
    overall_rating = db.Column(db.String)
    brand = db.Column(db.String)
    product_specifications = db.Column(db.String)

    # relaxed_fit : Relaxed_fit =  db.relationship('Relaxed_fit', backref='all_products', uselist=False, lazy=True)
    # regular_fit : Regular_fit = db.relationship('Regular_fit', backref='all_products', uselist=False, lazy=True)
    

#  foreign_keys=[agent_id],

# uniq_id,	crawl_timestamp,	product_url,	product_name,	product_category_tree,	pid,	retail_price,	discounted_price,	image,	is_FK_Advantage_product,	description,	product_rating,	overall_rating,	brand,	product_specifications

