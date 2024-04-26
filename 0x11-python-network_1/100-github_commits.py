
#!/usr/bin/python3
"""
Module to use the information after access github
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def main(argv):
    """
    Function that list 10 commits
    """

    def p_commits(i, l_commit):
        """
        List the commits, less than 10 commits
        """
        sha = l_commit[i].get('sha')
        commit = l_commit[i].get('commit')
        author = commit.get('author')
        name = author.get('name')
        print('{}: {}'.format(sha, name))

    repo = argv[1]
    owner = argv[2]
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get('https://api.github.com/repos/' + owner +
                            '/' + repo + '/commits', headers=headers)
    l_commit = response.json()
    size = len(l_commit)
    if size < 9:
        for i in range(0, size):
            p_commits(i, l_commit)
    else:
        for i in range(0, 10):
            p_commits(i, l_commit)


if __name__ == "__main__":
    main(argv)
