# crypto.bi CNT - Cardano Network Tools 

crypto.bi CNT implements parts of the Cardano network protocol in Python.

These tools allow you to listen in on the Cardano network and process messages. 

You can think of CNT as a network node implementation without a wallet and block generation components - just P2P networking code.

Network analysis is crucial to running a high performance staking pool. This is true for any [PoS cryptocurrency](https://crypto.bi/tape/pos/).

These tools can be used to measure node latency, to analyze the node graph and perform several other network tasks.

Example programs, with the `run_` prefix, are provided to quickly demonstrate how each library routine can be used,
so you can get up and running fast.   

## Documentation

Visit the official documentation at [crypto.bi CNT home](https://crypto.bi/tape/cnt/)

## Dependencies

Python 3.7+

Libs:

    sudo pip3 install grpc
     
## License

crypto.bi CNT is released under the GPL v3 license.

See COPYING file for details.

## Author

[Jose Fonseca](https://zefonseca.com/) is a contributor at [crypto.bi](https://crypto.bi/)