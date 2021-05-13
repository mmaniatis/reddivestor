FROM python

# Installing env dependencies for selenium:

# google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update --fix-missing
RUN apt-get install -y google-chrome-stable
# chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# copy reddivestor code base into working directory
COPY . /app
WORKDIR /app

# install dependencies from requirements.txt file
RUN pip install --upgrade pip
RUN python -m pip install -r requirements.txt

EXPOSE 80

RUN export MONGO_PASSWORD
RUN export COINMARKETCAP_API_KEY

# run python -u so we can see input.
CMD ["python3", "-u", "main.py"]



