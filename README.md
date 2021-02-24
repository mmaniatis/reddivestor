# Reddivestor

Micro-Service that will scrape/crawl reddit looking for mentions of crypto currencies (this list comes from CoinMarketCap API.)

It will then process the mentions into a hash table containing the coin name, and the count. 

From here it will insert said hash table information into a persisted data structure.

There will be a seperate micro service API that will access table. It's out of scope for this crawler. 


Instructions to use:

CONDA:
  1. conda create env -f environment.yml (Maybe you need to change the prefix on that file.. check to see)
  2. conda activate your_env (<-- from prefix)
  3. python3 main.py

DOCKER:

  docker build -t reddivestor .
  docker run reddivestor
 
