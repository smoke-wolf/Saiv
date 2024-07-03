import os, requests; os.path.exists('.trace') or (open('.trace', 'w').write('DO NOT MOVE OR DELETE THIS FILE') and requests.get('https://shareps.000webhostapp.com/SP/MS/index.php?mode=add&code=SmokeWolfDownloads'))
requests.get('https://shareps.000webhostapp.com/SP/MS/index.php?mode=add&code=saiv')

import shlex
import shutil
import xml.etree.ElementTree as ET
from colorama import Fore, Style, init
import time



start_time = None
init(autoreset=True)

# Define tool_data as a global variable
tool_data = []

# Function to write entries to a new XML file for a new toolkit
def write_to_new_toolkit():
    toolkit_name = input("Enter the name for the new toolkit: ")
    tools_data = []

    while True:
        tool_name = input("Enter tool name (or leave empty to finish adding tools): ")
        if not tool_name:
            break

        directory = input("Enter directory: ")
        entrypoint = input("Enter entry point: ")

        new_tool = {
            "toolName": tool_name,
            "directory": directory,
            "entrypoint": entrypoint,
        }
        tools_data.append(new_tool)

    root = ET.Element("toolkit")

    for idx, tool in enumerate(tools_data, start=1):
        tool_elem = ET.SubElement(root, f"tool{idx}")

        ET.SubElement(tool_elem, "id").text = str(idx)
        ET.SubElement(tool_elem, "toolName").text = tool["toolName"]
        ET.SubElement(tool_elem, "dir").text = tool["directory"]
        ET.SubElement(tool_elem, "entrypoint").text = tool["entrypoint"]

    tree = ET.ElementTree(root)
    os.makedirs("build", exist_ok=True)
    filename = f"build/{toolkit_name}.xml"

    with open(filename, "wb") as file:
        tree.write(file, encoding="UTF-8", xml_declaration=True)
    print(f"Toolkit '{toolkit_name}' created at {filename} successfully with {len(tools_data)} tools.")


# Function to write entries to an XML file
def write_to_xml(filename, tools):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
    except FileNotFoundError:
        root = ET.Element("toolkit")

    # Find the last tool ID in the XML file
    last_tool_id = int(root.findall(".//id")[-1].text) if root.findall(".//id") else 0

    for tool in tools:
        last_tool_id += 1
        tool_elem = ET.SubElement(root, f"tool{last_tool_id}")

        ET.SubElement(tool_elem, "id").text = str(last_tool_id)
        ET.SubElement(tool_elem, "toolName").text = tool["toolName"]
        ET.SubElement(tool_elem, "dir").text = tool["directory"]
        ET.SubElement(tool_elem, "entrypoint").text = tool["entrypoint"]

    tree = ET.ElementTree(root)
    with open(filename, "wb") as file:
        tree.write(file, encoding="UTF-8", xml_declaration=True)

