# Models
* Network 
* Hierarchical
* Relational (Pre-eminent type for general purpose dbs)
* et.c

Choice of model depends on requirements (performance, scalabilty et.c)

Applications of models other than relational:
* Search engine
* Fincancial trading
* Data mining

# Properties of a DB model
* Abstraction from hardware
* No data duplication
* Consistency

# Rules
* Atomicity: a transaction either happens or doesn't and doesn't find itself in a state inbetween those
* Consistency: A DB is always in a consistent state
* Isolation: Efect of two parallel operations is same as if they happened sequentially
* Durability: Once data is stored it shouldn't disappear

Databases are usually shielded behind some application or web interface for the purpose of convenience, abstraction and security.
