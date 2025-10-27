# Personal Test Data Generator – Group I  
![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Flask](https://img.shields.io/badge/Backend-Flask-lightgrey?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)
![Pytest](https://img.shields.io/badge/Tests-Pytest-green?logo=pytest)
![Postman](https://img.shields.io/badge/API-Postman-orange?logo=postman)
![Playwright](https://img.shields.io/badge/E2E-Playwright-purple?logo=microsoft)
![SonarQube](https://img.shields.io/badge/Static--Analysis-SonarQube-lightblue?logo=sonarqube)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub%20Actions-black?logo=githubactions)

📄 [Shared Google Docs Group: EP, BVA, Blackbox](https://docs.google.com/document/d/1GW89MWnAXZi4asn5hTVEzcce-luUpV88KWaRfE0m8N4/edit?tab=t.0)

---

## Overview  
The system generates **fake Danish personal data** — CPR, name, address, and phone — for software testing.  
Originally built in **PHP + MariaDB**, now converted to **Python (Flask) + SQLite** with a focus on **test-driven development** across unit, integration, and end-to-end levels.

Reference sources:  
- [arturomorarioja's PHP Backend](https://github.com/arturomorarioja/fake_info/)  
- [arturomorarioja's Frontend (HTML/CSS/JS)](https://github.com/arturomorarioja/js_fake_info_frontend)  
- [itsLearning Assignment Description (PDF)](https://github.com/Group-I-Personal-Test-Data-Generator/Personal-Test-Data-Generator/blob/main/First_Mandatory_Assignment.pdf)

---

## Project Structure
This is an **outline** of how we planned to organize files and folders for the assignment. 
```
.github/workflows
/frontend
/backend
/database
/tests
├── /unit
├── /integration
└── /e2e
/.github
└── /workflows
/pdf
├── /test-design (black, white, pdf)
└── /static-analysis (sonar, lint, screenshots)
app.py
.gitignore
README.md
```

---
## Run the project in local

```bash
# Terminal A for flask application
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

---

## Presentation Outline

### 1. Tech Stack & Conversion
**Responsible:** [@ChristianBT96](https://github.com/ChristianBT96)

- [x] PHP → Python (Flask) backend conversion
- [x] SQLite connection established
- [x] Same frontend reused (JS/HTML)  
- [x] SQLite connection established

---

### 2. CI/CD Pipeline
**Responsible:** [@ChristianBT96](https://github.com/ChristianBT96)

- [x] GitHub Actions workflow → main.yml
- [x] Triggered on push and pull main

---

### 3. Unit Testing  
**Responsible:** [@ViktorBach](https://github.com/ViktorBach), [@SofieAmalie44](https://github.com/SofieAmalie44)

**Checklist:**  
- [x] pyTest used for backend logic validation 
- [x] Black-box 
- [x] White-box 
- [x] tests/unit

```bash
pytest -q tests/unit
``` 

---

### 4. Integration Testing  
**Responsible:** [@marcus-rk](https://github.com/marcus-rk)  

**Checklist:**  

- **API ↔ Database**  
  - [x] tests/integration 
  - [x] pyTest for testing API ↔ SQLite
  - [x] Postman for testing API ↔ Client
  - [x] Postman with Newman in pipeline

```bash
pytest -q tests/integration
```  

---

### 5. Linting & SonarQube
**Responsible:** [@SofieAmalie44](https://github.com/SofieAmalie44)

**Checklist:**  
- [x] Static code analysis with ESLint 
- [x] SonarQube 

```bash
pylint backend/FakeInfoService/services/*.py
npx eslint "**/*.js"
```  

---

### 6. End-to-End Testing 
**Responsible:** [@DetGrey](https://github.com/DetGrey), [@nathasjafink](https://github.com/nathasjafink)  

**Checklist:**  
- [x] Playwright test
- [x] Run in pipeline

```bash
# Terminal B for frontend
python -m http.server 5500 --bind 127.0.0.1 --directory frontend

# Terminal C for e2e test
playwright install
pytest -q tests/e2e
``` 

---

## API Endpoints

| Method | Endpoint | Description |
|:-------|:----------|:-------------|
| GET | `/cpr` | Returns a fake CPR |
| GET | `/name-gender` | Returns first name, last name, and gender |
| GET | `/name-gender-dob` | Returns name, gender, and date of birth |
| GET | `/cpr-name-gender` | Returns CPR, name, and gender |
| GET | `/cpr-name-gender-dob` | Returns CPR, name, gender, and date of birth |
| GET | `/address` | Returns a fake address |
| GET | `/phone` | Returns a fake phone number |
| GET | `/person` | Returns all data for one fake person |
| GET | `/person?n=<number_of_fake_persons>` | Returns fake data for multiple persons (2–100) |

---

## Class FakeInfo – Public Methods

| Method | Return Type | Description |
|:--------|:-------------|:-------------|
| `getCPR()` | `str` | Generates a fake CPR number |
| `getFullNameAndGender()` | `dict` | Returns first name, last name, and gender |
| `getFullNameGenderAndBirthDate()` | `dict` | Returns name, gender, and date of birth |
| `getCprFullNameAndGender()` | `dict` | Returns CPR, first name, last name, and gender |
| `getCprFullNameGenderAndBirthDate()` | `dict` | Returns CPR, name, gender, and date of birth |
| `getAddress()` | `str` | Returns a fake address |
| `getPhoneNumber()` | `str` | Returns a fake phone number |
| `getFakePerson()` | `dict` | Returns all data for one fake person |
| `getFakePersons(amount: int)` | `list[dict]` | Returns fake data for multiple persons (2–100) |