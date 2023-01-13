https://cmdchallenge.com/

## 1. Your first challenge is to print "hello world" on the terminal in a single command.
- ans.:- echo "hello world" 

## 2. Print the current working directory.
- ans.:- pwd

## 3. List names of all the files in the current directory, one file per line.
- ans.:- ls

## 4. There is a file named access.log in the current directory. Print the contents.
- ans.:-cat access.log  

## 5. Print the last 5 lines of "access.log".
- ans.:-  cat access.log | tail -5 

## 6. Create an empty file named take-the-command-challenge in the current working directory.
- ans.:- touch take-the-command-challenge 

## 7. Create a directory named tmp/files in the current working directory
- ans.:- mkdir tmp tmp/files 

## 8. Copy the file named take-the-command-challenge to the directory tmp/files
- ans.:-  cp take-the-command-challenge ./tmp/files 

## 9. Move the file named take-the-command-challenge to the directory tmp/files
- ans.:- mv take-the-command-challenge ./tmp/files 

## 10. Create a symbolic link named take-the-command-challenge that points to the file tmp/files/take-the-command-challenge.
- ans.:- ln -s tmp/files/take-the-command-challenge 

## 11. Delete all of the files in this challenge directory including all subdirectories and their contents.
- ans.:- find . -name . -o -prune -exec rm -rf -- {} +

## 12. There are files in this challenge with different file extensions. Remove all files with the .doc extension recursively in the current working directory.
- ans.:- find . -name "*.doc" -type f -delete 

## 13. There is a file named access.log in the current working directory. Print all lines in this file that contains the string "GET".
- ans.:- grep "GET" ./access.log 

## 14. Print all files in the current directory, one per line (not the path, just the filename) that contain the string "500".
- ans.:- ls | grep -rl "500" 

## 15. Print the relative file paths, one path per line for all filenames that start with "access.log" in the current directory.
- ans.:- find . -name "access.log*" 

## 16. Print all matching lines (without the filename or the file path) in all files under the current directory that start with "access.log" that contain the string "500".
       - Note that there are no files named access.log in the current directory, you will need to search recursively.
- ans.:- grep -rh 500 */

## 17. Extract all IP addresses from files that start with "access.log" printing one IP address per line.
- ans.:- grep -ohr ^[*-9]*

## 18. Count the number of files in the current working directory. Print the number of files as a single integer.
- ans.:- ls -lr | wc -l

## 19. Print the contents of access.log sorted.
- ans.:- cat access.log | sort

## 20. Print the number of lines in access.log that contain the string "GET".
- ans.:-  grep -c G access.log

## 21. The file split-me.txt contains a list of numbers separated by a ; character.
       - Split the numbers on the ; character, one number per line.
- ans.:- cat split-me* | bc

## 22. Print the numbers 1 to 100 separated by spaces.
- ans.:- echo {1..100}

## 23. This challenge has text files (with a .txt extension) that contain the phrase "challenges are difficult". Delete this phrase from all text files recursively.
       - Note that some files are in subdirectories so you will need to search for them.
- ans.:- sed -ir "chal*" **/*.txt

## 24. The file sum-me.txt has a list of numbers, one per line. Print the sum of these numbers.
- ans.:- cat sum-me.txt |jq -s add

## 25. Print all files in the current directory recursively without the leading directory path.
- ans.:- ls -R|grep [a-z]

## 26. Rename all files removing the extension from them in the current directory recursively.
- ans.:- rm -rf **

## 27. The files in this challenge contain spaces. List all of the files (filenames only) in the current directory but replace all spaces with a '.' character.
- ans.:- ls -p | tr " " "."
