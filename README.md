# CITS5506 2024S2 Project - Smart Mailbox

## Overview

**Smart Mailbox** is an IoT-enabled solution designed to improve the convenience and security of traditional mail management systems. It combines real-time notifications, enhanced security features, and smart analytics to create a seamless experience for users.

## Features

- **Real-Time Notifications**: The Smart Mailbox records all mailbox activities, including new mail arrivals, lock/unlock events, password changes, and security alerts. These events are updated in real-time on the web dashboard. If email notifications are configured, users will receive real-time alerts on all mailbox activities.

- **Mailbox Security**: Equipped with a solenoid lock, the mailbox ensures secure access. Users can unlock the mailbox by entering a password on the hardware keypad or remotely via the web dashboard. Passwords can also be updated remotely. The system monitors for repeated failed access attempts and triggers security alerts as needed.

- **Smart Features**: Upon the arrival of new mail, the Smart Mailbox automatically captures a picture of the mail. This image is analyzed using ChatGPT to extract useful information and insights. Users can provide additional contextual information via the web dashboard to enhance accuracy. The dashboard also displays visual insights into usage patterns, such as daily mail counts, types of mail received, and delivery time trends.

- **Usability and Reliability**: The responsive design of the web dashboard ensures a smooth user experience on both desktop and mobile devices. The Smart Mailbox continues to function as a traditional mailbox even during network outages, allowing users to retrieve their mail without interruption. Once connectivity is restored, all data collected during offline periods is automatically synchronized, ensuring a complete activity history.

For more detailed information, please visit our [project report](https://www.overleaf.com/read/kwgvzccmddds#70f059).

## Running the Project

Make sure to download the entire repository, as both `device` and `backend` require access to the `shared` folder to function correctly.

### Starting the Frontend

To start the frontend, open a separate shell and run:

```bash
cd frontend
npm install
npm run dev
```

The frontend should now be accessible at `http://localhost:5173/`. Initially, you may see request errorswhich are expected because the backend isn't running yet. To resolve these errors, you'll need to start the backend.

For simplicity, we're using a development server here. This setup assumes the backend is running on the same machine and automatically proxies requests to URLs starting with `/api` to `http://127.0.0.1:5000`. If you opt not to use the development server, you'll need to know how to build a production version of the frontend, host the static files with a web server, and configure a reverse proxy to connect the frontend to the backend. Setting this up may vary based on your environment and is beyond the scope of this guide.

### Starting the Backend

Before starting the backend, configure `backend/config.py`:

- **`FRONTEND_HOST_NAME`**: Set this to your frontend's hostname. If running locally, this can be ignored, but images in email notifications might not display. For a cloud-hosted backend, use a public IP address.

- **`MailEventConfig.GPT_API_KEY`**: Provide the API key for ChatGPT to enable image analysis.

- **Email Settings**: Configure the following for email notifications to work:
  - `EmailConfig.SMTP_SERVER`
  - `EmailConfig.SMTP_PORT`
  - `EmailConfig.EMAIL_USER`
  - `EmailConfig.EMAIL_PASSWORD`

After completing the configuration, start the backend:

```bash
cd backend
./run.sh
```

At this stage, the frontend should be functioning properly, with no more request errors, and you should be able to modify the settings item. However, it still indicates that the device is offline.

### Starting the Device Application

Before launching the device application, ensure that all hardware components are properly set up. Update the GPIO pin numbers in `device/config.py` to align with your specific setup.

Next, modify the `BACKEND_HOST_NAME` in `device/config.py` to enable communication between the device and your backend server. If you're running the backend locally, make sure the Raspberry Pi is connected to the same network as the computer hosting the backend. Use the computer's internal IP address, typically in the format `192.168.x.x` or `10.x.x.x`. For a cloud-hosted backend, enter the server's public IP address.

After completing the configuration, run the device application with the following commands:

```bash
cd device
python3 main.py
```

If you encounter any dependency errors, install the necessary packages. Usually, the only package you will need to install is PiCamera2.

If all steps are followed correctly, you should see the device online in the web dashboard. Now, have fun!

### Setting Up Git Hooks [Optional]

This repository utilizes Git hooks to streamline contributions. After cloning the repository and navigating to the project directory, set up the Git hooks by running:

```bash
./setup-git-hooks.sh  # For Linux or macOS
setup-git-hooks.cmd   # For Windows
```

If the Git hooks are correctly set up, they will enforce commit message style guidelines and help format code before committing. However, most modern IDEs offer similar functionalities, so you may use these features based on personal preference.
