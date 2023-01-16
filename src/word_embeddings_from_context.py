import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
model.eval()


def text_transform(text):
    
    text = "[CLS] " + text + " [SEP]"
    tokenized_text = tokenizer.tokenize(text)
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
    segments_ids = [1] * len(tokenized_text)
    tokens_tensor = torch.tensor([indexed_tokens])
    segments_tensors = torch.tensor([segments_ids])
    return tokens_tensor, segments_tensors,tokenized_text


def get_hidden_states(tokens_tensor, segments_tensors):
    with torch.no_grad():
        encoded_layers, _ = model(tokens_tensor, segments_tensors)
    token_embeddings = torch.stack(encoded_layers, dim=0)
    token_embeddings = torch.squeeze(token_embeddings, dim=1)
    token_embeddings = token_embeddings.permute(1,0,2)

    return token_embeddings 

def get_sentence_embedding(token_embeddings):
    # Stores the token vectors, with shape [22 x 768]
    token_vecs_sum = []

    # `token_embeddings` is a [22 x 12 x 768] tensor.

    # For each token in the sentence...
    for token in token_embeddings:

        # `token` is a [12 x 768] tensor

        # Sum the vectors from the last four layers.
        sum_vec = torch.sum(token[-4:], dim=0)
        
        # Use `sum_vec` to represent `token`.
        token_vecs_sum.append(sum_vec)
    
    return token_vecs_sum



def get_word_index_from_sentence(tokenized_text,word,all_index=False):

    word=word.lower()

    sentence = ' '.join(tokenized_text).lower()
    if word not in sentence:
        print("Error : Word '"+word+"' not in sentence")
        return None
    if all_index:
        index=[]
        for i, token_str in enumerate(tokenized_text):
            if token_str == word:
                index.append(i)
        return index
    else:
        for i, token_str in enumerate(tokenized_text):
            if token_str == word:
                index=i
                break
        return index
 

def get_word_embedding(token_vecs_sum,index):

    return token_vecs_sum[index]




def get_word_embedding_from_sentence(text,word,all_index=False):
    tokens_tensor, segments_tensors,tokenized_text =text_transform(text)
    token_embeddings = get_hidden_states(tokens_tensor, segments_tensors)


    index = get_word_index_from_sentence(tokenized_text,word,all_index)

    token_vecs_sum = get_sentence_embedding(token_embeddings)

    if isinstance(index,list):
        word_embedding = []
        for i in index:
            word_embedding.append(get_word_embedding(token_vecs_sum,i))
    else:
        word_embedding = get_word_embedding(token_vecs_sum,index)

    return word_embedding


print(get_word_embedding_from_sentence("After stealing money from the bank vault, the bank robber was seen fishing on the Mississippi river bank.",'bank',all_index=True))