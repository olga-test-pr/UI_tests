import time
from pages.form_page import FormPage
from pytest import mark

class TestForm:
    @mark.form
    class TestFormPage:
        @mark.smoke
        def testform(self,driver):
            form_page = FormPage(driver,'https://demoqa.com/automation-practice-form')
            form_page.open()
            p = form_page.fill_form_fields()
            result = form_page.form_result()
            time.sleep(5)
            assert [p.firstname + ' ' + p.lastname, p.email] == [result[0], result[1]], 'the form has not been filled'

