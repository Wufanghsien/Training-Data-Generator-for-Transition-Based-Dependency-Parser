# Transition-Based Dependency Parser
 
A Python implementation of a transition-based dependency parser trained on CoNLL-U treebank data. This project includes non-projective tree detection as a preprocessing step, and a test suite validating the parser's correctness across multiple languages
## Authors 
- [@vx6701](https://github.com/vx6701)
- [@Wufanghsien](https://github.com/Wufanghsien)
## Project Overview
This project takes a dependency treebank in **CoNLL-U format** and produces a dataset suitable for training a delexicalized transition-based parser using a gold-standard oracle.
## How It Works
 
### Part 1: Non-Projective Tree Detection
 
The transition system used in this project (arc-standard) only works correctly with **projective** dependency trees.
 
A tree is **projective** if, for every arc from a head to a dependent, all words that appear between them in the sentence are also descendants of that head. If any arc "crosses" another, the tree is non-projective and must be skipped.
### Part 2: Oracle and Feature Extraction
The oracle simulates the arc-standard transition system step by step on a gold-standard tree, recording features and the correct action at each step.
 
**The transition system operates on two data structures:**
 
- **Stack (σ)** — tokens that have been partially processed
- **Buffer (β)** — tokens yet to be processed

**At each step, the oracle picks one of three actions:**
 
| Condition | Action |
|-----------|--------|
| Gold tree has a **left arc** from β0 → σ0 | `left-arc(label)` |
| Gold tree has a **right arc** from σ0 → β0, and **all children of β0 are already attached** | `right-arc(label)` |
| Neither condition is met | `shift` |

**Features extracted at each step (`get_features`):**
 
At every parsing step, two features are recorded alongside the action taken:
 
- **POS tag of σ0** — the top of the stack
- **POS tag of β0** — the next token in the buffer

**Example output:**

Given the sentence *"She saw him"*, the oracle might produce:
```  
Features:               Target class
[['ROOT', 'PRON'],      ['shift',
 ['PRON', 'VERB'],       'left-arc(nsubj)',
 ['ROOT', 'VERB'],       'shift',
 ['VERB', 'NOUN']]       'right-arc(obj)']
 ['ROOT', 'VERB']]       'right-arc(root)']
```
### Part 3: Test
Tests are written using [pytest](https://docs.pytest.org/) and cover:
 
- **Projective trees** — English, Spanish, and French sentences expected to return `True`
- **Non-projective trees** — sentences with crossing arcs expected to return `False`
- **Edge cases** — single-token sentences and root-only trees
- **Oracle actions** — verifying the correct sequence of parser actions for known example sentences
