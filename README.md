# MedGuideAI with Appointment Scheduling & Emergency Routing


## Overview

MedGuideAI is an AI-powered healthcare assistant designed to provide information on various medical topics, book appointments with doctors, and provide emergency routes to nearby hospitals. The chatbot leverages **LangChain**, **Hugging Face Embeddings**, **Pinecone**, and **Google APIs** to enhance patient experience and streamline healthcare services.

## Features

- **Medical Information Retrieval**: Answers questions based on a dataset of medical information stored in PDF files.
- **Doctor Appointment Scheduling**: Integrates with Google Calendar to check doctor availability, schedule appointments, and send reminders.
- **Emergency Routing to Hospitals**: Uses Google Maps to find and provide routes to the nearest hospital in case of emergencies.
- **User-Friendly Chat Interface**: Built with Chainlit for a streamlined conversation experience.

## Setup

### Prerequisites

- Python 3.8+
- [Google Cloud API Key](https://cloud.google.com/docs/authentication/getting-started)
- Pinecone API Key (for embeddings and document storage)
- Hugging Face Embeddings model

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Poojitha319/MedGuideAI.git
    cd MedGuideAI
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Environment Setup**:
   - Set up your Google API and Pinecone keys in the environment variables or in the `.env` file:
    ```bash
    export PINECONE_API_KEY="your_pinecone_api_key"
    export GOOGLE_MAPS_API_KEY="your_google_maps_api_key"
    ```

4. **Load Medical Data**:
   - Place your PDF files in a directory (e.g., `./content`) to be processed by the chatbot for medical information retrieval.

## Usage

### Running the Chatbot Locally

1. **Start Chainlit Interface**:
    ```bash
    chainlit run app.py -w
    ```

2. **Chat Commands**:
   - **Ask Medical Questions**: Type in any health-related question.
   - **Schedule an Appointment**: Enter “book an appointment with Dr. [name]” to check availability and schedule.
   - **Request Emergency Route**: Type “emergency route” to get directions to the nearest hospital.

## Project Modules

### 1. Medical Information Retrieval

The chatbot can answer medical questions by processing data stored in PDF files. It uses **LangChain** for embeddings and **Pinecone** for efficient data retrieval.

### 2.Doctor Appointment Scheduling

MedGuideAI integrates with Google Calendar to facilitate appointment scheduling. Users can easily book appointments with doctors by checking their availability and confirming the appointment through the chatbot.

#### Features

- Check doctor availability
- Schedule appointments
- Send reminders

#### Setup

1. **Google Calendar API**:
   - Ensure you have access to the Google Calendar API and obtain the necessary credentials.
   - Store your credentials securely and set the environment variable for the API key.

2. **Environment Variable**:
   - Set your Google API credentials in the environment variables or in a `.env` file:
    ```bash
    export GOOGLE_API_KEY="your_google_api_key"
    ```
### 3.Emergency Routing to Hospitals

The MedChatbot includes an emergency routing feature that assists users in finding the quickest route to the nearest hospital in case of emergencies. This feature leverages location services and mapping APIs to provide real-time navigation assistance.

#### Features

- Locate the nearest hospitals based on the user's current location.
- Provide step-by-step directions to the selected hospital.
- Display estimated travel time and distance.

#### Setup

1. **Google Maps API**:
   - Obtain an API key from Google Cloud Console for the Google Maps Directions API and Places API.
   - Store your credentials securely and set the environment variable for the API key.

2. **Environment Variable**:
   - Set your Google Maps API key in the environment variables or in a `.env` file:
    ```bash
    export GOOGLE_MAPS_API_KEY="your_google_maps_api_key"
    ```
### 4. Chainlit Chat Interface
A streamlined interface using Chainlit to enhance user experience. It handles inputs, processes requests for medical information, appointments, and emergency routing.
### Future Enhancements
- Medication Reminders: Set reminders for medications.
- Medical Record Access: Allow users to upload and access personal health records.
- Symptoms Checker: Integrate a symptom-checking feature to provide preliminary diagnostics.

