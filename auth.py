from flask import request, jsonify
from functools import wraps

def token_required(f):
    
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        print("Headers received:", request.headers) 
        print("Token received:", token)  
        if not token or token != 'valid_token':
            return jsonify({"message": "Invalid or missing token!"}), 403
        return f(*args, **kwargs)
    return decorated







