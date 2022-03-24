<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/RaylaKurosaki1503/Student_Information_System">
    <img src="images/logo.png" alt="Logo" width="100" height="100">
  </a>

<h1 align="center">Student Information System</h1>

  <p align="center">
    The main use of this project is to compute the grades for the past and current classes I have taken at my university and print them in an easy-to-read format.
    <br />
    <a href="https://github.com/RaylaKurosaki1503/Student_Information_System"><strong>Explore the docs »</strong></a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
	<summary>Table of Contents</summary>
	<ol>
		<li><a href="#about-the-project">About the Project</a></li>
		<li><a href="#features">Features</a></li>
		<li><a href="#getting-started">Getting Started</a>
			<ul>
				<li><a href="#disclaimer">DISCLAIMER</a></li>
				<li><a href="#prerequisites">Prerequisites</a></li>
				<li><a href="#installation">Installation</a></li>
			</ul>
		</li>
		<li><a href="#usage">Usage</a></li>
		<li><a href="#license">License</a></li>
	</ol>
</details>



<!-- ABOUT THE PROJECT -->
## About the Project
During my time at university, I wanted a way to compute my grades for the classes I was taking at the time and the classes I have already taken. While there is a system my university has for this, there is an upside for me making this project. The reason is that some professors (at the time I initially wanted to do this project) don't actually put in the grades in the university's system. I relied on the university's system to keep track of my grades so if the professors don't update my grade in the university's system, then I can't tell if I am doing well in class. This has become less of an issue as I continued to study at university, but I wanted to create this project in the case that it would happen again in the future. On a somewhat related note, some professors don't compute my grade normally and this needs to be computed manually since my university does not take this into consideration. This program, however, does take that into consideration for those specific classes.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- FEATURES -->
## Features
- [x] Prints out the student's past and current grades in a tabular format onto a text file.
- [x] Prints the student's transcript onto a Microsoft Excel Workbook file in a pretty and easy-to-read format.
- [ ] Prints the student's transcript onto a PDF file in a pretty and easy-to-read format.
- [x] Computes the GPA of all the student's minors (if any).
- [ ] Computes the GPA of all the student's majors.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### DISCLAIMER
While computing the students' final grades is something all professors do, there are some professors may have different methods for computing the student's final grade. In my case, I had a handful of professors who had a different method of calculating my final grade. Thus, I had to manually code the professors' method of computing my final grade for those classes. As a result, this project is tailored towards me. If you want to try and modify this project to fit your needs, then I would recommend learning how to code in python.


### Prerequisites
1. Must have [Python 3.10+](https://www.python.org/downloads/) installed.
2. Must have some knowledge programming in Python (in order to modify the project to tailor your needs).

### Installation
The following are instructions I would give to other experienced programmers. If you don't understand a specific step, I provided more clear instructions for each step. However, it will be assumed that your IDE of choice is [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows).
1. Clone this repository to your machine.
   1. Download the project to your PC/laptop. Then extract the ZIP file to your PC/laptop.
2. Create a new python 3.10 project using this project as the base.
   1. To do this in PyCharm, create a new project. Then set the location to the location where you extracted my project from. Afterwards, make sure to select the "Create from Existing Resources" option.
3. After creating the project, you will need to import the third-party modules [numpy](https://numpy.org/) and [openpyxl](https://openpyxl.readthedocs.io/en/stable/).
   1. To do this in PyCharm, go to the file [excel.py](src/__utils__/excel.py). Go to the import statements and click Alt+Enter. Then click Enter once more. This will import the module openpyxl. Do the same with the file [pretty_print.py](src/__utils__/pretty_print.py) to import the module numpy.
4. Finally, make sure that the source folder (src) is marked as Sources Root.
   1. To do this in PyCharm, right-click on the folder "src". Then hover over the option "Mark Directory as". Finally, pick the option "Sources Root" (the blue folder).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
I have provided two Microsoft Excel Workbooks, [sis_example.xlsx](data/sis_example.xlsx) and [sis_template.xlsx](data/sis_template.xlsx). The purpose of [sis_example.xlsx](data/sis_example.xlsx) is to not only see how the data is organized and formatted, but to also see the output of the program when using that as the file to parse through. The [sis_template.xlsx](data/sis_template.xlsx) file is a blank version of [sis_example.xlsx](data/sis_example.xlsx) so a user can record their data. Please make sure to rename the file from "sis_template.xlsx" to "sis.xlsx".

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License
This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE.txt) for license rights and limitations.

<p align="right">(<a href="#top">back to top</a>)</p>
