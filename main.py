import json
import pandas as pd
import matplotlib.pyplot as plt

def analyze_logs(file_path):
    log_data = []
    
    with open(file_path, 'r') as f:
        for line in f:
            try:
                entry = json.loads(line)
                # Capture key fields for analysis
                log_data.append({
                    'time': entry.get('time'),
                    'ip': entry.get('remoteAddr'),
                    'message': entry.get('message'),
                    'app': entry.get('app')
                })
            except json.JSONDecodeError:
                continue

    df = pd.DataFrame(log_data)
    
    # Filter for Security Events
    login_failures = df[df['message'].str.contains("Login failed", na=False)]
    email_failures = df[df['message'].str.contains("failed", na=False) & (df['app'] == 'core')]

    print(f"Total Login Failures Found: {len(login_failures)}")
    print(f"Total Email Failures Found: {len(email_failures)}")
    
    # Save a simple visualization
    if not login_failures.empty:
        login_failures['ip'].value_counts().plot(kind='bar', title='Login Failures by IP')
        plt.savefig('output/threat_map.png')

if __name__ == "__main__":
    analyze_logs('logs/nextcloud.log')