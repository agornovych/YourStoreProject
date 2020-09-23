# **Installation**
From the _project's root dir_ execute:

`python setup.py install`

# **Executing tests**
To execute full e2e:
`pytest -m e2e --conf=test/conf/env_setup.yml`

To execute User registration test:
`pytest -m user_registration --conf=test/conf/env_setup.yml`

To execute Buy product test:
`pytest -m buy_product --conf=test/conf/env_setup.yml`

To execute Wishlist test:
`pytest -m wishlist --conf=test/conf/env_setup.yml`


# **Threads are supported**
For threads add `-n` with amount of _threads_
`pytest -n 2 -m e2e --conf=test/conf/env_setup.yml`

