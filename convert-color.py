import subprocess
from tkinter import Tk
from pathlib import Path

#! Add extra path to your file
path = Path.cwd()
svg_files = path / 'svg'

file_content = ''
replace_color = '00C7BD'

def push():
    """
    Used to push to repo by executing these commands in the terminal:
    1. Run `git add .` - Stage all files
    2. Run `git commit -m <commit_msg>` - Commit with the provided message
    3. Run `git push` - Push to repo
    """
    def run(*args):
        return subprocess.check_call(['git'] + list(args))

    commit_msg = 'Change SVG color'
    run('add', '.')
    run('commit', '-m', commit_msg)
    run('push')

def change_svg_file():
    """
    Used to change color of each svg
    """

    # Iterate each file in the directory
    for svg in svg_files.iterdir():

        # Open a file and retrieve its content
        with open(svg, 'r') as file:
            file_content = file.read()
            
            # Change current color to `replace_color`
            file_content = file_content.replace('F58C6E', replace_color)

            file.close()

        # Write the new content to the file
        with open(svg, 'w') as file:
            file.write(file_content)
            file.close()

def main():
    change_svg_file()
    push()

# run the program
main()