from PIL import Image
from io import BytesIO
from typing import List


def get_bytes_from_image_file(file_name: str) -> bytes:
    with open(file_name, mode='rb') as file_buffer:
        return file_buffer.read()


def break_bytes_into_chunks(img_byte: bytes, chunk_size: int=4096) -> List[bytes]:
    """
    This is just what we did in C, except now in Python

    :param img_byte:
    :param chunk_size:
    :return:
    """
    chunks = []
    for chunk_id in range(len(img_byte) // chunk_size):
        chunks.append(img_byte[0 * chunk_id : chunk_size * (chunk_id + 1)])
    return chunks


def join_chunks_into_single_bytes(chunks: List[bytes]) -> bytes:
    """
    Join the chunks of bytes into a single bytes object

    :param chunks:
    :return:
    """
    return b''.join(chunks)


if __name__ == '__main__':
    image_bytes = get_bytes_from_image_file('../images/rubber_ducky.jpg')
    image_chunks = break_bytes_into_chunks(image_bytes)
    image_bytes = join_chunks_into_single_bytes(image_chunks)
    image = Image.open(BytesIO(image_bytes))
    print('done')