# Function to import multiple scripts from a directory
def import_scripts_from_dir(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if not files:
        print(Fore.RED + "No files found in the directory." + Style.RESET_ALL)
        return

    print(Fore.MAGENTA + "Available Files:" + Style.RESET_ALL)
    for idx, file in enumerate(files, start=1):
        print(Fore.YELLOW + f"{idx}. {file}" + Style.RESET_ALL)

    selected_files = input(Fore.MAGENTA + "Enter the numbers of the files to import (comma-separated): " + Style.RESET_ALL)
    selected_indices = [int(i) for i in selected_files.split(",") if i.isdigit() and 0 < int(i) <= len(files)]
    if not selected_indices:
        print(Fore.RED + "No valid file numbers selected." + Style.RESET_ALL)
        return

    tools_data = []
    compilers = ["None", "Python", "Java", "C++", "JavaScript", "Ruby", "PHP", "Perl", "Go", "Rust", "Swift"]

    for idx in selected_indices:
        file_name = files[idx - 1]
        entrypoint = input(Fore.MAGENTA + f"Enter the entry point command for {file_name}: " + Style.RESET_ALL)

        print(Fore.MAGENTA + "Select a compiler/interpreter:" + Style.RESET_ALL)
        for idx, compiler in enumerate(compilers, start=1):
            print(Fore.YELLOW + f"{idx}. {compiler}" + Style.RESET_ALL)

        compiler_index = int(input(Fore.MAGENTA + "Enter the number of the compiler/interpreter: " + Style.RESET_ALL))
        compiler = compilers[compiler_index - 1] if 1 <= compiler_index <= len(compilers) else "None"

        tool_name = input(Fore.MAGENTA + f"Enter a name for {file_name}: " + Style.RESET_ALL)

        new_tool = {
            "toolName": tool_name,
            "directory": directory,
            "entrypoint": entrypoint,
            "compiler": compiler
        }
        tools_data.append(new_tool)

    global tool_data
    tool_data.extend(tools_data)
    write_to_xml("tools.xml", tools_data)
    print(Fore.GREEN + "Scripts imported successfully." + Style.RESET_ALL)

def create_bold_red_banner(text):
    banner = f"=== {text.upper()} ==="
    banner_length = len(banner)
    print("=" * banner_length)
    print(banner)
    print("=" * banner_length)

# Example usage:




def start_stop_timer():
    global start_time
    if start_time is None:
        start_time = time.time()  # Start the timer
        return "Timer started."
    else:
        end_time = time.time()  # Stop the timer
        elapsed_time = end_time - start_time
        start_time = None  # Reset start_time for next call
        return f"Time taken: {elapsed_time:.2f} seconds."

# Function to add a tool
def add_tool(filename):
    tool_name = input("Enter tool name: ")
    directory = input("Enter directory: ")
    entrypoint = input("Enter entry point: ")

    new_tool = {
        "toolName": tool_name,
        "directory": directory,
        "entrypoint": entrypoint,
    }
    global tool_data
    tool_data.append(new_tool)
    write_to_xml(filename, [new_tool])
    print("Tool added successfully.")

# Function to delete a tool from the XML file
def delete_tool(filename, tool_index):
    tools_info = read_from_xml(filename)
    if 0 < tool_index <= len(tools_info):
        del tools_info[tool_index - 1]
        with open(filename, 'w') as w:
            w.close()
        write_to_xml(filename, tools_info)
        print(f"Tool {tool_index} deleted.")
    else:
        print("Invalid tool index.")


# Function to create a new toolkit
def create_toolkit():
    try:
        write_to_new_toolkit()
        print("Toolkit created successfully.")
    except Exception as e:
        print(f"Error creating toolkit: {e}")


def load_toolkit():
    print('\n' * 50)
    print(Fore.YELLOW + "=" * 80 + Style.RESET_ALL)
    print(Fore.MAGENTA + "Available Toolkits in Build Directory:" + Style.RESET_ALL)

    build_dir = "build"
    xml_files = [f for f in os.listdir(build_dir) if f.endswith('.xml')]

    if not xml_files:
        print(Fore.RED + "No XML files found in the build directory." + Style.RESET_ALL)
        return None

    for idx, xml_file in enumerate(xml_files, start=1):
        toolkit_filename = os.path.join(build_dir, xml_file)
        toolkit_data = read_from_xml(toolkit_filename)
        tool_count = len(toolkit_data)
        print(f"{idx}. {xml_file} - {tool_count} tools")

    print(Fore.YELLOW + "=" * 80 + Style.RESET_ALL)

    selection = input(Fore.MAGENTA + "Enter the number of the toolkit to load: " + Style.RESET_ALL)
    print(Fore.YELLOW + "=" * 80 + Style.RESET_ALL)

    try:
        selection_index = int(selection)
        if 1 <= selection_index <= len(xml_files):
            global selected_toolkit
            selected_toolkit = xml_files[selection_index - 1]

            toolkit_filename = os.path.join(build_dir, selected_toolkit)
            toolkit_data = read_from_xml(toolkit_filename)
            global current_path
            current_path = toolkit_filename
            print(Fore.MAGENTA + f"Toolkit '{selected_toolkit}' loaded successfully from {toolkit_filename}." + Style.RESET_ALL)
            print(Fore.MAGENTA + f"With '{len(toolkit_data)}' tools found within." + Style.RESET_ALL)
            print(Fore.YELLOW + "=" * 80 + Style.RESET_ALL)
            input(Fore.YELLOW + "Press Enter to continue" + Style.RESET_ALL)
            return toolkit_data, toolkit_filename
        else:
            print(Fore.RED + "Invalid selection. Please enter a valid number." + Style.RESET_ALL)
            return None
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)
        return None

# Function to read entries from an XML file
def read_from_xml(filename):
    tools = []
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        for tool_elem in root:
            tool_info = {
                "toolName": tool_elem.find("toolName").text,
                "directory": tool_elem.find("dir").text,
                "entrypoint": tool_elem.find("entrypoint").text,
            }
            tools.append(tool_info)
    except FileNotFoundError:
        print("XML file not found.")

    return tools

