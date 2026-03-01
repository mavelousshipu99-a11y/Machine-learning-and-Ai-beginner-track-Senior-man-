text = "Hello, WORLD! HELLO"
# processing
clean_text = text.strip()
#remove whitespace
lower_text = clean_text.lower()
#converts to lowercase
count_hello = lower_text.count("hello")
#count occurances
final_text = lower_text.replace("world", "python")

print(f"Count: {count_hello}, Result: (final_text)")