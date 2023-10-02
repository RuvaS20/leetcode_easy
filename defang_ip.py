#Given a valid (IPv4) IP address, return a defanged version of that IP address.
#A defanged IP address replaces every period "." with "[.]".
"""
Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
"""

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        for i in range(len(address)):
            if address[i] == "." and address[i-1] != "[":
                  address = address.replace(address[i], "[.]")

        return address