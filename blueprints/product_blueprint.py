from flask.blueprints import Blueprint
from ..handlers.prdouct_handler import Products
from ..models.Products import All_Products
from ..models.fitting import Regular_fit, Relaxed_fit

blueprint = Blueprint('product_blueprints',__name__)


@blueprint.route('/store_all_data', methods=['GET'])
def store_datas_():
    data = Products._store_data_()
    return data

@blueprint.route('/store_fitting_data', methods=['GET'])
def store_fit_data_():
    data = Products.store_fit_data()
    # data = Products.save_fits()
    return data

@blueprint.route('/all_products', methods=['GET'])
def all_products_():
    data = All_Products.query.all()
    # print(data)
    return data
    pass

@blueprint.route('/regular_fit', methods=['GET'])
def get_regular_fit():
    data = Regular_fit.query.all()
    print(data)
    return data
    pass

@blueprint.route('/relaxed_fit', methods=['GET'])
def get_relaxed_fit():
    data = Relaxed_fit.query.all()
    return data

@blueprint.route('/fitting_data', methods=['GET'])
def get_fit_data():
    data = Products.get_fit_data()
    return data    

@blueprint.route('/check', methods=['GET'])
def check():
    return "Ok"