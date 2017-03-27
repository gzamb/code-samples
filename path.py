class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        current_dir = [p for p in self.current_path.split('/') if p]
        path_directories = [p for p in new_path.split('/') if p]

        if not path_directories:
            self.current_path = '/'
            return self

        for idx, n in enumerate(path_directories):
            if n == '..':
                current_dir.pop()
            else:
                current_dir.append(n)

        self.current_path = '/' + '/'.join(current_dir)
        return self

paths = Path('/a/b/c/d')
paths = paths.cd('../x')
print(paths and paths.current_path)

paths = Path('/a/b/c/d')
paths = paths.cd('../..')
print(paths and paths.current_path)

paths = Path('/a/b')
paths = paths.cd('../..')
print(paths and paths.current_path)

paths = Path('/a/b/c/d')
paths = paths.cd('/')
print(paths and paths.current_path)

paths = Path('/a/b/c/d')
paths = paths.cd('j/f')
print(paths and paths.current_path)
