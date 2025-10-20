from helpers import verify_field
import validation


# 3. **Generate CPR only**
#    - Select `chkPartialOptions`
#    - Choose “CPR” from `cmbPartialOptions`
#    - Click “Generate”
#    - Verify CPR field is visible and valid

def test_generate_cpr(browser_page):
    # Select "Partial generation"
    browser_page.click("#chkPartialOptions")

    # Choose "CPR" from dropdown
    browser_page.select_option("#cmbPartialOptions", "cpr")

    # Click "Generate"
    browser_page.click("input[type=submit]")

    # Wait for CPR value to appear (but max 3 sec) and assert CPR is valid
    verify_field(browser_page, ".cprValue", validation.is_valid_cpr)


# 4. **Generate name and gender**
#    - Select `chkPartialOptions`
#    - Choose “Name and gender”
#    - Click “Generate”
#    - Verify first name, last name, and gender fields are visible

def test_generate_name_gender(browser_page):
    browser_page.click("#chkPartialOptions")
    browser_page.select_option("#cmbPartialOptions", "name-gender")
    browser_page.click("input[type=submit]")

    verify_field(browser_page, ".firstNameValue", validation.is_valid_name)
    verify_field(browser_page, ".lastNameValue", validation.is_valid_name)
    verify_field(browser_page, ".genderValue", validation.is_valid_gender)


## ------------------------------------------------- TODO NATHASJA HAS THE ONES BELOW
# 5. **Generate name, gender, and birthdate**
#    - Select `chkPartialOptions`
#    - Choose “Name, gender and birthdate”
#    - Click “Generate”
#    - Verify name, gender, and DOB fields are shown

# 6. **Generate CPR, name, and gender**
#    - Select `chkPartialOptions`
#    - Choose “CPR, name and gender”
#    - Click “Generate”
#    - Verify CPR, name, and gender fields are shown

# 7. **Generate CPR, name, gender, and birthdate**
#    - Select `chkPartialOptions`
#    - Choose “CPR, name, gender, birthdate”
#    - Click “Generate”
#    - Verify all four fields are visible

# 8. **Generate address**
#    - Select `chkPartialOptions`
#    - Choose “Address”
#    - Click “Generate”
#    - Verify street and town fields are shown

# 9. **Generate phone number**
#    - Select `chkPartialOptions`
#    - Choose “Phone number”
#    - Click “Generate”
#    - Verify phone number field is visible
