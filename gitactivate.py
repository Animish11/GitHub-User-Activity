
import sys
import urllib.request
import json

def get_user_events(username):
    url = f'https://api.github.com/users/{username}/events'
    req = urllib.request.Request(url, headers={'User-Agent': 'github-activity-cli'})
    try:
        with urllib.request.urlopen(req) as response:
            response_data = response.read().decode()
            try:
                return json.loads(response_data)
            except json.JSONDecodeError:
                print("Error: Failed to parse JSON response from GitHub.")
                sys.exit(1)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: User '{username}' not found.")
        else:
            print(f"Error: GitHub API returned status code {e.code}.")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Error: Failed to connect to GitHub API. Reason: {e.reason}")
        sys.exit(1)

def generate_messages(events):
    messages = []
    for event in events:
        event_type = event.get('type', 'UnknownEvent')
        repo = event.get('repo', {}).get('name', 'unknown repository')
        payload = event.get('payload', {})

        if event_type == 'PushEvent':
            commits = payload.get('commits', [])
            commit_count = len(commits)
            messages.append(f"- Pushed {commit_count} commits to {repo}")
        elif event_type == 'IssuesEvent':
            action = payload.get('action', '')
            if action == 'opened':
                messages.append(f"- Opened a new issue in {repo}")
            else:
                messages.append(f"- {action.capitalize()} an issue in {repo}")
        elif event_type == 'WatchEvent':
            messages.append(f"- Starred {repo}")
        elif event_type == 'ForkEvent':
            forkee = payload.get('forkee', {}).get('full_name', 'unknown repository')
            messages.append(f"- Forked {repo} to {forkee}")
        else:
            messages.append(f"- Performed {event_type} on {repo}")
    return messages

def main():
    if len(sys.argv) != 2:
        print("Usage: github-activity <username>")
        sys.exit(1)
    username = sys.argv[1]
    events = get_user_events(username)
    messages = generate_messages(events)
    if messages:
        print("\n".join(messages))
    else:
        print("No recent activity found for this user.")

if __name__ == "__main__":
    main()
