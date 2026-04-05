class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        blank_key = [chr(i + 97) for i in range(26)]

        groups = {}

        for x in strs:
            str_map = ",".join([str(x.count(char)) for char in blank_key])
            if str_map not in groups:
                groups[str_map] = []
            groups[str_map].append(x)

        group_list = []

        for item in groups.keys():
            group_list.append(groups[item])
        
        return group_list