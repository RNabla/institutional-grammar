# institutional-grammar

This repository merges multiple modules that were created during `Text Mining` project regarding `institutional grammar` in `Faculty of Mathematics and Information Science` of `Warsaw Univeristy of Technology`.

## Installation

Prerequisted:

- `python` points to Python 3.6+
- `pip` points to Pip for Python 3.6+

1. Clone this repository

```bash
git clone https://github.com/RNabla/institutional-grammar --recurse-submodules
cd instititutional-grammar
```

2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

3. Run installation script

```bash
chmod +x ./build_all.sh
./build_all.sh
```

## Scripts

### ig_annotator

This script takes single text file and creates mae file that contains annotations in `institutional grammar` that was specified during classes.

```bash
ig_annotator INPUT_FILE OUTPUT_FILE
```

- INPUT_FILE - path to text file containing document to annotate
- OUTPUT_FILE - path to output file where mae file will be created; if file exists than it will be overwritten

### ig_xml_to_xls

This script takes single mae file and creates corresponding document in xls format.

```bash
ig_annotator MAE_FILE OUTPUT_FILE
```

- MAE_FILE - path to file containing annotated document in MAE format 
- OUTPUT_FILE - path to output file where xls file will be created; if file exists than it will be overwritten

### ig_cogito

This script takes annotated document in xls file and creates mapping for `aIm` category for each actor.

```bash
ig_annotator XLS_FILE OUTPUT_FILE
```

- XLS_FILE - path to file containing annotated document in XLS format 
- OUTPUT_FILE - path to output file where csv file will be created; if file exists than it will be overwritten

### ig_relations

This script takes csv file with normalized `aIm` category and creates relation matrices between `aCtor`s for given `aIm` category.

```bash
ig_relations file output
```

- file - path to csv file 
- output - path to directory where all relation matrices will be saved

### ig_visualization

This webpage helps visualize relations created by previous module.

### ig

This script executes all scripts specified above. Script takes single text file and produces annotation results in provided output directory.

```bash
ig INPUT_FILE OUTPUT_DIR
```

- INPUT_FILE - path to text file containing document to annotate
- OUTPUT_DIR - path to output directory where annotation results will be saved; if directory already exists then content will be overwritten