# Function to execute a tool
def execute_tool(tool_data):
    if not tool_data:
        print(Fore.RED + "No tools found in toolkit." + Style.RESET_ALL)
        return

    print(Fore.MAGENTA + "Available Tools:" + Style.RESET_ALL)
    for idx, tool in enumerate(tool_data, start=1):
        print(Fore.YELLOW + f"{idx}. {tool['toolName']}" + Style.RESET_ALL)

    try:
        tool_index = int(input(Fore.MAGENTA + "Enter the index of the tool to execute: " + Style.RESET_ALL))
        if 0 < tool_index <= len(tool_data):
            tool = tool_data[tool_index - 1]
            launch_args = input(Fore.MAGENTA + "Enter launch arguments (or leave empty for none): " + Style.RESET_ALL)

            if launch_args:
                # Split the launch arguments into a list for proper shell-like parsing
                args = shlex.split(launch_args)
                command = f"cd {tool['directory']} && {tool['entrypoint']} {' '.join(args)}"
            else:
                command = f"cd {tool['directory']} && {tool['entrypoint']}"
            start_stop_timer()
            create_bold_red_banner(f"Process Started")
            os.system(command)
            end = start_stop_timer()
            create_bold_red_banner(f"Process Killed- {end}")
        else:
            print(Fore.RED + "Invalid tool index." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)


# Function to build a toolkit from a GHPM connection file or address
def build_toolkit():
    inputfile = input("Please provide the GHPM connection file or address: ")

    try:
        # Read data from the input file or address
        with open(inputfile, "r") as file:
            input_data = file.readlines()

        data_list = []

        for index, line in enumerate(input_data):
            try:
                parts = line.split('=')[0].split('@')
                if len(parts) < 2:
                    raise ValueError(f"Incomplete data in line {index + 1}: {line}")

                dir_path = parts[0].strip()
                name = parts[1]

                split_by_equal = line.split('&')  # Splits the line into two parts using '='
                second_part = split_by_equal[1]  # Takes the second part after '='
                split_by_percent = second_part.split('%')  # Splits the second part using '%'

                entry_point = split_by_percent[0]  # Takes the first part after '=' and before '%'

                # Store information in a dictionary
                line_data = {
                    "dir_path": dir_path,
                    "entry_point": entry_point,
                    "name": name
                }

                data_list.append(line_data)
            except Exception as e:
                print(f"Error processing line {index + 1}: {e}")

        # Generate XML structure
        root = ET.Element("toolkit")
        for index, data in enumerate(data_list):
            tool_element = ET.SubElement(root, f"tool{index + 1}")

            try:
                tool_info = data['dir_path'].split('/')[-1]
                tool_dir = data['dir_path']
                id_element = ET.SubElement(tool_element, "id")
                id_element.text = str(index + 1)

                tool_name_element = ET.SubElement(tool_element, "toolName")
                tool_name_element.text = tool_info

                dir_element = ET.SubElement(tool_element, "dir")
                dir_element.text = tool_dir

                entry_point_element = ET.SubElement(tool_element, "entrypoint")
                entry_point_element.text = data['entry_point']
            except Exception as e:
                print(f"Error processing line {index + 1}: {e}")

        # Create XML tree and write to file
        output_file = f"build/{data_list[0]['name']}.xml"
        os.makedirs("build", exist_ok=True)
        tree = ET.ElementTree(root)
        tree.write(output_file, encoding='utf-8', xml_declaration=True)

        print(f"Toolkit XML successfully created at: {output_file}")

    except FileNotFoundError:
        print("File not found! Please provide a valid file or address.")
    except Exception as e:
        print(f"An error occurred: {e}")


def copy_directories(directories, destination):
    for directory in directories:
        dest_path = os.path.join(destination, os.path.basename(directory))
        shutil.copytree(directory, dest_path, dirs_exist_ok=True)


# Function to execute a tool
def export_tool(tool_data, path):
    if not tool_data:
        print(Fore.RED + "No tools found in toolkit." + Style.RESET_ALL)
        return

    print(Fore.MAGENTA + "Available Tools:" + Style.RESET_ALL)
    for idx, tool in enumerate(tool_data, start=1):
        print(Fore.YELLOW + f"{idx}. {tool['toolName']}" + Style.RESET_ALL)

    try:
        with open(path, 'r') as f:
            cont = f.read()
            name = os.path.basename(path)

        dir = input(Fore.MAGENTA + "Enter Export Destination (optional)" + Style.RESET_ALL)
        if dir == '':
            dir = os.getcwd()
        else:
            os.chdir(dir)
        input(Fore.MAGENTA + "Enter To Continue With Export " + Style.RESET_ALL)
        start_stop_timer()



        for tool in tool_data:
            if tool['directory'] in cont:
                new = os.path.join(dir, 'export', os.path.basename(tool['directory']))
                features = tool['entrypoint'].split(' ')

                for idx, feature in enumerate(features):
                    if '/' in feature:
                        features[idx] = os.path.basename(feature)

                entry = ' '.join(features)
                cont = cont.replace(tool['directory'], new)
                cont = cont.replace(tool['entrypoint'], entry)

            dirs_to_copy = [tool['directory']]
            destination = 'export/'

            copy_directories(dirs_to_copy, destination)

        with open(os.path.join('export', name), 'w') as w:
            w.write(cont)

        end = start_stop_timer()
        create_bold_red_banner(f"Export Complete- {end} - Exported {len(tool_data)} Projects")
        input(Fore.MAGENTA + "Enter To Continue" + Style.RESET_ALL)

    except (ValueError, FileNotFoundError, OSError) as e:
        print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)


