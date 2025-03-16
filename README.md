# GitHub Activity CLI

A simple command-line interface (CLI) tool to fetch and display a GitHub user's recent activity.

![GitHub Activity CLI Demo](demo.gif) *Example output (replace with a real demo GIF if available)*

## Features

- Fetch recent GitHub activity for any public user.
- Display events like pushes, issue actions, stars, forks, and more in a human-readable format.
- Gracefully handles errors (e.g., invalid username, API failures).
- No external dependencies (uses Python standard libraries).

## Prerequisites

- Python 3.x (tested with Python 3.6+)
- A GitHub account (to use the tool; no authentication required).

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/github-activity-cli.git
   cd github-activity-cli
2. Run the script directly:
     python github_activity_cli.py <username>

     No additional installation is required!

   Usage
Basic Usage
bash
Copy

python github_activity_cli.py <username>

Replace <username> with the GitHub username you want to query.
Example
bash
Copy

python github_activity_cli.py kamranahmedse

Sample Output
Copy

- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred torvalds/linux
- Forked octocat/Spoon-Knife to johndoe/Spoon-Knife

Supported Event Types

    PushEvent: Displays commit counts and repository.

    IssuesEvent: Shows issue actions (opened, closed, etc.).

    WatchEvent: Indicates a starred repository.

    ForkEvent: Highlights repository forks.

    Other events are displayed generically (e.g., "Performed PullRequestEvent on user/repo").

Error Handling

    Invalid username: Error: User 'nonexistentuser' not found.

    API failures: Error: GitHub API returned status code 500.

    Network issues: Error: Failed to connect to GitHub API.

Contributing

Contributions are welcome!

    Fork the repository.

    Create a branch for your feature/fix: git checkout -b feature-name.

    Commit your changes and push to the branch.

    Open a Pull Request.

Please ensure your code follows Python PEP8 conventions.
License

This project is licensed under the MIT License. See LICENSE.

Made with Python and ❤️.
GitHub API documentation: https://docs.github.com/en/rest
Copy


---

### Notes:
1. Replace `yourusername` in the installation URL with your actual GitHub username.
2. Add a `LICENSE` file if you choose a license other than MIT.
3. Include a `demo.gif` to show sample output (optional but recommended).
4. Customize the "Contributing" section based on your preferences.

