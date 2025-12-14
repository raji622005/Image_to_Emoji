import cv2
import argparse
import sys
import os # 🌟 NEW: For interacting with the operating system
from typing import List

# 1️⃣ Multi-level emoji gradient mapping (10 levels for better detail)
BRIGHTNESS_TO_EMOJI_GRADIENT = [
    "⚫", "🌑", "🌘", "🌗", "🌖", "🌕", "⚪", "◻️", "◽", "⬜" 
]
GRADIENT_LEVELS = len(BRIGHTNESS_TO_EMOJI_GRADIENT)
ASPECT_CORRECTION_FACTOR = 0.55

# --- Utility Functions (Modified/New) ---

# 🌟 NEW: Function to open the file
def open_file(file_path: str):
    """
    Opens the file in the user's default text editor/viewer, 
    simulating a 'download' for immediate access.
    """
    try:
        # Use 'start' for Windows, 'open' for macOS, 'xdg-open' for Linux
        if sys.platform == "win32":
            os.startfile(file_path)
        elif sys.platform == "darwin": # macOS
            os.system(f"open {file_path}")
        else: # Linux and other Unix-like systems
            os.system(f"xdg-open {file_path}")
        
        print(f"📂 Attempting to open '{file_path}' for viewing...")
    except Exception as e:
        print(f"⚠️ Could not automatically open file. Please find it manually: {e}", file=sys.stderr)


# 6️⃣ Modular code structure - Image Processing (Same as before)
def process_image(image_path: str, output_width: int) -> tuple[List[List[int]], int, int]:
    """Load, validate, convert to grayscale, and resize the image."""
    try:
        img = cv2.imread(image_path)
    except Exception as e:
        raise FileNotFoundError(f"Error loading image: {e}")

    if img is None:
        raise ValueError(f"Could not read the image from path: '{image_path}'. Check if the file exists and is a valid image.")

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = gray_img.shape
    aspect_ratio = height / width
    new_height = int(aspect_ratio * output_width * ASPECT_CORRECTION_FACTOR)
    if new_height == 0: new_height = 1

    resized_img = cv2.resize(gray_img, (output_width, new_height), interpolation=cv2.INTER_LINEAR)
    
    print(f"🖼️ Original Size: {width}x{height} | Resized to: {output_width}x{new_height}")
    return resized_img.tolist(), output_width, new_height


# 6️⃣ Modular code structure - Emoji Mapping (Same as before)
def map_pixels_to_emojis(grayscale_data: List[List[int]]) -> str:
    """Converts 2D list of grayscale pixel values (0-255) into an emoji string."""
    emoji_art_lines = []
    division_factor = 256 / GRADIENT_LEVELS

    for row in grayscale_data:
        row_emojis = [
            BRIGHTNESS_TO_EMOJI_GRADIENT[min(int(pixel / division_factor), GRADIENT_LEVELS - 1)]
            for pixel in row
        ]
        emoji_art_lines.append("".join(row_emojis))
    
    return "\n".join(emoji_art_lines)


# 6️⃣ Modular code structure - Output Handling (Modified)
def save_to_file(emoji_art: str, output_file: str) -> bool:
    """
    Saves the generated emoji art to a file with Unicode-safe encoding.
    :returns: True if save was successful, False otherwise.
    """
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(emoji_art)
        print(f"\n✅ Emoji art successfully saved to '{output_file}'")
        return True
    except Exception as e:
        print(f"\n❌ Error saving file: {e}", file=sys.stderr)
        return False


# Main execution and CLI setup
def main():
    parser = argparse.ArgumentParser(
        description="Converts an image into an emoji-based representation.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        "image_path", type=str, help="Path to the input image file (e.g., 'input.jpg')."
    )
    parser.add_argument(
        "-w", "--width", type=int, default=50, help="Width of the output in emojis (Default: 50)."
    )
    parser.add_argument(
        "-o", "--output", type=str, default="emoji_art_output.txt", help="Output file name (Default: 'emoji_art_output.txt')."
    )
    # 🌟 NEW: Argument for "Download" (Auto-open)
    parser.add_argument(
        "-d", "--download", action="store_true", 
        help="If set, automatically opens the saved output file in the default text editor/viewer."
    )
    
    args = parsimport cv2
import argparse
import sys
import os # 🌟 NEW: For interacting with the operating system
from typing import List

# 1️⃣ Multi-level emoji gradient mapping (10 levels for better detail)
BRIGHTNESS_TO_EMOJI_GRADIENT = [
    "⚫", "🌑", "🌘", "🌗", "🌖", "🌕", "⚪", "◻️", "◽", "⬜" 
]
GRADIENT_LEVELS = len(BRIGHTNESS_TO_EMOJI_GRADIENT)
ASPECT_CORRECTION_FACTOR = 0.55

# --- Utility Functions (Modified/New) ---

