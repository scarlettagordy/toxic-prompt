Week 2

This week, I encountered significant technical roadblocks using the Perspective Comment Analyzer API, despite enabling billing and following Google Cloud's documentation. Persistent “Failed to load” and HTTP 403 errors prevented successful usage of the API. After attempting various workarounds including billing verification, project switching, and using different browsers, I pivoted to using Detoxify as a local evaluation method.

I wrote a new evaluation script (`3_perspective_evaluation_detoxify.py`) and installed the necessary packages including `pandas`. Then, I evaluated the `sample_outputs.txt` file, which contains original and generated prompt outputs, using Detoxify. The resulting toxicity scores were saved to `detoxify_results.csv`.

This solution was effective because it removed all reliance on unstable external APIs and allowed for faster and more reproducible local testing. The output will serve as the toxicity baseline for comparing against future detoxified outputs.

