# Lux\_Rescheduler

Lux\_Rescheduler is a simple desktop tool for shifting all calendar events from one day to another in a CalDAV calendar.

## ✨ What it does

This tool connects to your CalDAV calendar and allows you to **shift all events from a given start date to a new target date**. It's ideal for people who use their calendar as a task or todo list and sometimes don’t get through all their tasks in one day. Instead of manually moving each event, this app automates the process with one click.

As someone who personally uses their CalDAV calendar as a todo list, I created this because I often had to move several events from one day to another manually — this tool saves time and clicks.

## 🖥 How to Use

You can run this application in two ways:

### 1. As a Python script

Make sure you have Python 3 installed. Then, install the required libraries:

```bash
pip install customtkinter tkcalendar caldav
```

Then run the script with:

```bash
python Lux_Rescheduler.py
```

### 2. As a standalone executable (Windows)

You can download the latest `.exe` release from the [Releases](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/releases](https://github.com/LuxCodingFivem/Lux_Rescheduler/releases/tag/v1.0.0) section of this repository.
Just download and run — no installation or Python setup required.

> The app stores your CalDAV credentials encrypted using Windows DPAPI in a local `settings.json` file.

## 📋 Features

* Multi-language support (10+ languages)
* Shift all events from one day to another
* Save and encrypt CalDAV settings (username/password)
* Modern UI with `CustomTkinter`
* Progress bar for long calendar updates

## ⚙️ Settings

The app will ask for:

* CalDAV URL
* Username
* Password
* Preferred language

These settings are stored in `settings.json` and encrypted using Windows' built-in data protection (DPAPI).

## 🗕 Supported Calendars

The app supports **any CalDAV-compatible calendar**, including:

* Nextcloud/ownCloud
* iCloud (with app-specific password)
* Fastmail
* GMX/Web.de (if CalDAV is supported)
* Other custom CalDAV servers

## 📄 License

MIT License

Copyright (c) 2025 LuxCoding

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Thanks for using Lux\_Rescheduler.

---

Created by **LuxCoding** — 2025
