# import os
# import random
# import pandas as pd

# def predictor(image_link, category_id, entity_name):
#     '''
#     Call your model/approach here
#     '''
#     #TODO
#     return "" if random.random() > 0.5 else "10 inch"

# if __name__ == "__main__":
#     DATASET_FOLDER = '../dataset/'
    
#     test = pd.read_csv(os.path.join(DATASET_FOLDER, 'test.csv'))
    
#     test['prediction'] = test.apply(
#         lambda row: predictor(row['image_link'], row['group_id'], row['entity_name']), axis=1)
    
#     output_filename = os.path.join(DATASET_FOLDER, 'test_out.csv')
#     test[['index', 'prediction']].to_csv(output_filename, index=False)

import pandas as pd

out = pd.read_csv('src/final.csv')

def modify_element(value):
    if isinstance(value, str) and value.count('.') > 1:
        # Keep only the part after the first period
        return value.split('.', 1)[1]  # Splits the string at the first period and returns the second part
    return value  # If there's only one or no period, return the original value

# Apply the function to the DataFrame column
out['prediction'] = out['prediction'].apply(modify_element)

out.to_csv("final.csv",index=False)