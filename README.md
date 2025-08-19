# RuLexNorm: A Lexical Normalization Dataset for Russian Social Media Text 


**RuLexNorm** — the first open dataset for lexical normalization of Russian-language social media texts. 
**Disclaimer:** This dataset contains real comments with explicit or potentially sensitive content.

## Description

- Dataset: The data/dataset/RuLexNorm.norm file contains the core dataset of over 6,000 Russian text pairs from Twitter (X), mapping informal utterances to their normalized equivalents.
- Model: A baseline Transformer-based model for automatic lexical normalization of Russian social media text.

## Data Format

The dataset is provided in a data/dataset/RuLexNorm.norm file. The corpus is organized into entries separated by blank lines. Each entry consists of one or more lines representing a single text pair.

Each line within an entry follows this structure:
*   **Original token** `[TAB]` **Normalized form**

The normalization can be of three types:
1.  **One-to-One (1-1):** A single token is normalized to a single word.
   ```
   Прив! \t Привет!
   ```
2.  **One-to-Many (1-N):** A single token is normalized to multiple words, separated by a space.
   ```
   Чд? \t Что делаешь?
   ```
3.  **Many-to-One (N-1):** Multiple consecutive tokens are merged into a single normalized form. The normalization is provided for the first token, and subsequent tokens in the sequence have an empty string as their normalized form.
   ```
   Чуть \t Чуть-чуть
   чуть \t
   ```

## Citing work

- Irina Koliaskina
- Dmitry Sholomov

## Citing work

If you use the **RuLexNorm** corpus, please cite the following paper:

TODO

## License

This work is licensed under the Creative Commons Attribution-ShareAlike 2.5 Generic License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/2.5/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

---

For any questions or suggestions, please contact Irina Koliaskina (ira.koliaskian@mail.com)
