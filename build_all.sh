python -m venv .env
source .env/bin/activate

cd ig-annotator
chmod +x ./build.sh
./build.sh
cd ..


cd ig-cogito
chmod +x ./build.sh
./build.sh
cd ..

cd ig-relations
chmod +x ./build.sh
./build.sh
cd ..
