<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/RaylaKurosaki1503/Student_Information_System">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h1 align="center">Student Information System</h1>

  <p align="center">
    The main use of this project is to compute the grades for the past and current classes I have taken at my university and print them in an easy to read format.
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
				<li><a href="#installation">Installation</a></li>
			</ul>
		</li>
		<li><a href="#usage">Usage</a></li>
		<li><a href="#license">License</a></li>
	</ol>
</details>



<!-- ABOUT THE PROJECT -->
## About the Project
During my time at university, I wanted a way to compute my grades for the classes I was taking at the time and the classes I have already taken. While there is a system my university has for this, there is an upside for me making this project. The reason is because some professors (at the time I initially wanted to do this project) don't actually put in the grades in the university's system. I relied on the university's system to keep track of my grades so if the professors don't update my grade in the university's system, then I can't tell if I am doing well in class. This has became less of an issue as I continued to study at university but I wanted to create this project in the case that it would happen again in the future. On a somewhat related note, some professors don't compute my grade normally and this needs to be computed manually since my university does not take this into considereation. This program, however, does takes that into consideration for those specific classes.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- FEATURES -->
## Features
- [x] Prints out the student's grades for the current and previous semesters/terms.
- [x] Prints out the student's transcript (grades and GPAs).
- [ ] Check if the student has met their requirements to satisfy their degree(s).
- [x] Check if the student has met their requirements to satisfy their minor(s).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### DISCLAIMER
While computing the students' final grades is something all professors do, there are some professors may have different methods for computing the student's final grade. In my case, I had a handful of professors who had a differemt method of calculating my final grade so I had to manually code the professors' method of computing my final grade for those classes. Thus, this project is tailored towards me and this program MAY NOT work for you. 

### Installation
1. To start, you need to clone this repository to your desktop.
2. After you have created a copy of this project to your desktop, create a new python project using these existing files.
3. After creating the project, you will need to import some third-party modules/packages
	1. numpy
	2. openpyxl
4. Finally, make sure that the source folder (src) is marked as Sources Root.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
I have provided two Microsoft Excel Workbooks/Spreadsheets, [sis_example](src/data/sis_example.xlsx) and [sis_template](src/data/sis_template.xlsx). The purpose of [sis_example](src/data/sis_example.xlsx) is to not only see how the data is organized and formatted, but to also see the output of the program when using that as the file to parse through. The [sis_template](src/data/sis_template.xlsx) file is a blank version of the example fie so a user can record their data. Please make sure to rename the file from "sis_template.xlsx" to "sis.xlsx" and move that file to the data directory.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License
This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE.txt) for license rights and limitations.

<p align="right">(<a href="#top">back to top</a>)</p>
