# myTools - Clipboard & Text Utilities

A collection of command-line utilities for manipulating clipboard text on Linux (using `wl-clipboard` for Wayland).

## 📋 Installation

### Requirements
- Python 3
- `wl-clipboard` (for Wayland clipboard operations)

```bash
# Arch Linux
sudo pacman -S wl-clipboard

# Ubuntu/Debian
sudo apt install wl-clipboard

# Fedora
sudo dnf install wl-clipboard
```

### Setup
Make scripts executable:
```bash
chmod +x *.py
```

Add to your PATH (optional):
```bash
# Add to ~/.bashrc or ~/.zshrc
export PATH="$PATH:/home/user/scripts/myTools"
```

---

## 📚 Scripts Reference

### 🔤 Text Transformation

#### `cc` - Convert Double Colons
**Functionality:** Converts `::` to `:&ZeroWidthSpace;:` (for Anki cloze cards)  
**Usage:**
```bash
./cc
```
**Example:** `test::double` → `test:&ZeroWidthSpace;:double`

---

#### `rna` - Remove ALL Newlines
**Functionality:** Removes all newlines (both single and double), flattening text into one paragraph  
**Usage:**
```bash
./rna
```
**Example:**
```
Input:  Line 1
        Line 2
        
        Paragraph 2
Output: Line 1 Line 2  Paragraph 2
```

---

#### `rnp` - Remove Single Newlines (Preserve Paragraphs)
**Functionality:** Removes single newlines but preserves double newlines (paragraph breaks)  
**Usage:**
```bash
./rnp
```
**Example:**
```
Input:  Line 1
        Line 2
        
        Paragraph 2
Output: Line 1 Line 2
        
        Paragraph 2
```

---

#### `c1` - Set Cloze Number
**Functionality:** Sets all Anki cloze numbers to a specified number (default: 1)  
**Usage:**
```bash
./c1 [number]
```
**Example:** `{{c3::answer}}` with `./c1 1` → `{{c1::answer}}`

---

#### `tc` - Transform to Title Case
**Functionality:** Converts text to Title Case (first letter of each word capitalized)  
**Usage:**
```bash
./tc
```
**Example:** `hello world` → `Hello World`

---

#### `code` - Transform Into Code (HTML)
**Functionality:** Wraps clipboard text in `<code>` tags  
**Usage:**
```bash
./code
```
**Example:** `example` → `<code>example</code>`

---

### 📝 Line Manipulation

#### `ba` - Bullet Point Adder
**Functionality:** Adds `* ` to the start of each line  
**Usage:**
```bash
./ba
```
**Example:**
```
Input:  Item 1
        Item 2
Output: * Item 1
        * Item 2
```

---

#### `bc` - Bullet Point Compacter
**Functionality:** Removes extra newlines between bullet points and cleans ChatGPT formatting  
**Usage:**
```bash
./bc
```

---

#### `sp` - Space Indenter
**Functionality:** Adds N spaces to the start of each line  
**Usage:**
```bash
./sp <number_of_spaces>
```
**Example:** `./sp 4` adds 4 spaces to each line

---

#### `cm` - Comment Text Block
**Functionality:** Adds comment prefixes to each line  
**Usage:**
```bash
./cm <comment_type>
```
**Supported types:**
- `/` - Adds `// ` (C/C++/JavaScript style)
- `#` - Adds `# ` (Python/Bash style)

**Example:** With `./cm #`:
```
Input:  code line 1
        code line 2
Output: # code line 1
        # code line 2
```

---

### 📊 Markdown Headers

