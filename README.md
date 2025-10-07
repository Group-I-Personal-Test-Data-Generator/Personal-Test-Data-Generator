# Personal Test Data Generator – Group I
![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Flask](https://img.shields.io/badge/Backend-Flask-lightgrey?logo=flask)
![Pytest](https://img.shields.io/badge/Tests-Pytest-green?logo=pytest)
![MySQL](https://img.shields.io/badge/Database-MySQL-blue?logo=mysql)
![Postman](https://img.shields.io/badge/API-Postman-orange?logo=postman)
![Playwright](https://img.shields.io/badge/E2E-Playwright-purple?logo=microsoft)

---

### Project Overview
The system generates fake Danish personal data (CPR, name, address, phone) for testing.  
Originally in PHP + MariaDB, now converted to **?(Python + Flask + MySQL)?**.  
Focus: testing through unit, integration, and end-to-end levels.

Feel free to use my application code (either directly or as inspiration):
- Backend (MariaDB / PHP8): https://github.com/arturomorarioja/fake_info/
- Frontend (JavaScript / CSS3 / HTML5): https://github.com/arturomorarioja/js_fake_info_frontend

---

## Domains

### 0. Conversion Domain
Prepare a working backend for testing.  
- Convert PHP backend to Python.  
- Connect to MySQL (or MariaDB?).  
- Implement API endpoints in Flask (or FastAPI?).  
- Verify database access and responses manually.  

**Output:** Stable Python + MySQL backend with functional API.

---

### 1. Unit Domain
Test internal logic (no DB/API).  
- Validate CPR, gender, date of birth, address, phone generation.  
- Use pytest with black-box and white-box methods.  
- Run static analysis 
- Test case values

**Output:** Reliable backend logic and quality metrics.

---

### 2. Integration Domain
Test backend + database + API as one system.  
- Verify endpoints return consistent, correct data.  
- Test database retrieval via MySQL.  
- Automate API tests with Postman and pytest.  
- Add tests to CI pipeline.  

**Output:** Verified and automated integration flow.

---

### 3. System / End-to-End Domain
Test full workflow through the frontend.  
- Use Playwright (or Cypress/Selenium).  
- Validate UI correctly displays API data.  
- Integrate all test layers in CI/CD.  

**Output:** Fully tested system ready for demo and delivery.

---

## Team & Roles
| Members | Focus |
|----------|--------|
| ??? | Conversion |
| ??? | Unit tests + static analysis |
| ??? | Integration + API testing |
| ??? | End-to-End + CI/CD |

- @nathasjafink  
- @SofieAmalie44  
- @ViktorBach  
- @ChristianBT96  
- @DetGrey  
- @marcus-rk

---

## Project Structure
```
...
/backend
/tests/unit
/tests/integration
/tests/e2e
/.github/workflows
README.md
...
```

---

## Checklist
- [x] Organization / Repository created
- [ ] Backend converted to Python  
- [ ] Database connected  
- [ ] Unit tests & static analysis  
- [ ] Integration tests & CI setup  
- [ ] E2E tests & CI/CD pipeline  
- [ ] Report and presentation complete
