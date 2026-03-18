# IoT Device Health Monitor Dashboard

## Overview
The IoT Device Health Monitor Dashboard is a sophisticated application designed to streamline the monitoring and management of IoT devices. This platform provides a centralized interface where users can track device statuses, monitor battery levels, and receive real-time alerts for critical issues. It is particularly valuable for IoT network administrators and engineers who require a reliable tool to ensure the optimal operation of numerous devices simultaneously. By leveraging a powerful FastAPI backend and a dynamic Jinja2 templated frontend, this dashboard offers a comprehensive solution for visualizing device health metrics and analyzing historical data trends.

## Features
- **Device Management**: Seamlessly view and manage a comprehensive list of all registered IoT devices, including their current status and battery levels.
- **Real-time Alerts**: Receive immediate notifications for critical device issues, such as low battery levels, enabling timely interventions.
- **Data Analytics**: Analyze historical data to identify trends and optimize device performance effectively.
- **User-friendly Dashboard**: Access a centralized dashboard that provides a quick overview of all device statuses and alerts.
- **Customizable Settings**: Configure application settings and device thresholds to tailor the monitoring experience to specific needs.

## Tech Stack
| Technology | Version    |
|------------|------------|
| Python     | 3.11+      |
| FastAPI    | 0.95.2     |
| Uvicorn    | 0.22.0     |
| Jinja2     | 3.1.2      |
| SQLite3    | Built-in   |
| Docker     | Latest     |

## Architecture
The project architecture consists of a FastAPI backend that serves a Jinja2 templated frontend. The backend is responsible for handling API requests and interacting with an SQLite database to manage device and alert data. The frontend renders HTML templates for various views, including the dashboard, devices, alerts, settings, and analytics.

```plaintext
+------------------+
|   Frontend       |
| (HTML Templates) |
+--------+---------+
         |
         |
+--------v---------+
|   FastAPI        |
| (Backend API)    |
+--------+---------+
         |
         |
+--------v---------+
|   SQLite3 DB     |
| (Data Storage)   |
+------------------+
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package installer)
- Docker (optional for containerized deployment)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/iot-device-health-monitor-dashboard-auto.git
   cd iot-device-health-monitor-dashboard-auto
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the FastAPI server using Uvicorn:
   ```bash
   uvicorn app:app --reload
   ```
2. Open your browser and visit `http://127.0.0.1:8000` to access the dashboard.

## API Endpoints
| Method | Path               | Description                                      |
|--------|--------------------|--------------------------------------------------|
| GET    | /api/devices       | Retrieve a list of all devices                   |
| POST   | /api/devices       | Add a new device                                 |
| GET    | /api/alerts        | Retrieve a list of all alerts                    |
| PUT    | /api/devices/{id}  | Update an existing device by its ID              |
| GET    | /                  | Render the main dashboard page                   |
| GET    | /devices           | Render the devices page                          |
| GET    | /alerts            | Render the alerts page                           |
| GET    | /settings          | Render the settings page                         |
| GET    | /analytics         | Render the analytics page                        |

## Project Structure
```
.
├── Dockerfile                # Docker configuration file
├── app.py                    # Main application file containing API logic
├── requirements.txt          # Python dependencies
├── start.sh                  # Shell script to start the application
├── static/
│   └── css/
│       └── bootstrap.min.css # Bootstrap CSS for styling
└── templates/
    ├── alerts.html           # HTML template for alerts page
    ├── analytics.html        # HTML template for analytics page
    ├── dashboard.html        # HTML template for dashboard page
    ├── devices.html          # HTML template for devices page
    └── settings.html         # HTML template for settings page
```

## Screenshots
*Screenshots will be added here to illustrate the user interface and features.*

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t iot-device-monitor .
   ```
2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 iot-device-monitor
   ```
3. Visit `http://127.0.0.1:8000` in your browser to access the application.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the existing style and includes appropriate tests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---
Built with Python and FastAPI.
