from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)
logged_data = []

@app.route('/log', methods=['GET', 'POST'])
def log_request():
    data = {
        'timestamp': datetime.now().isoformat(),
        'method': request.method,
        'headers': dict(request.headers),
        'args': request.args.to_dict(),
        'form': request.form.to_dict(),
        'json': request.get_json() if request.is_json else None,
        'ip': request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    }
    
    logged_data.append(data)
    
    # Keep only last 100 entries to prevent memory issues
    if len(logged_data) > 100:
        logged_data.pop(0)
        
    return jsonify({"status": "logged"})

@app.route('/view_logs')
def view_logs():
    return jsonify(logged_data[-20:])  # Return last 20 entries
