# Student Information System
The main use of this project is to compute the grades for the past and current classes I have taken at my university and print them in an easy to read format.

## Description
During my time at university, I wanted a way to compute my grades for the classes I was taking at the time and the classes I have already taken. While there is a system my university has for this, there is an upside for me making this project. The reason is because some professors (at the time I initially wanted to do this project) don't actually put in the grades in the university's system. I relied on the university's system to keep track of my grades so if the professors don't update my grade in the university's system, then I can't tell if I am doing well in class. This has became less of an issue as I continued to study at university but I wanted to create this project in the case that it would happen again in the future. On a somewhat related note, some professors don't compute my grade normally and this needs to be computed manually since my university does not take this into considereation. This program, however, does takes that into consideration for those specific classes.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Features
- [x] Prints out the student's grades for the current and previous semesters/terms.
- [ ] Prints out the student's transcript (grades and GPAs).
- [ ] Check if the student has met their requirements to satisfy their degree(s).
- [ ] Check if the student has met their requirements to satisfy their minor(s).

## Installation
While printing out the grades is a universal feature for this project, some professors may have different methods for computing the student's final grade. Thus, this project is tailored towards me and I will not be providing an installation guide.

For experienced python programmers, you can simply clone the repository and run it in your preferred IDE. All files have documentation and most files have comments everywhere to explain how the algorithm works. With your python knowledge, you should be able to modify the code and personalize it to fit your needs.

## Usage
I have provided two Microsoft Excel Workbooks/Spreadsheets, [sis_example](data/sis_example.xlsx) and [sis_template](data/sis_template.xlsx). The purpose of [sis_example](data/sis_example.xlsx) is to not only see how the data is organized and formatted, but to also see the output of the program when using that as the file to parse through. The [sis_template](data/sis_template.xlsx) file is a blank version of the example fie so a user can record their data. Please make sure to rename the file from "sis_template.xlsx" to "sis.xlsx" adn move that file to the data directory.

## License
This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE.txt) for license rights and limitations.
