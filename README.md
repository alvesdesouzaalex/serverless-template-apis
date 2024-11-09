mkdir seuapp
cd seuapp  //create virtualenv, activate it
virtualenv venv -p python3
. venv/bin/activate.fish //install Flask and freeze requirements
(venv) pip install Flask
(venv) pip freeze > requirements.txt


```shell
virtualenv venv -p python3
```

```shell
sudo apt install python3-virtualenv
```

```shell
. venv/bin/activate.fish
```

```shell
 . venv/bin/activate
```


```shell
pip install --upgrade pip
```

```shell
pip install Flask
```

```shell
pip freeze > requirements.txt 
```

## Install all dependencies
```shell
npm install
```

## Install Serverless
```shell
npm install -g serverless
```

### Running the server
```shell
sls wsgi serve
```

### Nao precisa deste abaixo pois o profile ja esta declarado no serverless.yml
sls deploy --aws-profile profileName


### Usar este abaixo para deploy
sls deploy

```shell
sls deploy --stage dev
```


```shell
sls deploy --stage prod
```


### Libs
pip3 install Flask
pip3 install psycopg2-binary

pip freeze > requirements.txt 


 rm -rf quotes/
  384  mkdir quotes
  385  cd quotes/
  386  virtualenv venv -p python3
  387  sudo apt install python3-virtualenv
  388  virtualenv venv -p python3
  389  . venv/bin/activate.fish
  390  virtualenv venv -p python3
  391  ls
  392  . venv/bin/activate
  393  pip install Flask
  394  ls
  395  pip freeze > requirements.txt       # Assim que instalar uma dependencia rodar esse comando para jogar a dependencia no requirements e logo depois ser compilado no deploy
  396  ls
  397  cat requirements.txt 
  398  touch main.py
  399  ls
  400  nano main.py 
  401  run serverless wsgi serve
  402  serverless wsgi serve
  403  sls wsgi serve






serverless invoke local --function cronHandler



