import csv
import sys

def count_actions(csv_filename):
    action_count = 0
    last_rescuebot_action = None
    last_charlie_action = None
    
    with open(csv_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            rescuebot_action = row.get('rescuebot_action', '').strip()
            charlie_action = row.get('charlie_action', '').strip()
            
            if rescuebot_action and "move" not in rescuebot_action.lower():
                if rescuebot_action != last_rescuebot_action:
                    action_count += 1
                last_rescuebot_action = rescuebot_action
            else:
                last_rescuebot_action = None
            
            if charlie_action and "move" not in charlie_action.lower():
                if charlie_action != last_charlie_action:
                    action_count += 1
                last_charlie_action = charlie_action
            else:
                last_charlie_action = None
    return action_count

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("python collect_data_logs.py <csv_file>")
        sys.exit(1)
    csv_file = sys.argv[1]
    total_actions = count_actions(csv_file)
    print(f"Total Actions: {total_actions}")