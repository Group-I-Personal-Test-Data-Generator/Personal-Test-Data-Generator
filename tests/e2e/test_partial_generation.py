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


# 5. **Generate name, gender, and birthdate**
#    - Select `chkPartialOptions`
#    - Choose “Name, gender and birthdate”
#    - Click “Generate”
#    - Verify name, gender, and DOB fields are shown

def test_generate_name_gender_dob (browser_page):
    browser_page.click("#chkPartialOptions")
    browser_page.select_option("#cmbPartialOptions", "name-gender-dob")
    browser_page.click("input[type=submit]")

    verify_field(browser_page, ".firstNameValue", validation.is_valid_name)
    verify_field(browser_page, ".lastNameValue", validation.is_valid_name)
    verify_field(browser_page, ".genderValue", validation.is_valid_gender)
    verify_field(browser_page, ".dobValue", validation.is_valid_dob)

# 6. **Generate CPR, name, and gender**
#    - Select `chkPartialOptions`
#    - Choose “CPR, name and gender”
#    - Click “Generate”
#    - Verify CPR, name, and gender fields are shown

def test_generate_cpr_name_gender (browser_page):
    browser_page.click("#chkPartialOptions")
    browser_page.select_option("#cmbPartialOptions", "cpr-name-gender")
    browser_page.click("input[type=submit]")

    verify_field(browser_page, ".cprValue", validation.is_valid_cpr)
    verify_field(browser_page, ".firstNameValue", validation.is_valid_name)
    verify_field(browser_page, ".lastNameValue", validation.is_valid_name)
    verify_field(browser_page, ".genderValue", validation.is_valid_gender)
    

# 7. **Generate CPR, name, gender, and birthdate**
#    - Select `chkPartialOptions`
#    - Choose “CPR, name, gender, birthdate”
#    - Click “Generate”
#    - Verify all four fields are visible

def test_generate_cpr_name_gender_dob (browser_page):
    browser_page.click("#chkPartialOptions")
    browser_page.select_option("#cmbPartialOptions", "cpr-name-gender-dob")
    browser_page.click("input[type=submit]")

    verify_field(browser_page, ".cprValue", validation.is_valid_cpr)
    verify_field(browser_page, ".firstNameValue", validation.is_valid_name)
    verify_field(browser_page, ".lastNameValue", validation.is_valid_name)
    verify_field(browser_page, ".genderValue", validation.is_valid_gender)
    verify_field(browser_page, ".dobValue", validation.is_valid_dob)

# 8. **Generate address**
#    - Select `chkPartialOptions`
#    - Choose “Address”
#    - Click “Generate”
#    - Verify street and town fields are shown

def test_generate_address (browser_page):
    browser_page.click("#chkPartialOptions")
    browser_page.select_option("#cmbPartialOptions", "address")
    browser_page.click("input[type=submit]")

    verify_field(browser_page,".streetValue", validation.is_valid_street)
    verify_field(browser_page,".townValue", validation.is_valid_town)

# 9. **Generate phone number**
#    - Select `chkPartialOptions`
#    - Choose “Phone number”
#    - Click “Generate”
#    - Verify phone number field is visible

def test_generate_phone_number (browser_page):
    browser_page.click("#chkPartialOptions")
    browser_page.select_option("#cmbPartialOptions", "phone")
    browser_page.click("input[type=submit]")

    verify_field(browser_page,".phoneNumberValue", validation.is_valid_phone_number)
    
