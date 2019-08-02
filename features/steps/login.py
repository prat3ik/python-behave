from nose.tools import *
from behave import *

package_id = "com.seabornlee.robolectricdemo"


@given('I enter "{text}" in "{text_field_id}"')
def step_impl(context, text_field_id, text):
    text_field = context.driver.find_element_by_id(package_id + ":id/et_" + text_field_id)
    text_field.send_keys(text)


@when('I click on the "{text_on_button}" button')
def step_impl(context, text_on_button):
    context.driver.find_element_by_id(package_id + ":id/btn_" + text_on_button).click()


@then('I should see "{label_id}" is "{expected_text}"')
def step_impl(context, label_id, expected_text):
    text = context.driver.find_element_by_id(package_id + ":id/" + label_id).text
    eq_(expected_text, text)