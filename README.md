# **SheetCounterApp**

## **Overview**
*This repository contains a* **Flask-based web application** *designed to automate the counting of sheet stacks in a manufacturing plant. The application processes images of sheet stacks and provides an accurate count of the sheets.*

## **Technologies Used**
- **Python:** *The primary programming language used for development.*
- **Flask:** *A lightweight web framework used to create the web application.*
- **OpenCV:** *Library used for image processing and analysis.*
- **NumPy:** *Utilized for numerical operations in image processing.*

## **Features**
- **Image Upload:** *Users can upload images of sheet stacks through a user-friendly web interface.*
- **Automatic Counting:** *The application processes the uploaded image to estimate the number of sheets.*
- **Error Handling:** *Provides feedback and error messages if the image processing fails.*
- **Real-time Results:** *Displays the estimated sheet count immediately after processing the image.*

## **Future Enhancements**
- **Deep Learning Integration:** *Implement convolutional neural networks (CNNs) for more robust and accurate sheet counting.*
- **Enhanced User Interface:** *Improve the web interface for better user experience.*
- **Support for More Formats:** *Add support for various image formats and larger image sizes.*

## **Setup and Installation**
*To set up and run the application, follow these steps:*

1. **Clone the Repository**
   ```bash
   git clone <repository_link>
   cd <repository_name>

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install Required Libraries**
   Create a requirements.txt file in the root directory with the following content:

   ```bash
   Flask==2.0.1
   opencv-python==4.5.3.56
   numpy==1.21.1

5. **Install the dependencies using:**
   ```bash
    pip install -r requirements.txt

7. **Run the Application**
   ```bash
    python sheet_counter.py

The application will be accessible at http://127.0.0.1:5000/.

##**Issues and Troubleshooting**

LF/CRLF Warning: A warning about LF being replaced by CRLF is related to line endings in text files. This does not affect the functionality of the application.

##**Video Demonstration**
Watch the one-minute video demonstrating the application in action:

Video Demonstration Link 
https://www.loom.com/share/85952c3ca68048afb9eb8eec7aa694d2?sid=9deb823e-c82f-406b-9e02-7ef7384d1bcb

Contact
For any queries or feedback, please contact Harshavardhan at harshavardhanmanavalan@gmail.com.



