# 🖼️ Gemini Image Analysis Tool

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Gemini API](https://img.shields.io/badge/Powered%20by-Google%20Gemini-4285F4.svg)](https://ai.google.dev/)

A powerful Python script that leverages Google's Gemini AI to automatically analyze images and rename them with descriptive, SEO-friendly filenames based on their visual content.

## ✨ Features

- 🤖 **AI-Powered Analysis**: Uses Google's advanced Gemini AI for accurate image content recognition
- 📁 **Batch Processing**: Automatically processes entire folders of images
- 🏷️ **Smart Naming**: Generates descriptive, hyphenated filenames suitable for web use
- 🔧 **Configurable**: Customizable AI parameters for different use cases
- 📊 **Progress Tracking**: Real-time feedback on processing status
- 🛡️ **Error Handling**: Robust error handling for failed processing attempts

## 🚀 Quick Start

### Prerequisites

- **Python 3.8 or higher**
- **Google Gemini API key** (free tier available at [Google AI Studio](https://makersuite.google.com/app/apikey))
- **Internet connection** for API calls

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/muhammedsamal/gemini-image-analysis.git
   cd gemini-image-analysis
   ```

2. **Install required dependencies**:
   ```bash
   pip install google-generativeai
   ```

3. **Set up your Gemini API key**:
   
   **Option A: Environment Variable (Recommended)**
   ```bash
   export GEMINI_API_KEY='your-api-key-here'
   ```
   
   **Option B: For Windows Command Prompt**
   ```cmd
   set GEMINI_API_KEY=your-api-key-here
   ```
   
   **Option C: For Windows PowerShell**
   ```powershell
   $env:GEMINI_API_KEY="your-api-key-here"
   ```

## 📖 Usage

### Basic Usage

1. **Update the folder path** in the script:
   ```python
   folder_path = "/path/to/your/images"  # Change this to your image folder
   ```

2. **Run the script**:
   ```bash
   python gemini-image-analysis.py
   ```

### Example

**Before:**
```
📁 my-photos/
├── IMG_001.jpg
├── DSC_0234.png
└── photo.jpeg
```

**After:**
```
📁 my-photos/
├── golden-retriever-playing-fetch-park.jpg
├── sunset-mountain-landscape-silhouette.png
└── family-dinner-birthday-celebration.jpeg
```

## 🎛️ Configuration

The script includes several configurable parameters in the `generation_config`:

```python
generation_config = {
    "temperature": 0.7,        # Creativity level (0.0-1.0)
    "top_p": 0.95,            # Nucleus sampling
    "top_k": 40,              # Top-k sampling
    "max_output_tokens": 8192, # Maximum response length
}
```

### Parameters Explained

- **Temperature** (0.7): Controls creativity. Lower = more consistent, Higher = more varied
- **Top P** (0.95): Probability threshold for token selection
- **Top K** (40): Limits vocabulary to top K tokens
- **Max Output Tokens**: Maximum length of generated filename

## 🗂️ Supported File Formats

- **PNG** (`.png`)
- **JPEG** (`.jpg`, `.jpeg`)

> **Note**: The script can be easily extended to support additional formats like WebP, GIF, or TIFF by modifying the `supported_formats` tuple.

## 🔧 Advanced Configuration

### Custom Folder Processing

You can modify the script to process multiple folders:

```python
folders = [
    "/path/to/folder1",
    "/path/to/folder2", 
    "/path/to/folder3"
]

for folder in folders:
    process_and_rename_images(folder)
```

### Custom System Instructions

Modify the AI's behavior by changing the system instruction:

```python
system_instruction = "You are an SEO expert. Create web-optimized filenames with relevant keywords..."
```

## 📊 API Usage and Limits

- **Free Tier**: 15 requests per minute, 1,500 requests per day
- **Paid Tier**: Higher rate limits available
- **File Size**: Maximum 20MB per image
- **Processing Time**: ~2-5 seconds per image

## 🛠️ Troubleshooting

### Common Issues

**Error: `google.api_core.exceptions.PermissionDenied`**
- Check your API key is correctly set
- Verify the API key has Gemini API access enabled

**Error: `FileNotFoundError`**
- Ensure the folder path exists and is accessible
- Check file permissions

**Error: `google.api_core.exceptions.ResourceExhausted`**
- You've hit the API rate limit
- Wait a few minutes or upgrade to paid tier

**Poor filename quality**
- Adjust the `temperature` parameter
- Modify the system instruction for more specific requirements
- Ensure images have clear, recognizable content

### Debug Mode

Add debug prints to troubleshoot issues:

```python
print(f"Processing: {filename}")
print(f"API Response: {response.text}")
```

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. **Report bugs** by opening an issue
2. **Suggest features** or improvements
3. **Submit pull requests** with enhancements
4. **Improve documentation**

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with a clear description

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Gemini AI** for providing the powerful image analysis capabilities
- **Community contributors** for suggestions and improvements

## 📞 Support

- 🐛 **Bug Reports**: [Open an Issue](https://github.com/muhammedsamal/gemini-image-analysis/issues)
- 💡 **Feature Requests**: [Open an Issue](https://github.com/muhammedsamal/gemini-image-analysis/issues)
- 📧 **Contact**: [muhammedsamalt@gmail.com](mailto:muhammedsamalt@gmail.com)

## 🔗 Related Projects

- [Google AI Studio](https://makersuite.google.com/) - Get your API key
- [Gemini API Documentation](https://ai.google.dev/docs) - Official documentation

---

⭐ **If this project helped you, please star the repository!** ⭐
