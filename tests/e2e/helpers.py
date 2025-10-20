def verify_field(scope, selector, validator, timeout=3000):
    scope.wait_for_selector(selector, state="visible", timeout=timeout)
    element = scope.query_selector(selector)
    assert element is not None, f"Element {selector} not found in scope"
    value = element.inner_text()
    assert validator(value), f"Validation failed for {selector}: {value}"