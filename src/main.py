from algorithm import cosine_sim, jaccard_sim


def main_(text1, text2):
    
    M1_cos_sim = cosine_sim(text1, text2)
    M2_jac_sim = jaccard_sim(text1, text2)
    similarity_score = (M1_cos_sim + M2_jac_sim) / 2 
    
    return similarity_score
