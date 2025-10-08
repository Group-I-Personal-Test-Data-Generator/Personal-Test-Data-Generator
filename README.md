# Personal Test Data Generator – Group I  
![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Flask](https://img.shields.io/badge/Backend-Flask-lightgrey?logo=flask)
![MariaDB](https://img.shields.io/badge/Database-MariaDB-blue?logo=mariadb)
![Pytest](https://img.shields.io/badge/Tests-Pytest-green?logo=pytest)
![Postman](https://img.shields.io/badge/API-Postman-orange?logo=postman)
![Playwright](https://img.shields.io/badge/E2E-Playwright-purple?logo=microsoft)
![SonarQube](https://img.shields.io/badge/Static--Analysis-SonarQube-lightblue?logo=sonarqube)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub%20Actions-black?logo=githubactions)

📄 [Shared Google Docs Group: EP, BVA, Blackbox](https://docs.google.com/document/d/1GW89MWnAXZi4asn5hTVEzcce-luUpV88KWaRfE0m8N4/edit?tab=t.0)

---

## Overview  
The system generates **fake Danish personal data** — CPR, name, address, and phone — for software testing.  
Originally built in **PHP + MariaDB**, now converted to **Python (Flask) + MariaDB** with a focus on **test-driven development** across unit, integration, and end-to-end levels.

Reference sources:  
- [arturomorarioja's PHP Backend](https://github.com/arturomorarioja/fake_info/)  
- [arturomorarioja's Frontend (HTML/CSS/JS)](https://github.com/arturomorarioja/js_fake_info_frontend)  
- [itsLearning Assignment Description (PDF)](https://github.com/Group-I-Personal-Test-Data-Generator/Personal-Test-Data-Generator/blob/main/First_Mandatory_Assignment.pdf)

---

## Project Structure
This is a **temporary outline** of how we plan to organize files and folders for the assignment. 
```
/frontend
/backend
/database
/tests
├── /unit
├── /integration(api)
└── /e2e
/.github
└── /workflows
/docs
├── /test-design (black, white, pdf)
└── /static-analysis (sonar, lint, screenshots)
.gitignore
README.md
```

---

## Domain Responsibilities

### 1. Backend Conversion  
**Responsible:** [@ChristianBT96](https://github.com/ChristianBT96) + ChatGPT 5 Plus  

Convert PHP backend to Python (Flask) and connect to MariaDB.

**Checklist:**  
- [x] Organization + Repository created
- [ ] Folder structure created
- [ ] Backend logic converted
- [ ] Flask REST API endpoints implemented  
- [ ] MariaDB connection established  
- [ ] Manual API + DB verification  
- [ ] ...  

**Output:** Stable Flask + MariaDB backend.

---

### 2. Unit Testing  
**Responsible:** [@ViktorBach](https://github.com/ViktorBach), [@SofieAmalie44](https://github.com/SofieAmalie44), ([@ChristianBT96](https://github.com/ChristianBT96))  

Validate backend logic independent of database and API.

**Checklist:**  
- [ ] White-box tests (statement & branch coverage)  
- [ ] Black-box tests (EP, BVA, Decision Tables)  
- [ ] CPR, gender, date, phone, address logic verified  
- [ ] Statement & branch coverage metrics generated
- [ ] ...  

> ***Marcus Note:***    
> Just a thought, some of the `FakeInfo` methods could be split into smaller ones (like `getCpr()`, `getFullName()`, `getGender()`, or `getBirthDate()`).  
> Following SoC and AAA best practice, unit tests should focus on one behavior at a time, and combined methods (like `getCprFullNameGenderAndBirthDate()`) could make that harder.

**Output:** Reliable backend logic validated through automated tests.

---

### 3. Integration Testing  
**Responsible:** [@marcus-rk](https://github.com/marcus-rk)  

Test combined flow between backend, database, and API.

**Checklist:**  

- **API ↔ Database**  
  - [ ] Flask connects to MariaDB (no errors)  
  - [ ] Endpoints using DB (e.g. `/address`) return data from `addresses.sql`  
  - [ ] Data types and values make sense (town = str, etc.)  

- **Client ↔ API**  
  - [ ] Create Postman collection for all endpoints  
  - [ ] Validate response structure and key fields (`cpr`, `dob`, `gender`, etc.)  
  - [ ] Check logical consistency (CPR ↔ DOB, gender parity rule, error handling)  
  - [ ] Export collection to `tests/integration/api/` for later CI/CD  

- **Later (CI/CD)**  
  - [ ] Run Postman tests automatically in pipeline  

**Output:** Verified and automated integration flow.  

---

### 4. End-to-End Testing  
**Responsible:** [@DetGrey](https://github.com/DetGrey), [@nathasjafink](https://github.com/nathasjafink)  

Validate complete system behavior through the frontend.

**Checklist:**  
- [ ] Playwright / Cypress configured  
- [ ] UI displays API data correctly  
- [ ] “Happy path” tested end-to-end  
- [ ] Integrated into CI/CD  (LATER)
- [ ] ...  

**Output:** Full system tested and validated.

---

### 5. Static Testing & Quality Assurance  
**Responsible:** [@SofieAmalie44](https://github.com/SofieAmalie44)  

Ensure maintainable and consistent code quality.

**Checklist:**  
- [ ] ESLint configured  
- [ ] SonarQube analysis made (with screenshot?)
- [ ] ...  

**Output:** Codebase meets static quality and style standards.

---

### 6. CI/CD/CT Pipeline  
**Responsible:** ALL  

Automate testing, building, and deployment processes.

**Checklist:**  
- [ ] GitHub Actions workflow created  
- [ ] Unit + integration + E2E tests integrated  (all?) 
- [ ] Static analysis and coverage reports included
- [ ] ...  

**Output:** Fully automated and maintainable CI/CD pipeline.

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
| GET | `/person&n=<number_of_fake_persons>` | Returns fake data for multiple persons (2–100) |

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

