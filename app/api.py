from flask import Blueprint, jsonify, g, session, request
from app.firebase_admin_init import verify_firebase_token
from app.models import db, User, UserSession

api = Blueprint("api", __name__, url_prefix="/api")

def get_or_create_user(uid, firebase_user):
    user = User.query.filter_by(uid=uid).first()
    if user:
        return user
    user = User(
        uid=uid,
        email=firebase_user.get("email"),
        display_name=firebase_user.get("name") or firebase_user.get("email")
    )
    db.session.add(user)
    db.session.commit()
    return user

@api.route("/session/login", methods=["POST"])
@verify_firebase_token
def session_login():
    uid = g.get("uid")
    firebase_user = g.get("firebase_user", {})
    
    data = request.get_json() or {}
    name = data.get("name") or firebase_user.get("name") or firebase_user.get("email")
    picture = data.get("picture") or firebase_user.get("picture")

    try:
        user = User.query.filter_by(uid=uid).first()
        if user:
            if name and user.display_name != name:
                user.display_name = name
                db.session.commit()
        else:
            user = User(
                uid=uid,
                email=firebase_user.get("email"),
                display_name=name
            )
            db.session.add(user)
            db.session.commit()
            
        user_session = UserSession(
            user_id=user.id,
            ip_address=request.remote_addr,
            user_agent=request.user_agent.string
        )
        db.session.add(user_session)
        db.session.commit()
    except Exception:
        return jsonify({"error": "failed to create user"}), 500
        
    session["uid"] = uid
    session["user"] = {
        "name": name,
        "picture": picture
    }
    session.permanent = True
    return jsonify({"ok": True, "uid": uid}), 200



