from flask import Flask, request, Response, json
from flask_restplus import Api, Resource, fields
# import joblib
# import preprocessing as preprocess

flask_app = Flask(__name__)

app = Api(app = flask_app, 
          version = "1.0", 
          title = "Stackoverflow Predict Tag", 
          description = "Tag prediction according to user question")

# name_space = app.namespace('predict', description="Tag prediction according to user question")

# modelapp = app.model('Question Model', 
#           {'title': fields.String(required = True, description="Title of the question", help="Title cannot be blank."), 
#           'body': fields.String(required = True, description = "Description of your question", help="Description cannot be blank.")})

# # Load pre-trained models
# model_path = "exported_models/"
# vectorizer = joblib.load(model_path + "tfidf_vectorizer.pkl", 'r')
# multilabel_binarizer = joblib.load(model_path + "multilabel_binarizer.pkl", 'r')
# model = joblib.load(model_path + "xgboost_classifier_model.pkl", 'r')

# @name_space.route("/")
# class MainClass(Resource):
#     @app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
#     @app.expect(modelapp)
#     def post(self):
#         title = request.json['title']
#         body = request.json['body']
#         cleaned_title = preprocess.preprocess_text(title)
#         cleaned_body = preprocess.preprocess_text(body)
#         corpus = cleaned_title + cleaned_body
#         X_tfidf = vectorizer.transform([corpus])
#         predict = model.predict(X_tfidf)
#         tags = multilabel_binarizer.inverse_transform(predict)
#         results = json.dumps({'tags': tags})
#         return Response(results, status=200, mimetype='application/json')

@app.route("/")
def hello():
    return "hello world"

if __name__ == "__main__":
    app.run()
