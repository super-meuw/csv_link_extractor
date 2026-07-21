```markdown
# 🐱 CSV Link Extractor

**Clean URL extraction from CSV files - nothing more, nothing less.**

<div align="center">

```

  ,_         _,
   |\\.-"""-.//|
   \`         `/
  /    _   _    \
  |    a _ a    |
  '.=    Y    =.'
    >._  ^  _.<
   /   `````   \
   )           (
  ,(           ),
 / )   /   \   ( \
 ) (   )   (   ) (
 ( )   (   )   ( )
 )_(   )   (   )_(-.._
(  )_  (._.)  _(  )_, `\
 ``(   )   (   )`` .' .'
    ```     ```   ( (`
                   '-'
                                                                                

CSV Link Extractor v2.0

   by super-meuw

```

</div>

---

## 📋 Description

CSV Link Extractor is a lightweight, focused tool that extracts **only the URLs** from CSV files. Perfect for security researchers, data analysts, and anyone who needs clean URL lists without the clutter.

### What it does:
- ✅ Extracts URLs from CSV files
- ✅ Identifies the correct column automatically
- ✅ Removes duplicates
- ✅ Outputs clean URLs only (no IPs, ports, or metadata)
- ✅ Generates timestamped filenames
- ✅ Handles multiple encoding formats
- ✅ No external dependencies

---

## 🚀 Installation

No installation required! Just download the script and run it with Python 3.

```bash
# Download the script
wget https://your-server/csv_link_extractor.py

# Or clone the repository
git clone https://github.com/super-meuw/csv-link-extractor.git
cd csv-link-extractor

# Make it executable (Linux/Mac)
chmod +x csv_link_extractor.py
```

---

## 💻 Usage

### Basic Usage

```bash
python csv_link_extractor.py your_file.csv
```

### Example

```bash
python csv_link_extractor.py Asset-Data.csv
```

### Output

The script creates a file named: `extracted_links_YYYYMMDD_HHMMSS.txt`

**Input CSV:**
```csv
host,ip,port,protocol,title,domain,country,city,link,org
https://example.com,192.168.1.1,443,https,My Site,example.com,US,NY,https://example.com,MyOrg
https://another.org,10.0.0.5,80,http,Another,another.org,UK,LDN,https://another.org,OtherOrg
```

**Output TXT:**
```
https://example.com
https://another.org
```

---

## 🔧 Features

| Feature | Description |
|---------|-------------|
| **Smart Column Detection** | Automatically finds the URL column (link, url, website, domain) |
| **Duplicate Removal** | No duplicate URLs in output |
| **Clean Output** | Only URLs, no additional text or formatting |
| **Timestamped Files** | Never overwrite previous exports |
| **Error Handling** | Gracefully handles malformed CSV |
| **Multi-Encoding** | Supports UTF-8, UTF-8-SIG, Latin-1, and more |
| **Lightweight** | No external dependencies, uses only built-in modules |
| **Cross-Platform** | Works on Windows, Linux, and macOS |

---

## 📁 Supported Input Formats

- ✅ Standard CSV (comma-separated)
- ✅ TSV (tab-separated) 
- ✅ Semi-colon separated
- ✅ Any delimiter that Python's `csv` module can detect
- ✅ Files with BOM (Byte Order Mark)
- ✅ Files without headers (fallback mode)

---

## 🎯 Use Cases

1. **Security Research** - Extract target domains from asset lists
2. **Data Analysis** - Clean URL extraction from messy datasets
3. **Web Scraping** - Prepare seed URLs for crawlers
4. **Reconnaissance** - Build target lists from CSV exports
5. **Automation** - Pipeline integration for processing tasks
6. **Bug Bounty** - Extract targets from scope files
7. **OSINT** - Gather URL lists from various data sources

---

## ⚙️ Technical Details

- **Language:** Python 3.6+
- **Dependencies:** None (uses built-in modules only)
- **Encoding:** Auto-detects UTF-8, UTF-8-SIG, and Latin-1
- **Regex:** Pattern matches `http://` and `https://` URLs
- **Performance:** Processes files of any size efficiently
- **Memory Usage:** Minimal, streams data when possible

---

## 🛠️ Customization

### Change Output Filename Pattern

Edit the `generate_output_filename()` function:

```python
def generate_output_filename():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"my_custom_name_{timestamp}.txt"
```

### Change URL Detection Pattern

Modify the regex pattern in `extract_all_urls_from_text()`:

```python
url_pattern = r'https?://[^\s<>"\'{}|\\^`\[\],]+'  # Default
```

### Add Custom Column Names

Modify the column detection list in `extract_links_manual()`:

```python
if col.strip().lower() in ['link', 'url', 'website', 'domain', 'custom_column']:
    link_index = i
    break
```

---

## 📂 File Structure

```
csv-link-extractor/
├── csv_link_extractor.py   # Main script
├── README.md              # This file
├── LICENSE                # MIT License
├── example.csv            # Sample input file
└── extracted_links_*.txt  # Output files (generated)
```

---

## 🐛 Troubleshooting

### Issue: "Column 'link' not found"
**Solution:** The script will automatically try to find columns named `url`, `website`, or `domain`. If none exist, it will use fallback mode to extract all URLs.

### Issue: "UnicodeDecodeError"
**Solution:** The script tries multiple encodings automatically (UTF-8, UTF-8-SIG, Latin-1). If you still get errors, try:

```bash
python csv_link_extractor.py your_file.csv
```

### Issue: No URLs found
**Solution:** 
- Check if your CSV actually contains URLs
- URLs must start with `http://` or `https://`
- Try the fallback mode by removing the header

### Issue: Wrong URLs extracted
**Solution:** The script only extracts URLs from the 'link' column. If your URLs are in a different column, rename the column header to 'link'.

---

## 📊 Output Examples

### Sample Input (CSV):
```csv
host,ip,port,protocol,title,domain,country,city,link,org
https://site1.com,192.168.1.1,443,https,Title1,site1.com,US,NY,https://site1.com,Org1
https://site2.org,10.0.0.1,80,http,Title2,site2.org,UK,LDN,https://site2.org,Org2
http://site3.net,172.16.0.1,8080,http,Title3,site3.net,DE,BER,http://site3.net,Org3
```

### Sample Output (TXT):
```
https://site1.com
https://site2.org
http://site3.net
```

---

## 🔒 Security Considerations

- The script only reads files, never modifies them
- No external network calls are made
- All processing happens locally
- No data is sent anywhere

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Coding Standards
- Follow PEP 8
- Add comments for complex logic
- Update README.md if needed
- Test with various CSV formats

---

## 📜 License

MIT License

Copyright (c) 2026 super-meuw

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 👤 Author

**super-meuw**

---

## 🌟 Support

If you find this tool useful:
- ⭐ Star the repository on GitHub
- 🐛 Report issues
- 💡 Suggest features
- 📢 Share with others

---

## 📝 Changelog

### v2.0.0 (2026-07-20)
- Complete code rewrite
- Smart column detection
- Timestamped output files
- Better error handling
- Multi-encoding support
- Professional documentation

### v1.0.0 (2026-07-19)
- Initial release
- Basic URL extraction
- Duplicate removal

---

## 🙏 Acknowledgments

- Python community for the excellent standard library
- All contributors and users
- Open source community

---

<div align="center">

**Made with by super-meuw**



</div>
```
