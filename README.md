# Reddivestor
web crawler that will be used for a new app that tracks investments on reddit


Very early stages of development.. Just getting the crawler to be up and running, then the road map :

1. Refactor the crawler and implement unit tests
2. Begin saving the data in a persistent data store (MongoDB)
3. process the data
4. Create website / chrome app / some form of way to display processed info.


Instructions to use:

CONDA:
  1. conda create env -f environment.yml (Maybe you need to change the prefix on that file.. check to see)
  2. conda activate your_env (<-- from prefix)
  3. python3 main.py

DOCKER:

  docker build -t reddivestor .
  docker run reddivestor
 
