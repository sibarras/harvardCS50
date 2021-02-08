import os
import pathlib
import unittest, unittest.main as main

from selenium import webdriver

html_file = 'counter.html'

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()


class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri(html_file))
        self.assertEqual(driver.title, "Counter")
    
    def test_increase(self):
        driver.get(file_uri(html_file))
        increase = driver.find_element_by_id('increase')
        increase.click()
        self.assertEqual(driver.find_element_by_tag_name('h1').text, '1')

    def test_decrease(self):
        driver.get(file_uri(html_file))
        increase = driver.find_element_by_id('decrease')
        increase.click()
        self.assertEqual(driver.find_element_by_tag_name('h1').text, '-1')
    
    def test_multiple_increase(self):
        driver.get(file_uri(html_file))
        increase = driver.find_element_by_id('increase')
        for _ in range(3):
            increase.click()
        self.assertEqual(driver.find_element_by_tag_name('h1').text, '3')
    
    def test_multiple_decrease(self):
        driver.get(file_uri(html_file))
        decrease = driver.find_element_by_id('decrease')
        for _ in range(3):
            decrease.click()
        self.assertEqual(driver.find_element_by_tag_name('h1').text, '-3')
    

        """ Different Assertions in unittest
        assertEqual
        assertNotEqual
        assertTrue
        assertFalse
        assertIn
        assertNotIn
        """

if __name__ == '__main__':
    main()