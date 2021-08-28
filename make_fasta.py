#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from pathlib import Path
from collections import defaultdict

files = list(Path(".").glob("*.csv.*"))
outputs = defaultdict(lambda: [])

for file in files:
    curr_df = pd.read_csv(file)
    for index, row in curr_df.iterrows():
        outputs[row["Pool name"]].append(row["Sequence"])

for pool, sequences in outputs.items():
    with open(f"{pool}.fasta", "w") as f:
        for i, seq in enumerate(sequences):
            f.write(f">{pool}_{i}\n")
            f.write(f"{seq}\n")
        