#### `hp` - Header Plus (Push Down Header)
**Functionality:** Increases markdown header level (# → ##)  
**Usage:**
```bash
./hp
```
**Example:** `# Title` → `## Title`

---

#### `hm` - Header Minus (Push Up Header)
**Functionality:** Removes one `#` from markdown headers  
**Usage:**
```bash
./hm
```
**Example:** `# Title` → ` Title`

---

#### `eh` - Extract Headers
**Functionality:** Extracts module titles from markdown headers and formats them  
**Usage:**
```bash
./eh
```
**Example:**
```
Input:  ## Module 1: Foundations
        - HTTP protocol fundamentals
        ## Module 2: Basic Fetch Syntax
        - fetch() function signature
        
Output: # Foundations
        
        
        
        ---
        
        # Basic Fetch Syntax
        
        
        
        ---
```
**Use Case:** Converting outline structures into slide-ready markdown headers

---

### 🖼️ Image Processing

#### `attach_logo` - Batch Image Watermarking
**Functionality:** Adds PNG watermark overlays to a folder of images (.heic, .jpg, .jpeg, .png)  
**Usage:**
```bash
./attach_logo <input_directory>
./attach_logo <input_directory> --no-left   # Disable left watermark
./attach_logo <input_directory> --no-right  # Disable right watermark
```
**Features:**
- Supports HEIC, JPG, JPEG, PNG formats
- Adds two watermarks: logo (lower-left) and motto (lower-right)
- Preserves image quality (configurable JPEG quality)
- Outputs to `./with_logo/` directory
- Customizable watermark positions, sizes, and margins

**Example:**
```bash
./attach_logo ~/Photos/event_photos
```

**Configuration:** Edit script variables to customize:
- `OVERLAY_LEFT` / `OVERLAY_RIGHT` - Watermark PNG paths
- `MARGINL_X/Y` and `MARGINR_X/Y` - Position offsets
- `OVERLAY_HEIGHT_LEFT/RIGHT` - Watermark sizes (pixels)
- `OUTPUT_QUALITY` - JPEG quality (1-100, default: 100)

**Dependencies:**
```bash
pip install pillow pillow-heif
```

---

### �🛠️ Utilities

#### `bak` - Backup to ZIP
**Functionality:** Creates incremental ZIP backups of the current folder  
**Usage:**
```bash
./bak
```
**Note:** Windows-specific paths need to be updated for Linux

---

#### `mkbat` - Batch File Generator
**Functionality:** Generates `.bat` files for Python scripts in a folder  
**Usage:**
```bash
./mkbat <folder_path>
```
**Note:** Windows-specific, creates `.bat` launcher files

---

## 💡 File Names Explained

All scripts use ultra-short, intuitive names for quick typing:

| Name | Meaning | Function |
|------|---------|----------|
| `cc` | Colon Converter | Convert `::` for Anki |
| `rna` | Remove Newlines All | Flatten all text |
| `rnp` | Remove Newlines Preserve | Keep paragraphs |
| `c1` | Cloze 1 | Set Anki cloze numbers |
| `tc` | Title Case | Capitalize words |
| `code` | Code tags | Wrap in `<code>` |
| `ba` | Bullet Add | Add bullet points |
| `bc` | Bullet Compact | Clean bullet formatting |
| `sp` | Space/Indent | Add indentation |
| `cm` | Comment | Add comment prefixes |
| `hp` | Header Plus | Increase header level |
| `hm` | Header Minus | Decrease header level |
| `eh` | Extract Headers | Extract module titles |
| `bak` | Backup | Create ZIP backup |
| `mkbat` | Make Batch | Generate .bat files |

**Note:** Originally planned `h+` and `h-` but changed to `hp`/`hm` to avoid shell special characters.

---

## 🔄 Common Workflows

### Anki Card Creation
```bash
# Convert double colons for Anki
./cc

# Set all cloze deletions to number 1
./c1 1
```

### Text Cleanup
```bash
# Remove paragraph breaks
./rna

# Keep paragraphs but join wrapped lines
./rnp
```

### Markdown Formatting
```bash
# Add bullet points
./ba

# Clean up bullet point formatting
./bc

# Adjust header levels
./hp  # Make headers smaller (increase level)
./hm  # Make headers larger (decrease level)

# Extract module titles from outlines
./eh
```

### Code Formatting
```bash
# Add Python comments
./cm #

# Add C++ comments
./cm /

# Indent code blocks
./sp 4
```

---

## 📖 Notes

- All scripts read from and write to the system clipboard
- Scripts modified from Windows (pyperclip) to Linux (wl-clipboard) versions
- Original Windows implementations are preserved in comments within each file
- Most scripts operate silently; some provide success/error messages

---

## 🤝 Contributing

To add a new utility:
1. Follow the naming convention (short, intuitive)
2. Add usage info in the script header comments
3. Update this README with functionality and examples
4. Make it executable: `chmod +x script.py`

---

## 📜 License

Personal utility collection - use freely
