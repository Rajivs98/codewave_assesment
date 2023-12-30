Check Server---->
http://localhost:5000/get/check

For Store all products data---->
http://localhost:5000/get/store_all_data
[upload file parameter - "file" ]

For store fittings by filter cloths----->
http://localhost:5000/get/store_fitting_data

for fetch all products with all fields--->
http://localhost:5000/get/fitting_data

for fetch fittng products --->
http://localhost:5000/get/all_products

pass body "regular" or "relaxed"
{"type_of_fit": "regular"  }


For docker use command 

docker container run -d -p 5000:5000 assesment_by_rajiv

http://localhost:5000/get/check
