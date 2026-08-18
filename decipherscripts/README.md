# DecipherScripts Collection

This directory contains the merged Python deobfuscation scripts, decrypters, and utilities categorized by functionality.

## 🗂 Categories Overview

| Category | Description | Key Scripts / Tools |
| :--- | :--- | :--- |
| [`core/`](./core/) | General-purpose deobfuscation and multi-layer script unpackers | `DECODER-TOOLSs.py`, `dec_main.py`, `decody_decoder.py` |
| [`marshal/`](./marshal/) | Specialized decoders for Python `marshal` serialization & encodings | `Marshall_MAX.py`, `dec2-marshal.py`, `GoldenDec-main`, `MarshalDecoder-main` |
| [`python_versions/`](./python_versions/) | Version-targeted bytecode unpackers & AST decoders | `py_3_9.py`, `py_3_11.py`, `py_3_12_deobf.py`, `pycDcode-main` |
| [`obfuscator_decoders/`](./obfuscator_decoders/) | Custom obfuscator-specific scripts (Cython, Apocalipthyc, DecBot, SEO, etc.) | `Cython2.py`, `Apocalipthyc.py`, `DECBOTSS.py`, `seo.py`, `vendor_tools/` |
| [`decompilers/`](./decompilers/) | Native decompilers and disassemble utilities | `pycdc` (Decompyle++) |

---

## 🛠 Vendor Tools Breakdown

Under `obfuscator_decoders/vendor_tools/`, specific decoders contributed by community authors are organized:
- `DECODE_c4/`
- `DECODE_devil/`
- `DECODE_joker/`
- `DECODE_plya/`
- `DECODE_ress/`
- `DECODE_seo/`
- `DECODE_tc4/`
- `Tools-Decode-VIP/`
