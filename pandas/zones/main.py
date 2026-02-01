import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


data_list = []

# Read the entire file as a string and split into individual JSON objects
with open('data.jsonl', 'r', encoding='utf-8') as f:
    file_content = f.read()
    json_objects = file_content.split('}\n{')  # Split JSON objects by closing and opening braces

    # Add back the braces removed during splitting
    json_objects = [
        '{' + obj if not obj.startswith('{') else obj for obj in json_objects
    ]
    json_objects = [
        obj + '}' if not obj.endswith('}') else obj for obj in json_objects
    ]

    for obj in json_objects:
        try:
            entry = json.loads(obj)  # Parse each JSON object
            timestamp = entry['message']['timestamp']

            for zone_info in entry['message']['zones']:
                data_list.append({
                    'timestamp': timestamp,
                    'zone': zone_info['zone'],
                    'detect': zone_info['data']['detect'],
                    'count': zone_info['data']['count']
                })
        except json.JSONDecodeError as e:
            logging.error(f"JSONDecodeError: {e} in object: {obj}")

# Ensure data_list is not empty
if not data_list:
    logging.error("No valid data found in data.jsonl. Exiting.")
    exit(1)

# Create DataFrame
df = pd.DataFrame(data_list)

# Ensure 'timestamp' column exists
if 'timestamp' not in df.columns:
    logging.error("'timestamp' column not found in data. Exiting.")
    exit(1)

df['timestamp'] = pd.to_datetime(df['timestamp'])


# Remove filtering by specific zone
# filtered_df = df[df['zone'] == zone_id]
filtered_df = df

# Group data by zone
zones = filtered_df['zone'].unique()

# Create a single figure with subplots for all zones
num_zones = len(zones)
fig, axes = plt.subplots(num_zones + 1, 1, figsize=(12, 6 * (num_zones + 1)), sharex=False)

if num_zones == 1:
    axes = [axes]  # Ensure axes is always a list, even for a single subplot

# Assign colors to each zone
colors = plt.cm.tab10.colors
zone_colors = {zone: colors[i % len(colors)] for i, zone in enumerate(zones)}

# Create a combined plot for all zones at the top
combined_ax = axes[0]
combined_ax.set_xlabel('Time')
combined_ax.set_ylabel('Detect', color='tab:blue')
combined_ax.tick_params(axis='y', labelcolor='tab:blue')

# Format x-axis for time with 60-minute intervals
combined_ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))

# Create a second y-axis for count values
combined_ax2 = combined_ax.twinx()
combined_ax2.set_ylabel('Count', color='tab:red')
combined_ax2.tick_params(axis='y', labelcolor='tab:red')

# Update marker shapes for better distinction
# Detect: Circle, Count: Square
for zone in zones:
    zone_data = filtered_df[filtered_df['zone'] == zone]
    combined_ax.scatter(zone_data['timestamp'], zone_data['detect'], alpha=0.7, s=10, marker='o', color=zone_colors[zone], label=f'Detect - Zone {zone}')
    combined_ax2.scatter(zone_data['timestamp'], zone_data['count'], alpha=0.7, s=10, marker='s', color=zone_colors[zone], label=f'Count - Zone {zone}')

# Format x-axis for time without year
combined_ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
combined_ax.set_title('Combined Zone Data Over Time')

# Create individual plots for each zone
for i, zone in enumerate(zones):
    zone_data = filtered_df[filtered_df['zone'] == zone]

    ax = axes[i + 1]
    ax.set_xlabel('Time')
    ax.set_ylabel('Detect', color='tab:blue')
    ax.tick_params(axis='y', labelcolor='tab:blue')

    # Plot detect values for the zone
    ax.scatter(zone_data['timestamp'], zone_data['detect'], alpha=0.7, s=10, marker='x', color=zone_colors[zone], label=f'Detect - Zone {zone}')

    # Create a second y-axis for count values
    ax2 = ax.twinx()
    ax2.set_ylabel('Count', color='tab:red')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    # Plot count values for the zone
    ax2.scatter(zone_data['timestamp'], zone_data['count'], alpha=0.7, s=10, marker='^', color=zone_colors[zone], label=f'Count - Zone {zone}')

    # Format x-axis for time without year
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
    ax.set_title(f'Zone Data Over Time for Zone {zone}')

plt.xticks(rotation=45)
fig.tight_layout(rect=[0, 0.05, 1, 0.95], h_pad=5)

# Save the combined scatter plot
plt.savefig('all_zones_with_combined_scatter_plot.png')
plt.close()
