from flask import Flask
from flask_restful import Api,Resource,reqparse,abort,fields,marshal_with
from flask_sqlalchemy import SQLAlchemy
app = Flask (__name__)
api = Api (app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///C:/Users/adana/yeni/database.accdb'
db = SQLAlchemy(app)
class VideoModel(db.Model):
     id = db.Column(db.Integer,primary_key = True)
     name = db.Column(db.String(100),nullable= False)
     views= db.Column(db.Integer,nullable=False)
     likes= db.Column(db.Integer,nullable=False)

     def __repr__(self):
          return f"Video(name = {name},views={views},likes={likes})"

db.create_all()

names = {"tim": {"age":19, "gender": "male"},
        "bill": {"age":25,"gender": "undecided"}}
 class HelloWorld(Resource):
     def get(self,name):
          return names[name] 
     def post(self):
          return {"data": "Helloworld"}
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name",type=str,help ="Name of the video")
video_put_args.add_argument("views",type=int,help ="Views of the video")
video_put_args.add_argument("likes",type=int,help ="Likes of the video")
resource_fields = {
    'id' : fields.Integer,
    'name':fields.String ,
    'views':fields.Integer,
    'likes':fields.Integer
}

def abort_if_video_id_doesnt_exist(video_id):
     if video_id not in videos:
          abort(404,message="Video id is not valid")
def abort_if_video_exist(video_id):
     if video_id in videos:
         abort(409,message = "Video already exitst with that ID..")

class Video(Resource):
     marshal_with(resource_fields)
     def get(self,video_id):
          result = VideoModel.query.get(id = video_id)
          return result
          #abort_if_video_id_doesnt_exist(video_id)
          #return videos[video_id]
     marshal_with(resource_fields)
     def put(self,video_id):
           args = video_put_args.parse_args()
           result = VideoModel.query.filter_by(id = video_id).first()
           if result :
               abort(409,message = "You cant do that")
           db.session.add(video)
           db.session.commit()
           return videos,201
     def put(self,video_id):
          args = video_put_args.parse_args()
          result = VideoModel.query.filter_by(id = video_id).first()
          if not result :
               abort(409,message = "You cant do that")
          if "name" in args : 
               result.name = args ['name']
          if "views" in args:
               result.views = args ['views']
          if "likes" in args:
               result.likes = args['likes']
               db.session.add(result)
               db.session.commit()

               return result
     def delete(self,video_id):
          abort_if_video_id_doesnt_exist(video_id)
          del videos[video_id]
          return "",204


api.add_resource(Video,"/video/<int:video_id>")
#api.add_resource(HelloWorld,"/helloworld/<string:name>")
# in up we want that user to enter input string and adding get method the name parameter


if __name__ == "__main__":
     app.run(debug=True)
