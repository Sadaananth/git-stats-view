import plotext as plt
import subprocess
import re
import sys

def parse_commit_stats(commit_string):
    # Define regex patterns to extract the relevant data
    pattern = r"(insertions|deletions|files|commits|lines changed):\s*(\d+)"
    
    # Dictionary to hold the parsed data
    stats = {}

    # Find all matches using regex
    matches = re.findall(pattern, commit_string)
    
    # Store matches in a dictionary
    for match in matches:
        stat_name, value = match
        stats[stat_name] = int(value)
    
    return stats

def plot_commit_stats(stats):
    labels=list(stats.keys())
    values=list(stats.values())
    plt.bar(labels, values),

    # Display the plot in the console
    plt.show()


# Path to the Bash script
script_path = './get_stats.sh'

# Run the script
result = subprocess.run(['bash', script_path], capture_output=True, text=True)

# Print the output of the script
print("Output:")
print(result.stdout)

# Optionally, print any error if the script fails
if result.stderr:
    print("Error:")
    print(result.stderr)

stats = parse_commit_stats(result.stdout)
plot_commit_stats(stats)
