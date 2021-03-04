def generateSimpleTestHTML3Mentions(): 
    return "<html> \
                <h3>Ethereum is fantastic.</h3> \
                    <div> \
                    <div><p> Insert dummy text here </p> </div> \
                     </div> \
                <h3>I Like LINK because i like defi</h3> \
                    <div> \
                    <div><p> Do you like it too? </p> </div> \
                     </div> \
                <h3>I like coins</h3> \
                    <div> \
                    <div><p> LTC is great!</p> </div> \
                     </div> \
            </html>"

def generateTestCoinJSONResponse():
    return {'data': [{'name': 'Litecoin', 'symbol':'LTC'}, {'name': 'Ethereum', 'symbol':'ETH'}, {'name': 'Chainlink', 'symbol':'LINK'}] }