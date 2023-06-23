#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 16:20:31 2023

@author: molano
"""

import os
import re


def replace_expression(folder_path, search_expression, replacement_expression):
    # Traverse all subfolders and files recursively
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            print(file_name)
            file_path = os.path.join(root, file_name)
            if file_path.find('renaming.py') != -1:
                continue
            # Open the file in read mode
            try:
                with open(file_path, 'r') as file:
                    file_content = file.read()
                if file_content.find(search_expression) != -1:
                    print(f"Found old expression in {file_path}")
                # Replace the expression using regular expressions
                updated_content = re.sub(search_expression, replacement_expression,
                                         file_content)

                # Open the file in write mode and overwrite its content
                with open(file_path, 'w') as file:
                    file.write(updated_content)

            except UnicodeDecodeError:
                print(f"Could not process: {file_path}")

        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            # Rename the folder if the old expression is found
            new_dir_name = re.sub(search_expression, replacement_expression,
                                  dir_name)
            if new_dir_name != dir_name:
                new_dir_path = os.path.join(root, new_dir_name)
                os.rename(dir_path, new_dir_path)
                print(f"Renamed folder: {dir_path} -> {new_dir_path}")
        # rename main folder
        new_folder_path = re.sub(search_expression, replacement_expression,
                              folder_path)
        if new_folder_path != folder_path:
            new_dir_path = os.path.join(root, new_folder_path)
            os.rename(folder_path, new_dir_path)

def rename(folder_path, replacement_expression, search_expression='ngym_template'):
    """
    rename files and folders and replace the generic ngym_template within files
    with the name of the new toolbox

    Parameters
    ----------
    folder_path : str
        Replace with the desired folder path.
    replacement_expression : str
        replacement_expression.
    search_expression : str, optional
        Replace with the expression you want to search. Sefault is 'ngym_template'.

    Returns
    -------
    None.

    """
    replace_expression(folder_path, search_expression, replacement_expression)


if __name__ == '__main__':
    # Usage example
    # Replace with the desired folder path
    folder_path = '/home/molano/ngym_template'
    # Replace with the expression you want to replace
    replacement_expression = 'your_toolbox_name'
    rename(folder_path=folder_path, replacement_expression=replacement_expression)
