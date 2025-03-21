# Flask System Monitor

A simple Flask application to monitor system metrics, including CPU usage, RAM, disk usage, and open ports. The application provides a JSON API and an HTML-based dashboard.

## Features

- **CPU Usage Monitoring**: Get real-time CPU usage percentage.
- **RAM Usage**: View total, available, used, and percentage of memory usage.
- **Disk Usage**: Monitor total, used, free, and percentage of disk usage.
- **Open Ports Detection**: Lists unique listening ports on the system.
- **JSON API**: Returns system metrics in JSON format when queried with `?json` in the URL.

## Installation

### Prerequisites

- Python 3.x
- `pip` (Python package manager)

### Steps

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/flask-system-monitor.git
   cd flask-system-monitor
   ```

2. Create a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Run the application:

   ```sh
   python app.py
   ```

5. Open your browser and go to:

   ```
   http://localhost:5000/
   ```

   To get JSON output:

   ```
   http://localhost:5000/?json
   ```

## Deployment

To deploy on a production server, consider using **Gunicorn**:

```sh
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## API Response Example

When accessing `http://localhost:5000/?json`, the response will look like:

```json
{
    "cpu_usage": 12.5,
    "ram": {
        "total": 16777216,
        "available": 8321234,
        "used": 8465982,
        "percent": 50.5
    },
    "disk": {
        "total": 512000000000,
        "used": 256000000000,
        "free": 256000000000,
        "percent": 50.0
    },
    "open_ports": [22, 80, 443],
    "timestamp": 1711035600.123456
}
```

## License

This project is licensed under the MIT License.

## Author

[Abir Sarkar](https://github.com/knightabir)
