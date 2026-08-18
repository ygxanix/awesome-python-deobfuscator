#!/data/data/com.termux/files/usr/bin/bash
bin_dir=/data/data/com.termux/files/usr/bin/
git_pycdc_link=https://github.com/zrax/pycdc.git
git clone $git_pycdc_link
cd pycdc
cmake . && make
mv pycdc $bin_dir && mv pycdas $bin_dir
cd ..
rm -rf pycdc
chmod +x $bin_dir/pycdc $bin_dir/pycdas
echo all-done✅