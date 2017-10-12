def _add(path):
    import sys
    from os.path import abspath

    if path not in sys.path:
        sys.path.append(abspath(path))


def setup():
    from os.path import join, dirname
    from os import walk

    cur_dir = dirname(__file__)
    proj_dir = dirname(cur_dir)
    libs_dir = join(proj_dir, 'libs')

    for root, dirs, files in walk(libs_dir):
        if root == libs_dir:
            for lib in dirs:
                _add(join(libs_dir, lib))
            break