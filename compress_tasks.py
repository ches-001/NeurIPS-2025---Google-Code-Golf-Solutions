import os
import zopfli.zlib
from glob import glob
from tqdm import tqdm
from python_minifier import minify

def zip_src(src: bytes):
    # We prefer that compressed source not end in a quotation mark
    while (compressed := zopfli.zlib.compress(src))[-1] == ord('"'): src += b"#"

    def sanitize(b_in: bytes):
        """Clean up problematic bytes in compressed b-string"""
        b_out = bytearray()
        for b in b_in:
            if b==0: b_out+=b"\\x00"
            elif b==ord("\r"): b_out+=b"\\r"
            elif b==ord("\\"): b_out+=b"\\\\"
            else: b_out.append(b)
        return b"" + b_out
    
    compressed = sanitize(compressed)
    delim = b'"""' if ord("\n") in compressed or ord('"') in compressed else b'"'
    return b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes(" + delim + compressed + delim + b',"L1")))'


def compress_file(task_num: int):
    path = f"{SOLUTIONS_PATH}/task{str(task_num).zfill(3)}.py"
    if not os.path.isfile(path):
        if os.path.exists(path): print(path)
        return
    with open(path,"rb") as f: src = f.read()
    src=min([src, minify(src).encode()], key=len)
    compressed_src = zip_src(src)
    
    if len(compressed_src) < len(src): src=compressed_src
    path = f"{COMPRESS_PATH}/task{str(task_num).zfill(3)}.py"
    with open(path,"wb") as f: f.write(src)


def display_quality(path: str):
    solutions = glob(os.path.join(path, '*.py'))
    print(f"Number of puzzle files: {len(glob(os.path.join(PUZZLES_PATH, '*.json')))}")
    print(f"Number of solutions: {len(solutions)}")
    print(f"Competition score: {sum([max(1, 2500-os.path.getsize(f)) for f in solutions])}")
    print(f"Average filesize: {sum([os.path.getsize(f) for f in solutions])/len(solutions) :.4f} bytes\n\n")


if __name__ == "__main__":
    PUZZLES_PATH = "dataset\google-code-golf-2025"
    SOLUTIONS_PATH = "tasks"
    COMPRESS_PATH = "compressed_tasks"

    os.makedirs(COMPRESS_PATH, exist_ok=True)
    print("Uncompressed solutions quality:\n")
    display_quality(SOLUTIONS_PATH)

    for task_num in tqdm(range(1,401)):
        compress_file(task_num)

    print("Compressed solutions quality:\n")
    display_quality(COMPRESS_PATH)