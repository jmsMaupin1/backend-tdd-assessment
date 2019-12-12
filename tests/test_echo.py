#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess
import echo


# Your test case class goes here
class TestEcho(unittest.TestCase):

    # This test is dumb and doesnt work (ask for help)
    def test_help(self):
        """Running the program without arguments should show usage."""
        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read() + "\n"

        self.assertEquals(stdout, usage)

    def test_upper_short(self):
        stdout = echo.main(['-u', 'hello'])
        self.assertEquals(stdout, 'HELLO')

    def test_upper_long(self):
        stdout = echo.main(['--upper', 'hello'])
        self.assertEquals(stdout, 'HELLO')

    def test_lower_short(self):
        stdout = echo.main(['-l', 'HELLO'])
        self.assertEquals(stdout, 'hello')

    def test_lower_long(self):
        stdout = echo.main(['--lower', 'HELLO'])
        self.assertEquals(stdout, 'hello')

    def test_title_short(self):
        stdout = echo.main(['-t', 'HELLO'])
        self.assertEquals(stdout, 'Hello')

    def test_title_long(self):
        stdout = echo.main(['--title', 'HELLO'])
        self.assertEquals(stdout, 'Hello')

    def test_multiple_flags(self):
        tul = echo.main(['-tul', 'heLLo'])
        ul = echo.main(['-ul', 'heLLo'])
        self.assertEquals(tul, 'Hello')
        self.assertEquals(ul, 'hello')


if __name__ == '__main__':
    unittest.main()
