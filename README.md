# PyClerk
Use python to access all U.S. caselaw through the Harvard Law School Library Caselaw Access Project.

### Documentation

Documentation is super important to this project--the whole goal is ease of use for new coders.  That requires good documentation!

To rebulid the documentation:
- Generate latest raw API docs: 

`sphinx-apidoc -e -o docs/source/api pyclerk`

`sphinx-apidoc -e -o docs/source/api/endpoints pyclerk/endpoint_types`

- Build the docs 