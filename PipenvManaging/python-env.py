#  pipenv will do is it will come here and so we'll just say pipenv 
# and it's going to create this wrapper around Machine Learning.
# it's going to assign it to some ID
# going to create this virtual environment and then the requests 
# library here is no longer going to be system wide but instead,
# requests is going to be nested inside of this virtual environment.  
#

"""
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]

[packages]
numpy = "*"
requests = "*"

[requires]
python_version = "3.8"
"""