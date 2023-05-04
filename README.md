# Project for Professor Sopher

To run, make sure python is installed, and there is an instance of MongoDB running. 

Activate the virtualenv with the command:
```shell
activate /env/bin/activate.{shell that you are using}
```

To run the app, use the command:
```shell
streamlit run mongoTest.py
```

If you need to change the connection string, do so in the the mongoTest.py file.

To run mongodb locally with docker, navigate to the docker folder and:
```shell
start.sh
```
***Note: this command only works when running bash or zsh, if using a shell such as fish, run the commands below***
```shell
bash
start.sh
```

