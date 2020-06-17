#!/usr/bin/python3

def main(first_name, last_name):
  print(f"Hello, {first_name} {last_name}")

if __name__ == "__main__":
  scan_fname = input("What is your name?\n-> ")
  scan_lname = input("What is your last name?\n-> ")
  main(scan_fname, scan_lname)

