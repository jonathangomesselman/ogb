### script for writing meta information of datasets into master.csv
### for node property prediction datasets.
import pandas as pd

dataset_dict = {}
dataset_list = []

### add meta-information about protein function prediction task
name = "ogbn-proteins"
dataset_dict[name] = {"num tasks": 112, "num classes": 2, "eval metric": "rocauc", "task type": "binary classification"}
dataset_dict[name]["download_name"] = "proteinfunc"
dataset_dict[name]["version"] = 1
dataset_dict[name]["url"] = "https://snap.stanford.edu/ogb/data/nodeproppred/"+dataset_dict[name]["download_name"]+".zip"
## For undirected grarph, we only store one directional information. This flag allows us to add inverse edge at pre-processing time
dataset_dict[name]["add_inverse_edge"] = True 
dataset_dict[name]["has_node_attr"] = False
dataset_dict[name]["has_edge_attr"] = True
dataset_dict[name]["split"] = "species"
dataset_dict[name]["num nodes"] = 132534
dataset_dict[name]["additional node files"] = 'species'
dataset_dict[name]['additional edge files'] = 'None'

### add meta-information about protein function prediction task
name = "ogbn-products"
dataset_dict[name] = {"num tasks": 1, "num classes": 47, "eval metric": "accuracy", "task type": "multiclass classification"}
dataset_dict[name]["download_name"] = "products"
dataset_dict[name]["version"] = 1
dataset_dict[name]["url"] = "https://snap.stanford.edu/ogb/data/nodeproppred/"+dataset_dict[name]["download_name"]+".zip"
## For undirected grarph, we only store one directional information. This flag allows us to add inverse edge at pre-processing time
dataset_dict[name]["add_inverse_edge"] = True 
dataset_dict[name]["has_node_attr"] = True
dataset_dict[name]["has_edge_attr"] = False
dataset_dict[name]["split"] = "sales_ranking"
dataset_dict[name]["num nodes"] = 2449029
dataset_dict[name]["additional node files"] = 'None'
dataset_dict[name]['additional edge files'] = 'None'

### add meta-information about protein function prediction task
name = "ogbn-arxiv"
dataset_dict[name] = {"num tasks": 1, "num classes": 40, "eval metric": "accuracy", "task type": "multiclass classification"}
dataset_dict[name]["download_name"] = "arxiv"
dataset_dict[name]["version"] = 1
dataset_dict[name]["url"] = "https://snap.stanford.edu/ogb/data/nodeproppred/"+dataset_dict[name]["download_name"]+".zip"
## For undirected grarph, we only store one directional information. This flag allows us to add inverse edge at pre-processing time
dataset_dict[name]["add_inverse_edge"] = False 
dataset_dict[name]["has_node_attr"] = True
dataset_dict[name]["has_edge_attr"] = False
dataset_dict[name]["split"] = "time"
dataset_dict[name]["num nodes"] = 169343
dataset_dict[name]["additional node files"] = 'node_year'
dataset_dict[name]['additional edge files'] = 'None'

df = pd.DataFrame(dataset_dict)
# saving the dataframe 
df.to_csv("master.csv")