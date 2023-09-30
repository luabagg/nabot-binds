# Nabot Binds

This project is a simple script to create HotKeys.

It creates two KeyBinds that can be configured at keybinds.cfg. One will write random alphanumeric characters, and the other will write only numbers, with the specified length.

## Useful links

- [pynput](https://pypi.org/project/pynput/)
- [configobj](https://pypi.org/project/configobj/)

## Configuration

- Start by making a new virtual environment
    ```sh
    # At root dir
    python -m venv venv
    source venv/bin/activate
    ```
- Install dependencies
    ```sh
    pip install -r requirements.txt 
    ```
- Edit keybinds.cfg as you wish
- Run the script ()
    ```sh
    python ./app
    ```