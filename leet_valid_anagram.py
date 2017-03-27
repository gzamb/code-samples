class Solution(object):
    def isAnagram(self, s, t):
        """
        Using the count and compare solution
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        letter_vector = [0] * 26

        for letter in s:
            pos = ord(letter) - ord('a')
            letter_vector[pos] += 1

        for letter in t:
            pos = ord(letter) - ord('a')
            if letter_vector[pos] == 0:
                return False
            letter_vector[pos] -= 1

        if sum(letter_vector):
            return False

        return True


x = Solution()
print(x.isAnagram("earth", "heart"))
print(x.isAnagram("Lord Voldemort", "Tom Malvoro"))
print(x.isAnagram("a", "b"))
