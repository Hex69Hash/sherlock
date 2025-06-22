from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route('/sherlock', methods=['GET'])
def sherlock_lookup():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "No username provided"}), 400

    # Run Sherlock as subprocess
    try:
        result = subprocess.run(
            ['python3', 'sherlock/sherlock.py', username, '--print-found'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return jsonify({
            "output": result.stdout.splitlines()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
