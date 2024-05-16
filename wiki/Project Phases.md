
# Setup and Installation Phase

1. Install python3.12 

2. Create a virtual environment

```
python3 -m venv .venv

```

2. Activate the virtual env

```
source .venv/bin/activate
```

3. Install all dependencies for the project inside the virtual environment [Click here for more info about langflow](https://docs.langflow.org)

```
pip3 install langflow --pre --force-reinstall
```

# Prototype Phase

1. develop a prompt / instruction for the LLM to build an assistant (virtual bot of the person)

2. build a prototype virtual bot with default settings and attach resume of person as knowledge base

3. (optional) design a software architecture for backend 


# Backend Development Phase

1. develop the backend of application in python to interact with the virtual bot (based on software architecture)

2. (optional) design a software architecture for frontend


# Research Phase (API)

1. try out different APIs (like claude , bard , etc) for the backend application

2. develop the backend based on the API being used


# Research Phase (Virtual Bot)

1. try to use different prompting techniques to get better replies from the virtual bot

2. use different model parameters (temperature , max_length , top p ,etc )to get the desired answer for questions




