
<div align="center">

# 🔐 dec64

[![PyPI version](https://badge.fury.io/py/dec64.svg)](https://badge.fury.io/py/dec64)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/dec64.svg)](https://pypi.org/project/dec64/)

Recursively decode Base64 encoded strings with ease.

[Installation](#installation) •
[Usage](#usage) •
[Contributing](#contributing) •
[License](#license)

</div>

---


## Description

dec64 is a Python library that allows you to recursively decode Base64 encoded strings. It's designed to be simple to use and integrate into your projects.

## Installation

You can install dec64 using pip:
```
pip install dec64
```

## Usage

Here's a basic example of how to use dec64:

In command line:
```
dec64 -t "SGVsbG8sIHdvcmxkIGZyb20gZGVjNjQh"
```

In code:

```python
from dec64 import Base64Decoder

decoder = Base64Decoder()

encoded_string = "SGVsbG8sIHdvcmxkIGZyb20gZGVjNjQh"
decoded_string = decoder.decode(encoded_string)

print(decoded_string)
```

## Features

* Recursively decode Base64 strings
* Handle errors gracefully
* Support for reading from files

## Requirements

* Python 3.6+

## License

This project is licensed under the MIT License.

## Author

[xdearboy](https://github.com/xdearboy)

## Links

[* GitHub Repository](https://github.com/xdearboy/dec64)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
