# bert-word-embeddings-from-context-sentence :shipit:

*One way to confirm contextually dependent vectors is by evaluating the model's performance on tasks that require understanding the meaning of words in context, such as natural language inference or question answering. Another way is to perform a qualitative analysis by comparing the embeddings generated for a specific word in different sentences or contexts, and observing if they are similar or dissimilar.*

```python
from word_embeddings_from_context import  get_word_embedding_from_sentence

text_1 = "bring some money"
text_2 = "bring your focus to your heart"

word = "bring"

embedding_1 = get_word_embedding_from_sentence(text_1,word)
embedding_2 = get_word_embedding_from_sentence(text_2,word)

print(embedding_1[0:5])
print(embedding_2[0:5])

```
> Output 1 : tensor([ 0.1592,  0.4534,  2.8211, -1.0691,  1.4695])

> Output 2 : tensor([ 2.2381,  0.2831,  1.0606, -2.3082, -0.1782])

As you can see, the same word has different embeddings depending on the context :+1:
