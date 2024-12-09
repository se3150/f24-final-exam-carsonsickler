import time

@when('I type "{text}" in the message box')
def step_impl(context, text):
    context.behave_driver.find_element_by_css_selector('textarea#letters').send_keys(text)

@then(u'I expect the message to be "{message}"')
def step_impl(context, message):
    #div#decoded_message > p contains message
    assert context.behave_driver.find_element_by_css_selector('div#decoded_message > p').text == message

@when("I wait for {num} milliseconds")
def step_impl(context, num):
    time.sleep(int(num)/1000)