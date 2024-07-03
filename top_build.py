import os
import xml.etree.ElementTree as ET
from xml.dom import minidom
from colorama import Fore, Style, init

init(autoreset=True)


def get_interpreter(file):
    ext = os.path.splitext(file)[1].lower()
    if ext == '.py':
        return 'python'
    elif ext == '.sh':
        return 'bash'
    elif ext == '.js':
        return 'node'
    elif ext == '.pl':
        return 'perl'
    elif ext == '.rb':
        return 'ruby'
    else:
        return 'none'


def get_tool_name():
    return input("Enter the name of the tool: ")


def get_entrypoint(file, interpreter):
    if interpreter == 'none':
        return file
    else:
        return f"{interpreter} {file}"


def get_top_level_files(directory):
    files = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            files.append(filepath)
    return files


def prettify(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")


def display_files(files):
    print(f"{Fore.YELLOW}{Style.BRIGHT}Index\tFile Path")
    print(f"{Fore.YELLOW}{Style.BRIGHT}-----\t---------")
    for idx, file in enumerate(files):
        print(f"{Fore.CYAN}{idx}\t{Fore.GREEN}{file.split('/')[-1]}")


def create_xml_structure(directory):
    toolkit = ET.Element('toolkit')

    files = get_top_level_files(directory)

    display_files(files)
    indices = input(f"{Fore.MAGENTA}Enter the indices of the files to include (comma separated): ").strip().split(',')

    tool_id = 1
    for index in indices:
        try:
            index = int(index)
            file = files[index]
        except (ValueError, IndexError):
            print(f"{Fore.RED}Invalid index: {index}")
            continue

        tool = ET.SubElement(toolkit, f'tool{tool_id}')

        # Adding banner with filename
        filename = os.path.basename(file)
        banner = f"===== {filename} ====="
        print('\n'*50)
        print(banner)

        ET.SubElement(tool, 'id').text = str(tool_id)

        tool_name = get_tool_name()
        ET.SubElement(tool, 'toolName').text = tool_name

        ET.SubElement(tool, 'dir').text = os.path.dirname(file)

        interpreter = get_interpreter(file)
        entrypoint = get_entrypoint(file, interpreter)
        ET.SubElement(tool, 'entrypoint').text = entrypoint

        tool_id += 1

    xml_str = prettify(toolkit)
    nm = input('Enter the toolkit name: ')
    with open(f'build/{nm}.xml', 'w') as f:
        f.write(xml_str)


if __name__ == '__main__':
    directory = input("Enter the directory path: ").strip()
    create_xml_structure(directory)
    print(f"{Fore.YELLOW}XML structure created and saved.")
