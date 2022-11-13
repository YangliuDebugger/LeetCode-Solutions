class FileSystem:
    # Trie的大杂烩

    def __init__(self):
        self.root_dir = {}
        self.document = {}

    def ls(self, path: str) -> List[str]:
        d = self.root_dir
        if path == "/":
            path = ""
        paths = path.split("/")
        for p in paths:
            if p not in d:
                d[p] = {}
            d = d[p]
        res = []
        if '#' in d:
            res.append(paths[-1])
        else:
            for f in sorted(d.keys()):
                res.append(f)
        return res

    def mkdir(self, path: str) -> None:
        d = self.root_dir
        paths = path.split("/")
        for p in paths:
            if p not in d:
                d[p] = {}
            d = d[p]
        print(self.root_dir)

    def addContentToFile(self, filePath: str, content: str) -> None:
        d = self.root_dir
        paths = filePath.split("/")
        for path in paths:
            if path not in d:
                d[path] = {}
            d = d[path]
        d["#"] = '#'
        if filePath not in self.document:
            self.document[filePath] = ''
        self.document[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.document[filePath]

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)