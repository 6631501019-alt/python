from flask import Flask, request, jsonify
from flask_cors import CORS
import paramiko
import time

app = Flask(__name__)
CORS(app)

@app.route('/api/execute', methods=['POST'])
def execute_command():
    data = request.get_json() or {}
    router_ip = data.get('ip', '').strip()
    command = data.get('command', '').strip()

    if not router_ip or not command:
        return jsonify({
            'success': False,
            'error': 'กรุณากรอกทั้ง IP และคำสั่งของ Router'
        }), 400

    username = "admin"
    password = "cisco"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(
            hostname=router_ip,
            username=username,
            password=password,
            look_for_keys=False,
            allow_agent=False,
            timeout=10,
            banner_timeout=15,
            auth_timeout=15,
            disabled_algorithms={'pubkeys': []}
        )

        shell = ssh.invoke_shell()
        time.sleep(1)

        if shell.recv_ready():
            shell.recv(65535)

        shell.send("terminal length 0\n")
        time.sleep(0.5)

        shell.send(command + "\n")
        time.sleep(2)

        output = ""
        while shell.recv_ready():
            output += shell.recv(65535).decode('utf-8', errors='ignore')

        ssh.close()

        return jsonify({
            'success': True,
            'output': output if output else "Command executed with no output."
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
