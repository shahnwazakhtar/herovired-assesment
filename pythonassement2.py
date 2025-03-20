e
def count_file_contents(file_path):
  
    try:
        with open(file_path, 'r') as file:
            
            line_count = 0
            word_count = 0
            char_count = 0
            
         
            for line in file:
              
                line_count += 1
                
                
                words_in_line = line.split()
                word_count += len(words_in_line)
                
                
                char_count += len(line)
            
           
            print(f"Number of lines: {line_count}")
            print(f"Number of words: {word_count}")
            print(f"Number of characters: {char_count}")
    
    except FileNotFoundError:
       
        print(" The file you entered not exixt.")
    except Exception as e:
       
        print(f"An error occurred: {e}")


file_path = input("Please enter the path of the text file: ")


count_file_contents(file_path)
