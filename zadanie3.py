from binarytree import Node

root = Node("root")
root.lewy = Node("docs")
root.prawy = Node("media")
root.lewy.lewy = Node("szkice")
root.lewy.prawy = Node("pdf")
root.prawy.prawy = Node("video")

def zlicz_foldery(korzen):
    #WRITE YOUR CODE HERE
    pass

def czy_zawiera_folder(korzen, nazwa):
    # WRITE YOUR CODE HERE
    pass

print("Liczba folderów:", zlicz_foldery(root))
print("Czy zawiera 'pdf':", czy_zawiera_folder(root, "pdf"))
print("Czy zawiera 'muzyka':", czy_zawiera_folder(root, "muzyka"))

#oczekiwany wynik:
# Liczba folderów: 6
# Czy zawiera 'pdf': True
# Czy zawiera 'muzyka': False
