# Job_Tracker

A web application to help manage and track job applications, including application status updates, job descriptions, and CV analysis. Built with Flask, Bootstrap 4.5.2, and Chart.js.

# Features

- Add Job Applications: Input details such as company, position, date applied, status, and job description.
- View Job Applications: Display a list of all job applications with options to update statuses and view details.
- Application Status Chart: Visualize application statuses with a bar chart.
- CV Upload & Analysis: Upload and analyze your CV to get an acceptance percentage based on job descriptions and CV content.
- Responsive Design: Mobile-friendly with a hamburger menu for navigation.

# Technologies Used

- Backend: Flask
- Frontend: HTML, CSS, JavaScript
- UI Framework: Bootstrap 4.5.2
- Charting Library: Chart.js
- Database: CSV files for data storage

# Installation

- Clone the Repository

```bash
git clone https://github.com/hemangsharma/job-application-tracker.git
```
```bash
cd job-application-tracker
```

- Set Up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

- Install Dependencies
```bash
pip install -r requirements.txt
```

- Run the Application
```bash
flask run
```

# Configuration

- CSV Data Storage: Data is stored in data/applications.csv. Make sure this file is properly set up to store application details.
- CV Analysis: Place your CV PDF in the static folder and ensure the analysis script can read it.

# Usage

- Add Job Applications: Navigate to /add to input new job application details.
- View Job Applications: Navigate to /view to see and update the list of applications.
- View Application Status Chart: Navigate to /charts to see a visual representation of application statuses.

# License

This project is licensed under the MIT License. See the LICENSE file for details.