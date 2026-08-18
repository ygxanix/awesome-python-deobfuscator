import os, sys
os.system("pip install uncompyle6")
os.system("pip install pycdc")
import base64
import binascii
import zlib
import lzma
import marshal
import hashlib
import bz2
import urllib.parse
import quopri
import uu
import codecs
import pycdc
import uncompyle6

# دوال فك التشفير
def decode_base16(data):
    return base64.b16decode(data)

def decode_base32(data):
    return base64.b32decode(data)

def decode_base64(data):
    return base64.b64decode(data)

def decode_base85(data):
    return base64.b85decode(data)

def decode_hex(data):
    return bytes.fromhex(data)

def decompress_zlib(data):
    return zlib.decompress(data)

def decompress_lzma(data):
    return lzma.decompress(data)

def decompress_bz2(data):
    return bz2.decompress(data)

def decode_quopri(data):
    return quopri.decodestring(data)

def decode_uu(data):
    return uu.decode(data)

def decode_url(data):
    return urllib.parse.unquote(data)

def decode_unicode_escape(data):
    return codecs.escape_decode(data)[0]

def decode_rot13(data):
    return codecs.decode(data, 'rot_13')

def decode_utf7(data):
    return data.decode('utf-7')

def decode_utf8(data):
    return data.decode('utf-8')

def decode_utf16(data):
    return data.decode('utf-16')

def decode_utf32(data):
    return data.decode('utf-32')

def decode_ascii(data):
    return data.decode('ascii')

def decode_marshal(data):
    return marshal.loads(data)

def decode_sha256(data):
    return hashlib.sha256(data).hexdigest()

def decode_sha512(data):
    return hashlib.sha512(data).hexdigest()

def decode_md5(data):
    return hashlib.md5(data).hexdigest()

def decompress_gzip(data):
    import gzip
    from io import BytesIO
    with gzip.GzipFile(fileobj=BytesIO(data)) as f:
        return f.read()

def decode_binascii(data):
    return binascii.unhexlify(data)

def decode_unquote_plus(data):
    return urllib.parse.unquote_plus(data)

def decode_binascii_b2a(data):
    return binascii.b2a_hex(data)

def decompile_pyc(file_path):
    uncompyle6.decompile_file(file_path)

def decompile_with_pycdc(file_path):
    decompiler_instance = pycdc.decompiler.Pycdc()
    decompiler_instance.main(file_path)

def decode_ascii85(data):
    return base64.a85decode(data)

def decode_rle(data):
    return codecs.decode(data, 'bz2_codec')