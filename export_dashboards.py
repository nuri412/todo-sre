import requests
import json
import os

# Grafana API configuration
GRAFANA_URL = "http://localhost:3000"
API_KEY = "YOUR_API_KEY"  # You'll need to create this in Grafana
EXPORT_DIR = "grafana_dashboards"

def export_dashboards():
    # Create export directory if it doesn't exist
    if not os.path.exists(EXPORT_DIR):
        os.makedirs(EXPORT_DIR)

    # Headers for Grafana API
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        # Get all dashboards
        search_url = f"{GRAFANA_URL}/api/search"
        response = requests.get(search_url, headers=headers)
        dashboards = response.json()

        for dashboard in dashboards:
            if dashboard.get("type") == "dash-db":
                # Get dashboard JSON
                uid = dashboard.get("uid")
                dashboard_url = f"{GRAFANA_URL}/api/dashboards/uid/{uid}"
                dashboard_response = requests.get(dashboard_url, headers=headers)
                dashboard_json = dashboard_response.json()

                # Save to file
                filename = f"{EXPORT_DIR}/{dashboard.get('title').replace(' ', '_')}.json"
                with open(filename, 'w') as f:
                    json.dump(dashboard_json, f, indent=2)
                print(f"Exported dashboard: {dashboard.get('title')}")

    except Exception as e:
        print(f"Error exporting dashboards: {str(e)}")

if __name__ == "__main__":
    print("Starting dashboard export...")
    export_dashboards()
    print("Export complete!") 