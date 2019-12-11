#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess


# Your test case class goes here
class TestEcho(unittest.TestCase):

    def call_echo(self, option, test_input=None):
        command = ['python', './echo.py']
        command.extend([option, test_input])
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE
        )
        stdout, _ = process.communicate()

        return stdout

    def test_help(self):
        """Running the program without arguments should show usage."""
        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper_short(self):
        stdout = self.call_echo('-u', 'hello')
        self.assertEquals(stdout, 'HELLO')

    def test_upper_long(self):
        stdout = self.call_echo('--upper', 'hello')
        self.assertEquals(stdout, 'HELLO')

    def test_lower_short(self):
        stdout = self.call_echo('-l', 'HELLO')
        self.assertEquals(stdout, 'hello')

    def test_lower_long(self):
        stdout = self.call_echo('--lower', 'HELLO')
        self.assertEquals(stdout, 'hello')

    def test_title_short(self):
        stdout = self.call_echo('-t', 'HELLO')
        self.assertEquals(stdout, 'Hello')

    def test_title_long(self):
        stdout = self.call_echo('--title', 'HELLO')
        self.assertEquals(stdout, 'Hello')

    def test_multiple_flags(self):
        tul = self.call_echo('-tul', 'heLLo')
        ul = self.call_echo('-ul', 'heLLo')
        self.assertEquals(tul, 'Hello')
        self.assertEquals(ul, 'hello')


if __name__ == '__main__':
    unittest.main()
