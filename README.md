# Saiv: Comprehensive Toolkit Manager


![Saiv runs](https://shareps.000webhostapp.com/SP/MS/render.php?code=saiv&text=Succsessful%20Runs#)

#### Introduction

Saiv is a highly flexible and feature-packed toolkit manager developed to make organizing, executing, and deploying scripts and tools easy in dynamic environments. For developers, system administrators, or enthusiasts managing several projects, Saiv brings in an amicable interface and enormous functionality for a more productive workflow.

#### Key Features

1. **Toolkit Management**

**Create a Toolkit**
- Begin by creating a new toolkit within which to develop a custom toolkit for your project. Saiv allows the definition of tools, their names, directories, and entry points—ensuring that all these parts are well integrated.

**Load and Manage Toolkits**
- Access existing toolkits easily. Saiv allows you to load and manage many saved XML files. Each of them can easily be configured, modified, or even further extended by new tools as necessary for your project.

2. **Tool Operations**

**Add and Remove Tools**
- Add new tools to your toolkit using the command line interface. Inform it of a tool's name, directory path, and entry point command to be able to add more abilities on an ad-hoc basis.
- Easily eliminates outdated or unwanted tools and hence keeps the structure of the toolkit clean and efficient.

**Executing Tools**
- Start any tool from the toolkit with simple, intuitive commands. Saiv can execute tools using launch arguments that are customizable, meaning that the execution of the tool could easily be suited for the needs of each project.

3. **Toolkit Construction**

**Building Toolkits**
- Build new toolkits on GHPM connection files or addresses. With Saiv, there is an easy way of adding a group of external scripts and resources inside one toolkit, allowing flexibility for any project.

4. **Export and Deployment**

**Export Toolkits**
- Export your current toolkit to be implemented across various environments. Saiv is intelligent enough to adjust file paths and entry points, ensuring that the integration and functionality will be available upon deployment.

**Copying Directories**
- Copy directories within toolkits easily. This is an excellent feature for maintaining project structure integrity or packaging up for deployment without breaking working configurations.

#### Installation

To get started with Saiv:

1. **Clone Repository**

Clone Saiv repository from GitHub:
```bash
git clone https://github.com/smoke-wolf/Saiv.git
cd Saiv
```

2. **Install Dependencies**

Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

3. **Run Saiv**

Launch Saiv from a terminal:
```bash
python saiv.py
```

#### Getting Started

Creating a New Toolkit

To create a new toolkit using Saiv, follow the steps:

1. Run Saiv by executing `python saiv.py` in your terminal.
2. Press Option 3 to create a new toolkit.
3. Follow the prompts for entering the name of each tool, its directory path, and its entry point command.
4. After everything is added, all your tools will save the toolkit as a build directory in an XML file.

##### Loading and Managing Toolkits

Managing already existing Toolkits with Saiv:

1. Choose toolkit 4 from the main menu.

2. Choose the toolkit listed.
3. Personalize the toolkit by editing tools (option 1), removing tools (option 2), or calling out for new tools (option 5) as needed.

##### Executing Tools

Run a tool in your loaded toolkit :

1. Run the tool by choosing option five from the main menu.

2. Select the tool from the options shown.

3. Add in any launch arguments necessary and watch Saiv execute your tool precisely.

##### Export Toolkits

Export your toolbox for deployment:

1. Go to the main menu and press option 8, which will export the currently active toolkit.

2. Continue following the prompts to specify the export destination.

3. Saiv dynamically configures paths and entry points, keeping your toolkit constant and deployment-ready.

#### Advanced Usage

##### Building Toolkits from External Sources

Saiv makes it easy to build toolkits from external sources:

1. Choose option six from the main menu to develop a GHPM toolkit.

2. Share the connection file for GHPM or provide the address, together with information about the toolkit.

3. Saiv processes data, making a new toolkit XML file in the `build` directory that can be used instantly.

##### Managing Copies of Directories

Efficiently handle directory copies in your toolkits.

1. Use the `copy_directories` function of Saiv to copy directories when needed.

2. Select directories for copying and destination folder.
3. Saiv manages the copy process with integrity of structure and content.

#### Example

```bash
python saiv.py
```

---
