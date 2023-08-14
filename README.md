## String Matching - RegEx.

## Pattern Syntax

The supported metacharacters in the pattern include:

- `.` (dot): Matches any single character except a newline.
- `*`: Matches zero or more occurrences of the preceding character or group.
- `+`: Matches one or more occurrences of the preceding character or group.
- `?`: Matches zero or one occurrence of the preceding character or group.
- `^`: Specifies the beginning of a line or string.
- `$`: Specifies the end of a line or string.
- `(` and `)`: Groups multiple characters or expressions together.
- `|`: Represents alternation, allowing either of the provided patterns to be matched.
- `[` and `]`: Defines a character class, matching any single character inside the brackets.

## Example

Let's say you want to find occurrences of the pattern `a.*b|(c|d)[0-9]` in the text `azb a1b c7d89 c2b a3b`.

1. Put the pattern `a.*b|(c|d)[0-9]` in `pattern.txt`.
2. Put the text `azb a1b c7d89 c2b a3b` in `text.txt`.
3. Run the program using the command `python string_matcher.py`.

After running the program, an `output.txt` file will be generated with the positions where the pattern is found in the text.

## Note

- Modify `pattern.txt` and `text.txt` with your desired pattern and text.
- Regular expressions can be powerful but might require escaping special characters. Make sure to adjust the pattern accordingly.
- This program provides a basic example of regex pattern matching. For more complex scenarios, consider using established libraries like `re` in Python.

```
Pattern found at positions: 0, 4, 11, 15, 18
```

Please replace placeholders like `pattern.txt` and `text.txt` with the actual filenames you're using. This README provides a basic template, so feel free to add more details if needed.
```
