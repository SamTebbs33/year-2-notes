# Grammar
Classes:
	* Class 0: unrestricted phrase strucure grammars (no restriction on type of rules)
	* Class 1: context-sensitive grammars. Result of parsing can depend on some context (A -> B if x else C)
	* Class 2: context-free. Result of parsing does not depend on a context
	* Class 3: regular. A -> B | t, where A, B are non-terminals and T is terminal.

## Context-free grammars
Backus-Naur form devised by John Backus for ALGOL.
Formalised by Chomsky (1956). CFGs are separate from and are independent of their semantics.

Set of non-terminals that are composed of other rules and set of terminals that are composed of simple characters or regular expressions.
Start symbol and set of non-terminals of the form `A -> B`.

## Parsing
Grammars are only declarative specification and don't declare how parsing takes place.

* Top-down: Start with start symbol and terminate with terminals
* Bottom-up: Start with terminals and terminate with start symbol

## Good grammars
* Linguistic naturalness
* Mathematical power (if all sentences can be represented correctly)
* Computational efficiency
* Work well with new and unseen data

## Sentenc types
* Declarative: I like trains
* Imperatives: Board the train
* Yes/No questions: Do you like trains?
* Wh-question: Whay don't you like trains?
