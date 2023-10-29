# What is this for?

This folder should be used to store configuration files.

This file can be used to provide users with instructions for how to reproduce local configuration with their own credentials.

## Instructions

1. Inside the `.env` folder, create the `DATABASE_URL` key with the following values:

```
DATABASE_URL=postgresql+psycopg2://ibge_commodities_data_user:PASSWORD@your_host/your_db
```
