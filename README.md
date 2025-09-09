# smart-dashboard

A customizable smart dashboard that displays Google Calendars, editable meal plans, a to-do list, and weather, designed for Raspberry Pi deployment.

## Developed by Courtney B. Watson

### Features:
- Google Calendar integration (multiple accounts)
- Editable weekly meal plan
- To-do list with add/remove/toggle
- Weather widget for Boston, MA
- Manual refresh + dark/light mode toggle
- Mobile/TV responsive UI

### Setup Instructions:
1. Clone repo and install dependencies:
```bash
pip install -r requirements.txt
```

2. Add your Google Calendar service account credentials as `credentials.json`
3. Share your calendars with the service account email
4. Run the app:
```bash
python app.py
```

### Raspberry Pi Deployment:
Use `setup_pi.sh` to install and launch on boot.
