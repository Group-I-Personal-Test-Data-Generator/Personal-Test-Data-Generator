# Personal Test Data Generator – Group I
![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Flask](https://img.shields.io/badge/Backend-Flask-lightgrey?logo=flask)
![Pytest](https://img.shields.io/badge/Tests-Pytest-green?logo=pytest)
![MySQL](https://img.shields.io/badge/Database-MySQL-blue?logo=mysql)
![Postman](https://img.shields.io/badge/API-Postman-orange?logo=postman)
![Playwright](https://img.shields.io/badge/E2E-Playwright-purple?logo=microsoft)
![GitHub Actions](https://img.shields.io/badge/CI-CD-GitHub_Actions-black?logo=githubactions)

### 🎯 Project Overview
Application that generates **fake Danish personal data** (CPR, names, addresses, phone numbers) for software testing.  
Originally built in PHP + MariaDB, now converted to **Python + MySQL**.  
The focus is **testing** — not development — using unit, integration, and end-to-end approaches.  

---
## 🧩 Domains and Dependencies
### **0. Conversion Domain**
**Goal:** Prepare a consistent and testable Python + MySQL backend.  
- Convert backend logic from PHP to Python.  
- Connect to MySQL using `mysql.connector`.  
- Recreate endpoints in Flask (or FastAPI?).  
- Verify API outputs and database access manually.  
**→ Output:** Working baseline system for all subsequent testing domains.

---
### **1. Unit Domain**
**Goal:** Verify correctness of individual backend functions.  
- Test CPR, gender, date-of-birth generation.  
- Test address and phone logic.  
- No database or API involved (pure Python).  
- Apply black-box and white-box techniques.  
**→ Output:** Reliable backend logic and full code coverage.

---

### **2. Integration Domain**
**Goal:** Verify data flow across backend + database + API.  
- Ensure correct responses from endpoints (Flask/FastAPI).  
- Check consistency between CPR and date-of-birth.  
- Validate address data from MySQL.  
- Use Postman + pytest integration tests.  
**→ Output:** Backend and API work as a unified system.

---

### **3. System / End-to-End Domain**
**Goal:** Validate the entire system through the frontend.  
- Use Cypress or Playwright to simulate user actions.  
- Verify that UI displays API data correctly.  
- Include error handling and edge cases.  
**→ Output:** Fully functional fake data generator tested as a whole.

---
### 👥 Team & Roles
| Pair | Members | Focus |
|------|----------|--------|
| 1 | Name1, Name2 | Unit tests + static analysis |
| 2 | Name3, Name4 | Integration + API testing |
| 3 | Name5, Name6 | End-to-End + CI/CD |

---

### 🧩 Project Structure
```
/backend
/tests/unit
/tests/integration
/tests/e2e
/.github/workflows
README.md
```

---

### ✅ Progress
- [x] Backend converted to Python
- [ ] Database connected
- [ ] Unit tests & static analysis
- [ ] Integration tests & CI
- [ ] E2E tests & CI/CD
- [ ] Report & presentation ready
