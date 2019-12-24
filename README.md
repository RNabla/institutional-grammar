# institutional-grammar

This repository merges multiple modules that were created during `Text Mining` project regarding `Institutional grammar` in `Faculty of Mathematics and Information Science` of `Warsaw Univeristy of Technology`.

## Installation

Prerequisted:

- `python` points to Python 3.6+
- `pip` points to Pip for Python 3.6+

1. Install virtual environment

```bash
python -m venv venv
source venv/bin/activate
```
2. Run installation script

```bash
chmod +x ./build_all.sh
sudo -H ./build_all.sh
```

## Scripts

### ig-annotator

This script takes single text file and creates mae file that contains annotations in `institutional grammar` that was specified during classes.

```bash
ig_annotator INPUT_FILE OUTPUT_FILE
```

- INPUT_FILE - path to text file containing document to annotate
- OUTPUT_FILE - path to output file where mae file will be created; if provided file exists than it will be overwritten

### 



### ig

This script executes whole annotation pipeline. Script takes single text file and produces annotation results in provided output directory.

```bash
ig INPUT_FILE OUTPUT_DIR
```

- INPUT_FILE - path to text file containing document to annotate
- OUTPUT_DIR - path to output directory where annotation results will be saved; if directory already exists then content will be overwritten


