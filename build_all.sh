python -m venv .env
source .env/bin/activate

cd ig-annotator
python setup.py sdist
pip install dist/*
rm -rf dist/
rm -rf *egg-info/
pip install -r requirements.txt
cd ..

cd MAE_to_CSV/src
python setup.py sdist
pip install dist/*
rm -rf dist/
rm -rf *egg-info/
cd ..
pip install -r requirements.txt
cd ..