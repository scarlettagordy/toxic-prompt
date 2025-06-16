Week 1 Research Log

 Goals
- Understand the paper: "You Only Prompt Once".
- Set up local environment.
- Run and evaluate Detoxify model.
- Begin setting up GitHub documentation and syncing code.

 Summary of Activities
- Read and summarized the paper’s methodology and results.
- Successfully set up Python virtual environment.
- Installed required packages (e.g., Detoxify, Transformers).
- Created and tested `3_perspective_evaluation.py` using Detoxify for offline toxicity scoring.
- Evaluated example outputs and confirmed the expected behavior of Detoxify scoring.
- Set up personal GitHub repo at: [https://github.com/scarlettagordy/toxic-prompt](https://github.com/scarlettagordy/toxic-prompt)
- Resolved Git merge conflict and synced all code and outputs.

 Results
Sample output from Detoxify:
	Text: You're disgusting and I hate you!
	Toxicity Score: 0.9912

	Text: I hope you have a great day!
	Toxicity Score: 0.0008

	Text: Everyone like you is worthless.
	Toxicity Score: 0.9492

 Next Week's Plan
- Identify suitable datasets used in the paper (e.g., HateXplain, ParaDetox).
- Explore running `1_toxicity_classification.py` using provided input files.
- Review original evaluation scripts and compare output interpretation steps.
- Begin modifying or replacing code as needed to replicate paper’s results.

