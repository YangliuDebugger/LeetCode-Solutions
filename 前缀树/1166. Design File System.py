class FileSystem:

    def __init__(self):
        self.root = {'': [-1, {}]}

    def createPath(self, path: str, value: int) -> bool:
        paths = path.split('/')
        d = self.root
        for idx, folder in enumerate(paths):
            if folder in d:
                if idx == len(paths) - 1:
                    return False  # Already exist
                else:
                    d = d[folder][1]
            else:
                if idx != len(paths) - 1:
                    return False  # no parent folder
                else:
                    d[folder] = [value, {}]
        return True

    def get(self, path: str) -> int:
        paths = path.split('/')
        d = self.root
        for idx, folder in enumerate(paths):
            if folder in d:
                if idx == len(paths) - 1:
                    return d[folder][0]
                d = d[folder][1]
            else:
                return -1

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)