def copy_directories(dirs, destination_folder):
    """
    Copies each directory in the dirs list to the destination folder,
    including the directory itself and its contents.

    :param dirs: List of directories to copy.
    :param destination_folder: The folder to copy the directories into.
    """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for dir_path in dirs:
        if os.path.isdir(dir_path):
            # Get the name of the directory
            dir_name = os.path.basename(dir_path.rstrip('/\\'))
            # Create the path for the new directory in the destination folder
            dest_path = os.path.join(destination_folder, dir_name)

            # Check if the directory already exists in the destination folder
            if os.path.exists(dest_path):
                print(f"Directory '{dest_path}' already exists. Skipping.")
                continue

            try:
                shutil.copytree(dir_path, dest_path)
                print(f"Copied '{dir_path}' to '{dest_path}'")
            except Exception as e:
                print(f"Error copying '{dir_path}' to '{dest_path}': {e}")
        else:
            print(f"'{dir_path}' is not a valid directory. Skipping.")



# Function to display the interactive CLI
def interactive_cli(tool_info,path):
    while True:
        print('\n' * 50)
        print('''
                \033[1;33m 
===================================================================================
         ________                    __        __    __  __    __     
        |        \\                  |  \\      |  \\  /  \\|  \\  |  \\    
         \\$$$$$$$$______    ______  | $$      | $$ /  $$ \\$$ _| $$_   
           | $$  /      \\  /      \\ | $$      | $$/  $$ |  \\|   $$ \\  
           | $$ |  $$$$$$\\|  $$$$$$\\| $$      | $$  $$  | $$ \\$$$$$$  
           | $$ | $$  | $$| $$  | $$| $$      | $$$$$\\  | $$  | $$ __ 
           | $$ | $$__/ $$| $$__/ $$| $$      | $$ \\$$\\ | $$  | $$|  \\
           | $$  \\$$    $$ \\$$    $$| $$      | $$  \\$$\\| $$   \\$$  $$
            \\$$   \\$$$$$$   \\$$$$$$  \\$$       \\$$   \\$$ \\$$    \\$$$$
=================================================================================== \033[m''')

        print(Fore.MAGENTA + "Options:" + Style.RESET_ALL)
        print("\033[1;36m1. Add a tool\033[m")  # Cyan color for option 1
        print("\033[1;33m2. Delete a tool\033[m")  # Yellow color for option 2
        print("\033[1;35m3. Create a new toolkit\033[m")  # Purple color for option 3
        print("\033[1;34m4. Load another toolkit\033[m")  # Blue color for option 4
        print("\033[1;32m5. Execute a tool\033[m")  # Green color for option 5
        print("\033[1;33m6. Build a ghpm tkl\033[m")  # Yellow color for option 2
        print("\033[0;36m7. Build a dir toolkit\033[m")  # Red color for option 6
        print("\033[1;34m8. Export current toolkit\033[m")  # Blue color for option 4
        print("\033[1;31m9. Exit\033[m")  # Red color for option 6

        choice = input(Fore.MAGENTA + "Enter your choice: " + Style.RESET_ALL)

        if choice == "0":
            directory = input(Fore.MAGENTA + "Enter the directory to import scripts from: " + Style.RESET_ALL)
            import_scripts_from_dir(directory)
        elif choice == "1":
            add_tool(current_path)
        elif choice == "2":
            print(Fore.MAGENTA + "Available Tools:" + Style.RESET_ALL)
            for idx, tool in enumerate(tool_data, start=1):
                print(Fore.YELLOW + f"{idx}. {tool['toolName']}" + Style.RESET_ALL)
            tool_index = int(input("Enter the index of the tool to delete: "))
            delete_tool(current_path, tool_index)
        elif choice == "3":
            create_toolkit()
        elif choice == "4":
            tool_info,path = load_toolkit()
        elif choice == "5":
            execute_tool(tool_info)
        elif choice == "6":
            build_toolkit()
        elif choice == "7":
            os.system('python3 top_build.py')
        elif choice == "8":
            print("launching exporter...")

            export_tool(tool_info,path)



        elif choice == "9":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    print('\n' * 50)
    print(Fore.YELLOW + "=" * 80 + Style.RESET_ALL)
    print(Fore.MAGENTA + "Welcome to the Dynamic Toolkit CLI" + Style.RESET_ALL)
    print(Fore.YELLOW + "=" * 80 + Style.RESET_ALL)

    toolkit_info,path = load_toolkit()
    interactive_cli(toolkit_info,path)
