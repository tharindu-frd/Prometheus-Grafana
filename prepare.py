from tqdm import tqdm
import requests

files = [("green_tripdata_2022-01.parquet", "."), ("green_tripdata_2021-01.parquet", "./evidently_service/datasets")]


# So we load the data and store them inside the root directory as well as inside the evidently/datasets
print(f"Download files:")
for file, path in files:
    url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{file}"
    resp = requests.get(url, stream=True)
    save_path = f"{path}/{file}"
    with open(save_path, "wb") as handle:
        for data in tqdm(resp.iter_content(),
                         desc=f"{file}", ## description
                         postfix=f"save to {save_path}",
                         total=int(resp.headers["Content-Length"])):
            handle.write(data)
