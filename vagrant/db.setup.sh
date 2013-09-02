#!/usr/bin/env bash

# Create DB and DB owner.

sudo -u postgres bash <<EOF

# Create nypy role
psql -d postgres -c "create role nypyowner with encrypted password 'nypylocal' login;"

# Create DB
psql -d postgres -c "create database nypy with owner nypyowner;"

EOF
