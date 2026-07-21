#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CSV Link Extractor - Extract clean URLs from CSV files
Author: super-meuw
Version: 2.0.0
"""

import csv
import sys
import os
import re
from datetime import datetime

# ============================================================
# BANNER - ASCII Cat
# ============================================================
BANNER = r"""

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

"""

def extract_links_from_csv(file_path):
    """
    Extract only the 'link' column from CSV file
    
    Args:
        file_path (str): Path to CSV file
        
    Returns:
        list: List of extracted URLs
    """
    links = []
    seen = set()
    
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            # Detect delimiter
            sample = f.read(1024)
            f.seek(0)
            
            dialect = csv.Sniffer().sniff(sample)
            reader = csv.DictReader(f, dialect=dialect)
            
            # Find link column
            if 'link' in reader.fieldnames:
                for row in reader:
                    link = row.get('link', '').strip()
                    if link and link not in seen:
                        links.append(link)
                        seen.add(link)
            else:
                print("[!] Column 'link' not found. Available columns:")
                print(f"    {', '.join(reader.fieldnames)}")
                
                # Try to find URL column
                for row in reader:
                    for key, value in row.items():
                        if value and re.match(r'https?://', value):
                            if value not in seen:
                                links.append(value)
                                seen.add(value)
    
    except Exception as e:
        print(f"[!] CSV parsing error: {e}")
        links = extract_links_manual(file_path)
    
    return links

def extract_links_manual(file_path):
    """
    Fallback method: manual CSV parsing
    
    Args:
        file_path (str): Path to CSV file
        
    Returns:
        list: List of extracted URLs
    """
    links = []
    seen = set()
    
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
        # Parse header
        header = lines[0].strip().split(',')
        
        # Find link column index
        link_index = None
        for i, col in enumerate(header):
            if col.strip().lower() in ['link', 'url', 'website', 'domain']:
                link_index = i
                break
        
        if link_index is None:
            return extract_all_urls_from_text(file_path)
        
        # Parse data rows
        for line in lines[1:]:
            parts = line.strip().split(',')
            if len(parts) > link_index:
                link = parts[link_index].strip().strip('"\'')
                if link and link not in seen and re.match(r'https?://', link):
                    links.append(link)
                    seen.add(link)
    
    return links

def extract_all_urls_from_text(file_path):
    """
    Ultimate fallback: extract all URLs from text
    
    Args:
        file_path (str): Path to file
        
    Returns:
        list: List of extracted URLs
    """
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    url_pattern = r'https?://[^\s<>"\'{}|\\^`\[\],]+'
    all_urls = re.findall(url_pattern, content)
    
    links = []
    seen = set()
    
    for url in all_urls:
        url = url.rstrip(',.;:!?\'"')
        if url and url not in seen:
            links.append(url)
            seen.add(url)
    
    return links

def generate_output_filename():
    """
    Generate unique output filename with timestamp
    
    Returns:
        str: Output filename
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"extracted_links_{timestamp}.txt"

def save_links(links, output_file):
    """
    Save extracted links to file
    
    Args:
        links (list): List of URLs
        output_file (str): Output file path
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for link in links:
            f.write(link + '\n')

def print_results(links, output_file):
    """
    Display extraction results
    
    Args:
        links (list): List of extracted URLs
        output_file (str): Output file path
    """
    print("\n" + "="*50)
    print(f"[+] Extraction complete!")
    print(f"[+] Total URLs extracted: {len(links)}")
    print(f"[+] Output saved to: {output_file}")
    
    if links:
        print("\n[+] Sample extracted URLs:")
        for link in links[:5]:
            print(f"    • {link}")
        if len(links) > 5:
            print(f"    ... and {len(links) - 5} more")
    print("="*50)

def main():
    """Main execution flow"""
    
    print(BANNER)
    print("="*50)
    
    # Check arguments
    if len(sys.argv) < 2:
        print("[!] Usage: python script.py <input.csv>")
        print("[!] Example: python script.py Asset-Data.csv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Validate input file
    if not os.path.exists(input_file):
        print(f"[!] Error: File '{input_file}' not found!")
        sys.exit(1)
    
    print(f"[+] Processing: {input_file}")
    
    # Extract links
    links = extract_links_from_csv(input_file)
    
    # Generate output filename
    output_file = generate_output_filename()
    
    # Save results
    save_links(links, output_file)
    
    # Display results
    print_results(links, output_file)

if __name__ == "__main__":
    main()
