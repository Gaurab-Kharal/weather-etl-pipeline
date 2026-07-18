from src.extractor import fetch_load_data
from src.transformer import transform_berlin

if __name__ == "__main__":
    fetch_load_data(52.52, 13.41, "Berlin")
    transform_berlin()