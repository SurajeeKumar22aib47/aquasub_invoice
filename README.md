# Automated Invoice Extraction and Management

## Overview

The **Automated Invoice Extraction and Management** system leverages **Python**, **OCR**, and **Large Language Models (LLMs)** to accurately extract and classify invoice data. The system efficiently processes invoices, extracts key information (such as seller, buyer, total amount, tax), and stores it securely in an **MS SQL** database. The solution integrates **real-time data management** and **secure transaction handling** for a seamless and scalable invoice management system.

## Technologies Used

- **Python** – Core programming language for data extraction and logic.
- **OCR** – Optical Character Recognition for text extraction from invoices.
- **LLMs** – Large Language Models (like GPT, T5) for **Entity Recognition (NER)** and classification.
- **HTML, CSS, JavaScript** – For creating the dynamic web interface.
- **MS SQL** – Database for storing extracted invoice data securely.
- **MySQL** – For transaction processing, integrated using **JDBC**.
- **Flask/Django** – Web framework for creating the backend and user interface.

## Features

- **Invoice Data Extraction**: Automatically extract key fields such as seller, buyer, description, total amount, tax, and others from invoice documents.
- **Real-Time Data Processing**: Seamless upload and processing of invoice files (PDF, DOCX, etc.).
- **Secure Data Storage**: Integration with **MS SQL** for secure and scalable storage of extracted data.
- **Transaction Processing**: Interaction with a **MySQL** database for secure transaction handling.
- **User Interface**: Dynamic and user-friendly interface built using **HTML, CSS**, and **JavaScript** for smooth interaction.

## Installation

### Requirements

- Python 3.7+
- MS SQL or MySQL database
- Required Python libraries (listed below)

### Steps to Install

1. Clone this repository:

    ```bash
    git clone https://github.com/SurajeeKumar22aib47/Automated-Invoice-Extraction.git
    ```

2. Navigate into the project directory:

    ```bash
    cd Automated-Invoice-Extraction
    ```

3. Install required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your database:
    - Ensure that **MS SQL** or **MySQL** is properly set up.
    - Create a database and update the database credentials in `config.py`.

5. Run the application:

    ```bash
    python app.py
    ```

6. Access the application through `http://localhost:5000` in your web browser.

## How It Works

1. **Invoice Upload**: Users can upload invoices (PDF, DOCX) via the web interface.
2. **Data Extraction**: The system uses **OCR** to extract text and **LLMs** for entity recognition (NER).
3. **Data Classification**: Extracted data is categorized into fields like **seller**, **buyer**, **total amount**, **tax**, etc.
4. **Storage**: The processed data is stored securely in the **MS SQL** database.
5. **Transaction Processing**: The system handles transactions using **MySQL**, ensuring reliable operations.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any queries or suggestions, feel free to reach out:

- **Email**: sksurajee1245@gmail.com
- **LinkedIn**: [Surajee Kumar](https://www.linkedin.com/in/surajee-kumar-853909256)
- **Website**: [Surajee Kumar S](https://surajee-kumar-portfolio.netlify.app/)

