import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
long_bookshelf = utils.load_books('books_large.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()
long_bookshelf_v1 = long_bookshelf.copy()

###### comparison functions #####
def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b):
  return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])
#################################

##### outputs #####
sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for book in sort_1:
  print(book['title'])
print('--- END ---')

sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
for book in sort_2:
  print(book['author'])
print('--- END ---')

sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
for book in bookshelf_v2:
  print(book['author'])
print('--- END ---')

# sort_3 = sorts.bubble_sort(long_bookshelf, by_total_length)
# for book in sort_3:
#   print(book['title'])
# print('--- END ---')

sorts.quicksort(long_bookshelf_v1, 0, len(long_bookshelf_v1) - 1, by_total_length)
for book in long_bookshelf_v1:
  print(book['title'])
print('--- END ---')
###################
