import numpy as np

def clean_and_scale_scores(scores: np.ndarray, min_score, max_score):
    
    scaledscores = np.zeros(scores.shape)
    
    if scores.ndim == 1:
        for i in range(scores.size):
            if scores[i] < min_score:
                scaledscores[i] = min_score
            elif scores[i] > max_score:
                scaledscores[i] = max_score
            else:
                scaledscores[i] = scores[i]
        
        for i in range(scaledscores.size):
            scaledscores[i] = (scaledscores[i] - min_score) / (max_score - min_score)
        return scaledscores
    
    if scores.ndim == 2:
        for i in range(scores.shape[0]):
            for j in range(scores.shape[1]):
                if scores[i, j] < min_score:
                    scaledscores[i, j] = min_score
                elif scores[i, j] > max_score:
                    scaledscores[i, j] = max_score
                else:
                    scaledscores[i, j] = scores[i, j]
        for i in range(scores.shape[0]):
            for j in range(scores.shape[1]):
                scaledscores[i, j] = (scaledscores[i, j] - min_score) / (max_score - min_score)
                
        return scaledscores