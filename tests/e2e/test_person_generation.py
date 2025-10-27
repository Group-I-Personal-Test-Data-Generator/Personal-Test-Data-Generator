from helpers import verify_field
import validation

# 1. **Generate 1 full person**
#    - Ensure `chkPerson` is selected
#    - Leave `txtNumberPersons` at default (1)
#    - Click “Generate”
#    - Verify CPR, name, gender, DOB, address, and phone number are shown

def test_generate_one_person(browser_page):
    browser_page.click("#chkPerson")
    browser_page.fill("#txtNumberPersons", "1")
    browser_page.click("input[type=submit]")

    verify_field(browser_page, ".cprValue", validation.is_valid_cpr)
    verify_field(browser_page, ".firstNameValue", validation.is_valid_name)
    verify_field(browser_page, ".lastNameValue", validation.is_valid_name)
    verify_field(browser_page, ".genderValue", validation.is_valid_gender)
    verify_field(browser_page, ".dobValue", validation.is_valid_dob)
    verify_field(browser_page, ".streetValue", validation.is_valid_street)
    verify_field(browser_page, ".townValue", validation.is_valid_town)
    verify_field(browser_page, ".phoneNumberValue", validation.is_valid_phone_number)


#  2. **Generate multiple persons**
#    - Select `chkPerson`
#    - Set `txtNumberPersons` to 3
#    - Click “Generate”
#    - Verify 3 person cards are rendered with complete data

def test_generate_three_people(browser_page):
    browser_page.click("#chkPerson")
    browser_page.fill("#txtNumberPersons", "3")
    browser_page.click("input[type=submit]")

    browser_page.wait_for_selector(".personCard", state="visible", timeout=3000)
    cards = browser_page.query_selector_all(".personCard")

    assert len(cards) == 3

    for card in cards:
        verify_field(card, ".cprValue", validation.is_valid_cpr)
        verify_field(card, ".firstNameValue", validation.is_valid_name)
        verify_field(card, ".lastNameValue", validation.is_valid_name)
        verify_field(card, ".genderValue", validation.is_valid_gender)
        verify_field(card, ".dobValue", validation.is_valid_dob)
        verify_field(card, ".streetValue", validation.is_valid_street)
        verify_field(card, ".townValue", validation.is_valid_town)
        verify_field(card, ".phoneNumberValue", validation.is_valid_phone_number)
