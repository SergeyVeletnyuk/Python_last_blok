from pathlib import Path


def group_rename_files(new_name: str, ext_renamed: str, ext_new: str, saved_range: tuple):
    work_path = Path.cwd()
    count_renamed = 0
    for i in work_path.iterdir():
        if i.is_file() and i.suffix == ext_renamed:
            file_name = f"{i.stem[saved_range[0]:saved_range[1]]}{new_name}_{count_renamed + 1:03}{ext_new}"
            i.rename(Path(i.parent, file_name))
            count_renamed += 1

    print(count_renamed)


if __name__ == '__main__':
    group_rename_files("task", ".txt", ".pdf", (1, 3))
