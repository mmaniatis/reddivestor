# Reddivestor

Currently running in AWS via Elastic Beanstalk

Micro-Service that will scrape/crawl reddit looking for mentions of crypto currencies (this list comes from CoinMarketCap API.)

It will then process the mentions into a hash table containing the coin name, and the count. 

From here it will insert said hash table information into a persisted data structure.

There will be a seperate micro service API that will access table. It's out of scope for this crawler. 


Instructions to use:

You will need two ENV Variables:

  MONGO_PASSWORD
  COINMARKETCAP_API_KEY

From here you can do typical docker commands. export such as,


git clone
docker build -t image_name .

export MONGO_PASSWORD=YOUR_PASS
export COINMARKETCAP_API_KEY=YOUR_KEY

docker run -e MONGO_PASSWORD -e COINMARKETCAP_API_KEY image_name

or 

docker run --env-list .env image_name (add to .env file)
