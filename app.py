from flask import Flask, render_template, request, jsonify
import psutil
import time

app = Flask(__name__)

@app.route('/')
def index():
    if 'json' in request.args:
        # Get system metrics
        cpu_usage = psutil.cpu_percent()
        print(cpu_usage)
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        connections = psutil.net_connections(kind='inet')
        
        # Get unique listening ports
        open_ports = set()
        for conn in connections:
            if conn.status == 'LISTEN' and conn.laddr:
                open_ports.add(conn.laddr.port)
        open_ports = sorted(list(open_ports))


        return jsonify({
            'cpu_usage': cpu_usage,
            'ram': {
                'total': ram.total,
                'available': ram.available,
                'used': ram.used,
                'percent': ram.percent
            },
            'disk': {
                'total': disk.total,
                'used': disk.used,
                'free': disk.free,
                'percent': disk.percent
            },
            'open_ports': open_ports,
            'timestamp': time.time()
        })
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')