# 🌟 NEW: Function to open the file
def open_file(file_path: str):
    """
    Opens the file in the user's default text editor/viewer, 
    simulating a 'download' for immediate access.
    """
    try:
        # Use 'start' for Windows, 'open' for macOS, 'xdg-open' for Linux
        if sys.platform == "win32":
            os.startfile(file_path)
        elif sys.platform == "darwin": # macOS
            os.system(f"open {file_path}")
        else: # Linux and other Unix-like systems
            os.system(f"xdg-open {file_path}")
        
        print(f"📂 Attempting to open '{file_path}' for viewing...")
    except Exception as e:
        print(f"⚠️ Could not automatically open file. Please find it manually: {e}", file=sys.stderr)


# 6️⃣ Modular code structure - Image Processing (Same as before)
def process_image(image_path: str, output_width: int) -> tuple[List[List[int]], int, int]:
    """Load, validate, convert to grayscale, and resize the image."""
    try:
        img = cv2.imread(image_path)
    except Exception as e:
        raise FileNotFoundError(f"Error loading image: {e}")

    if img is None:
        raise ValueError(f"Could not read the image from path: '{image_path}'. Check if the file exists and is a valid image.")

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = gray_img.shape
    aspect_ratio = height / width
    new_height = int(aspect_ratio * output_width * ASPECT_CORRECTION_FACTOR)
    if new_height == 0: new_height = 1

    resized_img = cv2.resize(gray_img, (output_width, new_height), interpolation=cv2.INTER_LINEAR)
    
    print(f"🖼️ Original Size: {width}x{height} | Resized to: {output_width}x{new_height}")
    return resized_img.tolist(), output_width, new_height


# 6️⃣ Modular code structure - Emoji Mapping (Same as before)
def map_pixels_to_emojis(grayscale_data: List[List[int]]) -> str:
    """Converts 2D list of grayscale pixel values (0-255) into an emoji string."""
    emoji_art_lines = []
    division_factor = 256 / GRADIENT_LEVELS

    for row in grayscale_data:
        row_emojis = [
            BRIGHTNESS_TO_EMOJI_GRADIENT[min(int(pixel / division_factor), GRADIENT_LEVELS - 1)]
            for pixel in row
        ]
        emoji_art_lines.append("".join(row_emojis))
    
    return "\n".join(emoji_art_lines)


# 6️⃣ Modular code structure - Output Handling (Modified)
def save_to_file(emoji_art: str, output_file: str) -> bool:
    """
    Saves the generated emoji art to a file with Unicode-safe encoding.
    :returns: True if save was successful, False otherwise.
    """
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(emoji_art)
        print(f"\n✅ Emoji art successfully saved to '{output_file}'")
        return True
    except Exception as e:
        print(f"\n❌ Error saving file: {e}", file=sys.stderr)
        return False


# Main execution and CLI setup
def main():
    parser = argparse.ArgumentParser(
        description="Converts an image into an emoji-based representation.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        "image_path", type=str, help="Path to the input image file (e.g., 'input.jpg')."
    )
    parser.add_argument(
        "-w", "--width", type=int, default=50, help="Width of the output in emojis (Default: 50)."
    )
    parser.add_argument(
        "-o", "--output", type=str, default="emoji_art_output.txt", help="Output file name (Default: 'emoji_art_output.txt')."
    )
    # 🌟 NEW: Argument for "Download" (Auto-open)
    parser.add_argument(
        "-d", "--download", action="store_true", 
        help="If set, automatically opens the saved output file in the default text editor/viewer."
    )
    
    args = parser.parse_args()

    # --- Execution Logic ---
    try:
        # Process the image
        grayscale_data, new_width, _ = process_image(args.image_path, args.width)
        
        # Map pixels to emojis
        emoji_art = map_pixels_to_emojis(grayscale_data)
        
        # Print the result to console
        print("\n" + "="*new_width*2)
        print("🎨 Generated Emoji Art:")
        print("="*new_width*2)
        print(emoji_art)
        print("="*new_width*2)
        
        # Save the result
        save_success = save_to_file(emoji_art, args.output)

        # 🌟 NEW: Auto-open/Download logic
        if args.download and save_success:
            open_file(args.output)


    except (FileNotFoundError, ValueError) as e:
        print(f"\n🛑 Fatal Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()er.parse_args()

    # --- Execution Logic ---
    try:
        # Process the image
        grayscale_data, new_width, _ = process_image(args.image_path, args.width)
        
        # Map pixels to emojis
        emoji_art = map_pixels_to_emojis(grayscale_data)
        
        # Print the result to console
        print("\n" + "="*new_width*2)
        print("🎨 Generated Emoji Art:")
        print("="*new_width*2)
        print(emoji_art)
        print("="*new_width*2)
        
        # Save the result
        save_success = save_to_file(emoji_art, args.output)

        # 🌟 NEW: Auto-open/Download logic
        if args.download and save_success:
            open_file(args.output)


    except (FileNotFoundError, ValueError) as e:
        print(f"\n🛑 Fatal Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
