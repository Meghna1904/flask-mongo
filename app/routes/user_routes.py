from flask import Blueprint, request, jsonify
from app.models.user import User
from bson import ObjectId
import pymongo.errors

user_bp=Blueprint("user",__name__,url_prefix="/users")
user_model= User()
@user_bp.route("/",methods=["GET"])
def get_all_users():
    try:
        users=user_model.get_all()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}),500
    

@user_bp.route("/<user_id>",methods=["GET"])
def get_user(user_id):
    try:
        user=user_model.get_by_id(user_id)
        if not user:
            return jsonify({"error":"user not found"}),404
        return jsonify(user),200
    except pymongo.errors.InvalidId:
        return jsonify({"error":"Invalid user ID"}),400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@user_bp.route("/",methods=["POST"])
def create_user():
    try:
        data=request.get_json()
        user_id=user_model.create(data)
        return jsonify({"user_id": user_id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@user_bp.route("/<user_id>",methods=["PUT"])
def update_user(user_id):
    try:
        data=request.get_json()
        updated=user_model.update(user_id,data)
        if not updated:
            return jsonify({"error":"User not found"}),404
        return jsonify({"message":"User updated successfully"}),200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except ValueError as e:
        return jsonify({"error":str(e)}),500
    
@user_bp.route("/user_id",methods=["DELETE"])
def delete_user(user_id):
    try:
        deleted_user=user_model.delete(user_id)
        if not deleted_user:
            return jsonify({"error":"User not found"}),404
        return jsonify({"message":"user deleted successfully"}),200
    except pymongo.errors.InvalidId:
        return jsonify({"error":"Invalid user ID"}),400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
