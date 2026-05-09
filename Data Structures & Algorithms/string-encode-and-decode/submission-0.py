class Solution:

    def encode(self, strs: List[str]) -> str:
        to_be_send = ""
        for word in strs:
            to_be_send += str(word)
            to_be_send += "55:34|,."
        return to_be_send


    def decode(self, s: str) -> List[str]:
        my_list = []
        my_list= s.split("55:34|,.")
        return my_list[:-1]
