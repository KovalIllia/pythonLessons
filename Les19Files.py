# example 1
# new_value=input("Write something: ")
# fw=open('doc/file1.txt','a')#create doc
# fw.write(f"{new_value}\n")#update doc
# fw.close()#close doc
#
# print()
# print()

# example 2. New value with input
# fw=open('doc/file2.txt','w')#create doc, w-
# fw.write("Hello whole world!")#update doc
# fw.close()#close doc


# print()
# print()


# example 3
fa=open('doc/file1.txt', 'r')
text=fa.read()
fa.close()
print(text)