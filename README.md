# CloudletEngine
Platform for writing bots for VK `Python 3.8+`

### Installing this project
```shell
git clone https://github.com/SekaiTeam/cloudlet_engine.git
```

Install all the necessary packages to work with the project:
```shell
pip install -r requirements.txt
```

configure the environment variables:
```shell
cp example.env .env
nano .env
```

At the end, configure the connection to the database and run the migrations command:
```shell
python manage.py migrate
```

### Run bot

To start the bot, use the command:
```shell
python manage.py startbot
```
