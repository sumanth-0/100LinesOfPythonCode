Random plots utility

Usage:

1. Create a virtual environment (recommended):

   python -m venv .venv
   source .venv/bin/activate

2. Install dependencies:

   pip install -r requirements.txt

3. Run the script:

   python random_plots.py --count 2000 --seed 42 --outdir output

It will create `histogram.png` and `scatter.png` in the output directory.
