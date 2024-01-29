# build_files.sh
pip install -r requirements.txt
source venv/bin/activate
python manage.py collectstatic