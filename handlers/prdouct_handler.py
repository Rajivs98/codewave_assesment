from ..models.Products import All_Products
from ..models.fitting import Regular_fit, Relaxed_fit
# import requests
from flask import request, jsonify, Response, make_response
import pandas as pd
from ..db import db
import json, csv, re
# from sqlalchemy.orm import sessionmaker


class Products:
    def __init__(self) -> None:
        pass

    def _store_data_():
        try:
            if 'file' not in request.files:
                return {'error': 'No file attached'}
            file = request.files.get('file')
            # path = 'files/flipkart_1.csv' 
            df = pd.read_csv(file)
            products_data = df.to_dict(orient='records')
            # print("products_data", type(products_data))
            
            for data in products_data:
                # print(data['product_specifications'])        
                all_ = All_Products(
                    uniq_id = data['uniq_id'],
                    crawl_timestamp = data['crawl_timestamp'],
                    product_url = data['product_url'],
                    product_name = data['product_name'],
                    product_category_tree = data['product_category_tree'],
                    pid = data['pid'],
                    retail_price = data['retail_price'],
                    discounted_price = data['discounted_price'],
                    image = data['image'],
                    is_FK_Advantage_product = data['is_FK_Advantage_product'],
                    description = data['description'],
                    product_rating = data['product_rating'],
                    overall_rating = data['overall_rating'],
                    brand = data['brand'],
                    product_specifications = data['product_specifications'],
                )
                # rel = 'fit' in data['product_specifications'] and data['product_specifications']['fit'] == 'relaxed'

                # relaxed = Relaxed_fit(
                #     fabric = '',
                #     idealfor = ''
                # )
                # reg = ''
                # regular = Regular_fit(
                #     fabric = '',
                #     idealfor = ''
                # )
                db.session.add(all_)
                db.session.commit()
            return jsonify("file uploded")
        except Exception as e:
            return jsonify({"err": str(e)})
    
        

    def store_fit_data():
        products = All_Products.query.all()
        # products = All_Products.query.filter('key'=='Fit')
        try:
            for product in products:
                # print(product.product_specifications)
                # print(type(product.product_specifications))
                data=product.product_specifications
            
                regular_pattern = r'"key"\s*=>\s*"Fit",\s*"value"\s*=>\s*("Regular"|"Regular Fit")'
                relaxed_pattern = r'"key"\s*=>\s*"Fit",\s*"value"\s*=>\s*("Relaxed"|"Relaxed Fit")'

                regular_match = re.search(regular_pattern, data)
                relaxed_match = re.search(relaxed_pattern, data)

                if regular_match:
                    fabric_match = re.search(r'"key"\s*=>\s*"Fabric",\s*"value"\s*=>\s*"(.*?)"', data)
                    idealfor_match = re.search(r'"key"\s*=>\s*"Ideal For",\s*"value"\s*=>\s*"(.*?)"', data)
                    if fabric_match and idealfor_match:
                        fabric_value = fabric_match.group(1)
                        # print(f"{fabric_value}")
                        idealfor_value = idealfor_match.group(1)
                        print(f" {idealfor_value}")
                        regular_fit_ = Regular_fit(
                            fabric=fabric_value,
                            idealfor=idealfor_value
                        )
                        db.session.add(regular_fit_)
                        db.session.commit()
                
                if relaxed_match:
                    fabric_match = re.search(r'"key"\s*=>\s*"Fabric",\s*"value"\s*=>\s*"(.*?)"', data)
                    idealfor_match = re.search(r'"key"\s*=>\s*"Ideal For",\s*"value"\s*=>\s*"(.*?)"', data)
                    if fabric_match and idealfor_match:
                        fabric_value = fabric_match.group(1)
                        # print(f"{fabric_value}")
                        idealfor_value = idealfor_match.group(1)
                        print(f" {idealfor_value}")
                        relaxed_fit_ = Relaxed_fit(
                            fabric=fabric_value,
                            idealfor=idealfor_value)
                        db.session.add(relaxed_fit_)
                        db.session.commit()
                # else:
                #     pass
                # db.session.commit()
                # db.session.close()
            return jsonify("Data Store Success"), 200
        except Exception as e:
            return ({"erroe": str(e)}), 400



    def get_fit_data():
        try:
            fit_type = request.json.get('type_of_fit')
            if fit_type == 'relaxed':
                data = Relaxed_fit.query.all()
                return jsonify(data), 200
            elif fit_type == 'regular':
                data = Regular_fit.query.all()
                # data.headers['Content-Type']='application/json'
                # data.headers['Access-Control-Allow-Origin'] = '*'
                return jsonify(data)
                # return Response(json.dumps(data), mimetype="application/json",), 200
            else:
                return jsonify({"error": "Invalid fit type"}), 400
        except Exception as e:
            return jsonify({"err" : str(e)}), 400


    def check_():
        return "ok"
