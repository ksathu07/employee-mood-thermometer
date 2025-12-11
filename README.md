# Employee Mood Thermometer (Pulse Tracker)

A full-stack web application that captures daily employee mood check-ins and converts them into useful dashboards for HR and managers. 

## 1. Features

- Simple daily mood check-in (e.g., Happy, Neutral, Stressed, Sad). 
- Secure storage of mood entries with date and time. 
- Team/manager dashboard with mood summary and recent entries.  
- Role-based access for employees and admins (HR/managers).  

## 2. Tech Stack

- **Frontend:** HTML, CSS, JavaScript. 
- **Backend:** Node.js / Express.  
- **Database:** MySQL or MongoDB for storing users and mood logs.   



## 3. Project Structure


analyse-mood-tracker/
  templates/
    index.html
    ...
  database/
    schema.sql
  README.md




## 4. Setup Instructions

1. Clone or unzip the project.  
2. Import `database/schema.sql` into your database (MySQL/Mongo script etc.).  
3. Open `templates/index.html` in a browser or run your frontend dev server. 
4. Run  `Python wsgi.py` in your terminal

## 5. How to Use

- Employees open the mood check-in page and select today’s mood.  
- Data is saved in the database and reflected in the dashboard. 
- HR/managers log in to the dashboard to see mood counts, trends and recent entries. 

## 6. Future Improvements

- Add email/OTP login for employees.  
- Add AI-based insights or alerts for continuous low mood trends. 
- Integrate with HR tools (attendance, project management, etc.).  

## 7. Credits

Project by **Sathursan Kamalanathan** as part of industrial training at **SarlaYash Learning Solutions LLP**. 