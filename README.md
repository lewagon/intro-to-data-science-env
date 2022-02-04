
setup environment for the [Introduction to Data Science](https://github.com/lewagon/intro-to-data-science-challenges) challenges

# update package version

update the contents of `requirements_raw.txt`, then process `requirements.txt` from a new env:

``` bash
pyenv install 3.7.12
pyenv virtualenv-delete binder
pyenv virtualenv 3.7.12 binder
pyenv local binder
pip install -U pip
export REQ_URL=https://raw.githubusercontent.com/lewagon/intro-to-data-science-env/update-setup/requirements_raw.txt
export PACKAGES=$(curl -s ${REQ_URL} | tr "\\n" " ")
pip install $(echo ${PACKAGES})
pip freeze | grep $(echo ${$(echo ${PACKAGES})/#/-e }) > requirements.txt
```
