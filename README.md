# Full Stack Python Data Dashboard

## Project Overview
This project is a dashboard web application developed for **Grazioso Salvare**. The dashboard leverages **MongoDB** for data storage and retrieval while utilizing the **Dash** framework for creating an interactive web interface. The core functionality includes the ability to perform CRUD operations on a MongoDB database and visualize data in a user-friendly manner.

## Required Functionality
The dashboard meets the following key requirements:
- **CRUD Operations**: Users can create, read, update, and delete data records from MongoDB using the `MongoCRUD.py` module.
- **Data Visualization**: The data stored in MongoDB can be viewed and analyzed through graphical representations created in the `ProjectTwoDashboard.ipynb` notebook, powered by **Pandas** and **Matplotlib**.

## Screenshots / Proof of Functionality
- Starting State of the Dashboard:
  - Water Rescue Radio Button Clicked
  - Mountain or Wilderness Rescue Radio Button Clicked
  - Disaster or Individual Tracking Button Clicked
  - Reset widget clicked resulting in the default dashboard

## Tools Used
### 1. MongoDB
MongoDB was used as the database for this project due to its scalability, flexibility, and ability to store large volumes of unstructured data. Its compatibility with Python through the **PyMongo** library makes it an ideal choice for projects requiring easy integration with Python-based web applications.
- **Rationale**: MongoDB’s document-based structure allows it to efficiently handle the data from the Austin Animal Center, which can have variable attributes. Additionally, it provides fast querying capabilities, enabling real-time interaction with the dashboard.

### 2. Python (PyMongo, Pandas, Matplotlib)
- **PyMongo**: Used to interface with MongoDB and handle the CRUD operations in the `MongoCRUD.py` module.
- **Pandas**: Used for data manipulation and analysis within the dashboard.
- **Matplotlib**: Used for plotting the data and generating visual representations in the dashboard.
- **Rationale**: Python provides a robust ecosystem of libraries that streamline database interactions, data manipulation, and visualization. PyMongo connects easily with MongoDB, while Pandas and Matplotlib are reliable for handling and visualizing data.

### 3. Dash Framework
The **Dash** framework was used to build the interactive web interface of the dashboard. It provides a way to combine Python, HTML, and CSS to create dynamic and responsive dashboards.
- **Rationale**: Dash is designed for building web applications with a focus on interactivity. Its integration with Python makes it a natural fit for projects where the backend (MongoDB) and the front end (dashboard) need to work seamlessly together.

## Project Workflow
### Steps Taken:
1. **Setting up MongoDB**:
   - Installed and configured MongoDB on the local machine.
   - Imported the dataset from the Austin Animal Center into the MongoDB database.
2. **Developing MongoCRUD.py**:
   - Created the `MongoCRUD.py` module to handle basic CRUD operations on the MongoDB database.
   - Ensured functions for inserting, reading, updating, and deleting records were functional.
3. **Building the Dashboard**:
   - Used the Dash framework to develop an interactive dashboard that interfaces with the MongoDB database via `MongoCRUD.py`.
   - Integrated data visualization using **Pandas** and **Matplotlib**.
4. **Testing the Dashboard**:
   - Tested the full functionality of the dashboard in `ProjectTwoDashboard.ipynb` using test data from MongoDB.
   - Verified CRUD operations and visualizations were working as expected.

## Challenges Encountered
### Formatting the Data:
Some of the data found within the Austin Animal Center CSV file was not compatible with the **Pandas** framework. Specifically, the ID column was filled with MongoDB objects that were unable to be read. The solution was to drop the ID from the list of objects.

### Image Processing:
Rendering the image in the dashboard proved to be a difficult task. I assume it was due to the way I was creating the path for the image. However, I found no proper solution for this issue.

## Conclusion
This dashboard successfully meets the requirements of the **Grazioso Salvare** project by providing a functional web interface to interact with MongoDB. The combination of **Python**, **MongoDB**, and the **Dash** framework enables users to efficiently manage and visualize data. The project demonstrates the powerful integration of a NoSQL database with a Python-based web application.


---

For my client/server development course, I was tasked with building a fullstack python webapp that utilitzed MongoDB, Python, Dash and Pandas.

How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?

To write maintainable, readable, and adaptable code, key principles such as modular design, clear documentation, descriptive naming, and consistent formatting are essential. In my work on the CRUD Python module, I successfully separated database logic from the dashboard, enabling reusability and easier maintenance. The module's straightforward, well-commented functions make it easy to understand and modify, while its flexibility allows it to be adapted for future projects or databases. This modular approach reduced code duplication, facilitated testing, and can be reused in other web applications, APIs, or cloud-based systems, making it a scalable and versatile tool.


How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?


As a computer scientist, I approach problems by breaking them down into manageable components and focusing on modularity, reusability, and scalability. For Grazioso Salvare’s database and dashboard requirements, I first identified the core functionality—CRUD operations—and designed a reusable module that could be easily integrated with the dashboard. This approach ensured that the database interaction was cleanly separated from the user interface, allowing for easier testing and maintenance. Compared to previous assignments, this project required a deeper integration of frontend and backend technologies, demanding more attention to how data flows between the database and the dashboard. In the future, I would continue to prioritize modular design while employing techniques like efficient database indexing, cloud integration, and API development to create scalable, adaptable databases that meet diverse client needs.

What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

Computer scientists solve complex problems by designing, developing, and optimizing software and systems that enable efficient data processing, automation, and decision-making. This work matters because it powers the technology that drives innovation, improves productivity, and enables businesses to operate more effectively. In a project like the one for Grazioso Salvare, my work helps by streamlining their data management through a well-designed CRUD module and an intuitive dashboard. This allows them to easily track, update, and analyze data, ultimately improving their decision-making processes and operational efficiency. By automating and visualizing data, companies can save time, reduce errors, and focus on their core mission, making their work more impactful and scalable.
