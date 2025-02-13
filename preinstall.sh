# run this shell script after you activate the virtual environment
pip install -r requirements.txt

# install pytest and pylint just in case if requirements.txt doesn't download them
pip install -U pytest
pip install pylint

# install npm packages if you want to deploy the bot on AWS Lambda
npm install