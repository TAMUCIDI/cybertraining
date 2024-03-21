module spider anaconda
module load Anaconda3/2022.10

conda create --name myenv

conda activate myenv

wget "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"

pip install geopandas
pip install pandas
pip install seaborn
pip install transformers
pip install chardet
pip install geopandas==0.8.1 
conda install plotly
pip install pyshp
pip install xlrd

pip install git+https://github.com/huggingface/accelerate
pip install datasets
pip install evaluate
ml GCC/12.3.0
python -m pip install optimum
pip install --upgrade-strategy eager install optimum[onnxruntime]
