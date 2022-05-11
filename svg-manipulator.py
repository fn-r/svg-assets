import re
import subprocess
from pathlib import Path

path = Path.cwd()
svg_files = path / 'svg'

file_content = ''
svg_current_fill_color = '#00C7BD'

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

def change_svg_properties(svg_properties):
    """
    Used to change properties value of each svg
    """

    # Iterate each file in the directory
    for svg in svg_files.iterdir():

        # Open a file and retrieve its content
        with open(svg, 'r') as file:
            file_content = file.read()
            file.close()

            # Change width
            current_width = (re.findall('width=".*"', file_content)[0].split(' ')[0])
            file_content = file_content.replace(current_width, f"width=\"{svg_properties['width']}\"")

            # Change height
            current_height = (re.findall('height=".*"', file_content)[0].split(' ')[0])
            file_content = file_content.replace(current_height, f"height=\"{svg_properties['height']}\"")

            # Change fill color
            current_height = (re.findall('fill=".*"', file_content)[0].split(' ')[0])
            file_content = file_content.replace(current_height, f"fill=\"{svg_properties['fill']}\"")

        # Write the new content to the file
        with open(svg, 'w') as file:
            file.write(file_content)
            file.close()

def prompt():
    """
    Used to prompt user for new properties values
    """

    svg_properties = {
        'fill': '',
        'width': '',
        'height': ''
    }

    new_width = input('New width: ')
    new_height = input('New height: ')
    new_color = input('New fill color: ')

    svg_properties['fill'] = new_color
    svg_properties['width'] = new_width
    svg_properties['height'] = new_height

    return svg_properties

def main():
    new_values = prompt()
    change_svg_properties(new_values)
    push()

# run the program
main()