
from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__continent__)
api = Api(app)

class countries(Resource):
    def get(self):
       data = pd.read_csv('countries.csv')
       data = data.to_dict('records')
       return { 'data' : data}, 200

    def post(self):
        continent = request.args['continent']
        country = request.args['country']
        capital= request.args['capital']

        data = pd.read_csv('countries.csv')

        new_data = pd.DataFrame({
            'continent': [continent],
            'country': [country],
            'capital': [capital]
        })
        data = data.append(new_data, ignore_index=True)
        data.to_csv('countries.csv', index=False)
        return {'data': new_data.to_dict('records')}, 200

    class continent(Resource):
        def get(self):
            data = pd.read_csv('countries.csv', usecols=[0])
            data = data.to_dict('records')
            return {'data': data}, 200

    api.add_resource(continent, '/countriescontinent')
    api.add_resource(countries, '/countries')

    if __continent__ == '__main__':
        app.run(host="0.0.0.0", port=6767)
