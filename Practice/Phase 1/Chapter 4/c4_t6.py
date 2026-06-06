# t1
web_url = input("Please enter your website link: ")
is_correct = web_url.startswith("https://")
print(is_correct)
# t2
bad_sentence = "I absolutely hate programming in Java"
modified_sentence = bad_sentence.replace("hate", "love").replace("Java", "Python")
print(modified_sentence)
# t3
document_text = "Python is amazing, Python is fast, let's learn Python!"
total_times = document_text.count("Python")
python_position = document_text.find("Python")
print(f"The word 'Python' appears {total_times} times and first found at index no {python_position}")
