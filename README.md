
setup environment for the [Introduction to Data Science](https://github.com/lewagon/intro-to-data-science-challenges) challenges

the challenges are served through [mybinder](https://www.notion.so/lewagon/B2U-Intro-to-Data-Science-f88a9af1afff44109bfd3)

# update package version

update the contents of `requirements_raw.txt`, then process `requirements.txt` from a new env:

``` bash
pyenv install 3.12.0
pyenv virtualenv-delete binder
pyenv virtualenv 3.12.0 binder
pyenv local binder
pip install -U pip
export REQ_URL=https://raw.githubusercontent.com/lewagon/intro-to-data-science-env/master/requirements_raw.txt
export PACKAGES=$(curl -s ${REQ_URL} | tr "\\n" " ")
pip install $(echo ${PACKAGES})
pip freeze | grep $(echo ${$(echo ${PACKAGES})/#/-e }) > requirements.txt
```

# info

`build.log` contains the mybinder image build and container start logs
