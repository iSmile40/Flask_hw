from flask import request, jsonify
from flask.views import MethodView

from app import app, db

from models import Ads

from validator import validate
from schema import ADS_CREATE


class AdsView(MethodView):

    def get(self, ad_id):
        advertisement = Ads.by_id(ad_id)
        return jsonify(advertisement.to_dict())

    @validate('json', ADS_CREATE)
    def post(self):
        advertisement = Ads(**request.json)
        advertisement.add()

        return jsonify(advertisement.to_dict())

    def delete(self):
        advert_data = request.json
        advert = Ads(**request.json)
        Ads.query.filter_by(**advert_data).delete()
        db.session.commit()
        return jsonify({'id': advert.id})


app.add_url_rule('/ads/<int:ad_id>', view_func=AdsView.as_view('advertisements_get'), methods=['GET'])
app.add_url_rule('/ads/', view_func=AdsView.as_view('advertisements_create'), methods=['POST'])
app.add_url_rule('/ads/', view_func=AdsView.as_view('advertisements_delete'), methods=['DELETE'])
