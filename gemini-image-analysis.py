import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def get_mime_type(extension):
    """Get the appropriate MIME type for the given file extension."""
    mime_types = {
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.webp': 'image/webp'
    }
    return mime_types.get(extension.lower(), 'image/jpeg')

def upload_to_gemini(path, mime_type=None):
    """Uploads the given file to Gemini."""
    file = genai.upload_file(path, mime_type=mime_type)
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file

def get_suggested_filename(response_text):
    """Extract the filename from the AI response."""
    # Remove special characters and get the first line that looks like a filename
    lines = response_text.split('\n')
    for line in lines:
        # Clean up the line and remove any markdown or special characters
        clean_line = line.strip().strip('*').strip('•').strip()
        if clean_line and not clean_line.startswith('Here') and not clean_line.lower().startswith('suggested'):
            return clean_line
    return None

def process_and_rename_images(folder_path):
    """Process images and rename them based on AI suggestions."""
    # Added WebP support
    supported_formats = ('.png', '.jpeg', '.jpg', '.webp')

    generation_config = {
        "temperature": 0.7,  # Reduced temperature for more focused responses
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        generation_config=generation_config,
        system_instruction="You are an image analysis expert. Analyze the image and respond with ONLY a single descriptive filename (no bullets, no explanations). The filename should be concise, relevant, and use hyphens between words. Do not include file extensions."
    )

    # Process each file in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(supported_formats):
            file_path = os.path.join(folder_path, filename)
            extension = os.path.splitext(filename)[1].lower()

            try:
                # Use the new get_mime_type function for proper MIME type detection
                mime_type = get_mime_type(extension)
                uploaded_file = upload_to_gemini(file_path, mime_type=mime_type)
                
                chat_session = model.start_chat()
                response = chat_session.send_message([
                    "Analyze this image and respond with a single descriptive filename (no explanations, no bullets).",
                    uploaded_file
                ])

                # Get the suggested filename
                new_name = get_suggested_filename(response.text)
                if new_name:
                    # Clean up the suggested name
                    new_name = new_name.replace(' ', '-').lower()
                    if not new_name.endswith(extension):
                        new_name += extension

                    # Create the new file path
                    new_path = os.path.join(folder_path, new_name)

                    # Rename the file
                    os.rename(file_path, new_path)
                    print(f"Renamed: {filename} -> {new_name}")
                else:
                    print(f"Could not process {filename}: No valid suggestion received")

            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

# Use the function
folder_path = "/path/to/your_folder"  # Update this path
process_and_rename_images(folder_path)
