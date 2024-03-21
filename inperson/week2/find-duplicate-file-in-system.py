class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # stores file content maped to their directory
        dic = defaultdict(set)

        for path in  paths:
            directory,*files = path.split()
            
            for _file in files:
                file_name, content = _file.split("(")
                dic[content[:-1]].add( f"{directory}/{file_name}")

        return [list(duplicate) for duplicate in dic.values() if len(duplicate)>1]