import os,asyncio,base64,string,random,time,zlib,shutil
try:
    import cython
except:
    print("install lib cython ...")
    os.system("pip install cython")
    print("resatrt")
    exit()
def gw(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
def gw2(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
def remove_comments(input_file, output_file):
    with open(input_file, 'r') as input_f:
        content = input_f.read()

    output_content = ''
    in_comment = False
    i = 0

    while i < len(content):
        if content[i:i+2] == '/*':
            in_comment = True
            i += 2
            continue
        elif content[i:i+2] == '*/':
            in_comment = False
            i += 2
            continue

        if not in_comment:
            output_content += content[i]

        i += 1

    with open(output_file, 'w') as output_f:
        output_f.write(output_content)
if not os.path.exists("m/"):
    os.mkdir("m")
def g(name):
    w=open(f"m/{name}","r",encoding="utf-8");a=w.read();w.close()
    if a.count("\n")<30:
        a=a+"#"+gw(1000)
    encoded_bytes = base64.b64encode(a.encode('utf-8'))
    a=encoded_bytes.decode('utf-8')
    lis2=[]
    lis = a.split("a")
    result = []
    for i in range(len(lis)):
        result.append(lis[i])
        if i < len(lis) - 1:
            result[-1] += "a"
    lis=(result)
    lis=lis[::-1]
    a=""
    t=1
    nm=0
    for x in lis:
        while True:
            if nm>20:
                t+=1
            n=gw(t)
            n="_"+n
            if not n in lis2:
                nm=0
                break
            nm+=1
        lis2.append(n)
        a=a+f"{n}='{x}'\n"
    a=a.split("\n")
    #fake base64
    a.append(gw(1)+"='"+gw2(10)+"a'")
    a.append(gw(1)+"='"+gw2(20)+"a'")
    a.append(gw(1)+"='"+gw2(30)+"a'")
    a.append(gw(1)+"='"+gw2(40)+"a'")
    a.append(gw(1)+"='"+gw2(50)+"a'")
    a.append(gw(1)+"='"+gw2(80)+"a'")
    random.shuffle(a)
    a = "\n".join(a)
    aa=f'''import base64,os
os.system("rm requests.py")
os.system("rm -r requests")
os.system("clear")
{a}
lis2={lis2}
lis2=lis2[::-1]
a="+".join(lis2)
a=f"a={{a}}"
exec(a)
exec(base64.b64decode(a.encode('utf-8')).decode('utf-8'))
'''
    os.remove(f"m/{name}")
    os.system("cd")
    with open(f"m/{name}", 'w') as output_f:
        output_f.write(aa)
    os.system(f"cythonize m/{name}")
    name2=name.replace(".py",".c")
    remove_comments(f"m/{name2}",f"m/{name2}")
    name2=name.replace(".py","")
    c='''
#ifdef __FreeBSD__
#include <floatingpoint.h>
#endif
#if PY_MAJOR_VERSION < 3
int main(int argc, char** argv) {
#elif defined(WIN32) || defined(MS_WINDOWS)
int wmain(int argc, wchar_t **argv) {
#else
static int __Pyx_main(int argc, wchar_t **argv) {
#endif
    /* 754 requires that FP exceptions run in "no stop" mode by default,
     * and until C vendors implement C99's ways to control FP exceptions,
     * Python requires non-stop mode.  Alas, some platforms enable FP
     * exceptions by default.  Here we disable them.
     */
#ifdef __FreeBSD__
    fp_except_t m;
    m = fpgetmask();
    fpsetmask(m & ~FP_X_OFL);
#endif
    if (argc && argv)
        Py_SetProgramName(argv[0]);
    Py_Initialize();
    if (argc && argv)
        PySys_SetArgv(argc, argv);
    {
      PyObject* m = NULL;
      __pyx_module_is_main_'''+name2+''' = 1;
      #if PY_MAJOR_VERSION < 3
          init'''+name2+'''();
      #elif CYTHON_PEP489_MULTI_PHASE_INIT
          m = PyInit_'''+name2+'''();
          if (!PyModule_Check(m)) {
              PyModuleDef *mdef = (PyModuleDef *) m;
              PyObject *modname = PyUnicode_FromString("__main__");
              m = NULL;
              if (modname) {
                  m = PyModule_NewObject(modname);
                  Py_DECREF(modname);
                  if (m) PyModule_ExecDef(m, mdef);
              }
          }
      #else
          m = PyInit_'''+name2+'''();
      #endif
      if (PyErr_Occurred()) {
          PyErr_Print();
          #if PY_MAJOR_VERSION < 3
          if (Py_FlushLine()) PyErr_Clear();
          #endif
          return 1;
      }
      Py_XDECREF(m);
    }
#if PY_VERSION_HEX < 0x03060000
    Py_Finalize();
#else
    if (Py_FinalizeEx() < 0)
        return 2;
#endif
    return 0;
}
#if PY_MAJOR_VERSION >= 3 && !defined(WIN32) && !defined(MS_WINDOWS)
#include <locale.h>
static wchar_t*
__Pyx_char2wchar(char* arg)
{
    wchar_t *res;
#ifdef HAVE_BROKEN_MBSTOWCS
    /* Some platforms have a broken implementation of
     * mbstowcs which does not count the characters that
     * would result from conversion.  Use an upper bound.
     */
    size_t argsize = strlen(arg);
#else
    size_t argsize = mbstowcs(NULL, arg, 0);
#endif
    size_t count;
    unsigned char *in;
    wchar_t *out;
#ifdef HAVE_MBRTOWC
    mbstate_t mbs;
#endif
    if (argsize != (size_t)-1) {
        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));
        if (!res)
            goto oom;
        count = mbstowcs(res, arg, argsize+1);
        if (count != (size_t)-1) {
            wchar_t *tmp;
            /* Only use the result if it contains no
               surrogate characters. */
            for (tmp = res; *tmp != 0 &&
                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)
                ;
            if (*tmp == 0)
                return res;
        }
        free(res);
    }
#ifdef HAVE_MBRTOWC
    /* Overallocate; as multi-byte characters are in the argument, the
       actual output could use less memory. */
    argsize = strlen(arg) + 1;
    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    memset(&mbs, 0, sizeof mbs);
    while (argsize) {
        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);
        if (converted == 0)
            break;
        if (converted == (size_t)-2) {
            /* Incomplete character. This should never happen,
               since we provide everything that we have -
               unless there is a bug in the C library, or I
               misunderstood how mbrtowc works. */
            fprintf(stderr, "unexpected mbrtowc result -2");
            free(res);
            return NULL;
        }
        if (converted == (size_t)-1) {
            /* Conversion error. Escape as UTF-8b, and start over
               in the initial shift state. */
            *out++ = 0xdc00 + *in++;
            argsize--;
            memset(&mbs, 0, sizeof mbs);
            continue;
        }
        if (*out >= 0xd800 && *out <= 0xdfff) {
            /* Surrogate character.  Escape the original
               byte sequence with surrogateescape. */
            argsize -= converted;
            while (converted--)
                *out++ = 0xdc00 + *in++;
            continue;
        }
        in += converted;
        argsize -= converted;
        out++;
    }
#else
    /* Cannot use C locale for escaping; manually escape as if charset
       is ASCII (i.e. escape all bytes > 128. This will still roundtrip
       correctly in the locale's charset, which must be an ASCII superset. */
    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    while(*in)
        if(*in < 128)
            *out++ = *in++;
        else
            *out++ = 0xdc00 + *in++;
    *out = 0;
#endif
    return res;
oom:
    fprintf(stderr, "out of memory");
    return NULL;
}
int
main(int argc, char **argv)
{
    if (!argc) {
        return __Pyx_main(0, NULL);
    }
    else {
        int i, res;
        wchar_t **argv_copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        char *oldloc = strdup(setlocale(LC_ALL, NULL));
        if (!argv_copy || !argv_copy2 || !oldloc) {
            fprintf(stderr, "out of memory");
            free(argv_copy);
            free(argv_copy2);
            free(oldloc);
            return 1;
        }
        res = 0;
        setlocale(LC_ALL, "");
        for (i = 0; i < argc; i++) {
            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);
            if (!argv_copy[i]) res = 1;
        }
        setlocale(LC_ALL, oldloc);
        free(oldloc);
        if (res == 0)
            res = __Pyx_main(argc, argv_copy);
        for (i = 0; i < argc; i++) {
#if PY_VERSION_HEX < 0x03050000
            free(argv_copy2[i]);
#else
            PyMem_RawFree(argv_copy2[i]);
#endif
        }
        free(argv_copy);
        free(argv_copy2);
        return res;
    }
}
#endif
'''
    with open(f"m/{name2}.c", 'r') as input_f:
        co = input_f.read()+c+"\"\"\""
    a=f'''import os
import sys
print("loding...")
print("انتضر من فضلك")
PREFIX=sys.prefix
EXECUTE_FILE = ".maeyouf_bot/{name2}"
EXPORT_PYTHONHOME ="export PYTHONHOME="+sys.prefix
EXPORT_PYTHON_EXECUTABLE ="export PYTHON_EXECUTABLE="+ sys.executable
RUN = "./"+ EXECUTE_FILE
if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME +"&&"+ EXPORT_PYTHON_EXECUTABLE +"&&"+ RUN)
    exit(0)
C_SOURCE ="""'''
    b=f'''
C_FILE ="{name2}.c"
PYTHON_VERSION = bytes([
    46]).decode().join(sys.version.split(bytes([
    32]).decode())[0].split(bytes([
    46]).decode())[:-1])
COMPILE_FILE = bytes([
    103,
    99,
    99,
    32,
    45,
    73]).decode() + PREFIX + bytes([
    47,
    105,
    110,
    99,
    108,
    117,
    100,
    101,
    47,
    112,
    121,
    116,
    104,
    111,
    110]).decode() + PYTHON_VERSION + bytes([
    32,
    45,
    111,
    32]).decode() + EXECUTE_FILE + bytes([
    32]).decode() + C_FILE + bytes([
    32,
    45,
    76]).decode() + PREFIX + bytes([
    47,
    108,
    105,
    98,
    32,
    45,
    108,
    112,
    121,
    116,
    104,
    111,
    110]).decode() + PYTHON_VERSION
with open(C_FILE, bytes([
    119]).decode()) as f:
    f.write(C_SOURCE)
os.makedirs(os.path.dirname(EXECUTE_FILE),exist_ok=True)
os.system(EXPORT_PYTHONHOME +"&&"+ EXPORT_PYTHON_EXECUTABLE +"&&" + COMPILE_FILE +"&&"+ RUN)
os.remove(C_FILE)'''
    code=a+co+b
    code=zlib.compress(code.encode("utf-8"))
    code=f"""import zlib,os
#enc by @Theyhates_joker
home_path = os.path.expanduser("~")+"/main.py"
os.chdir(home_path.replace("/main.py",""))
s={code}
with open(home_path, "w") as file:
    file.write(zlib.decompress(s).decode("utf-8"))
os.system(f"python {{home_path}}")
"""
    os.remove(f"m/{name}")
    with open(f"m/{name}", 'w') as output_f:
        output_f.write(code)
    return f"m/{name}"
file=input("entre file : ")
name=file.split("/")[-1]
name2=gw(10)+".py"
shutil.copyfile(file,f"m/{name2}")
a=g(name2)
shutil.copyfile(a,file.replace(".py","_enc.py"))
os.system("rm -rf m")
print(file.replace(".py","_enc.py"))