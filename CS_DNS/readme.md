# Create and Delete DNS record, using custom integrations in Code Stream
### This is the same code, as in the DNS folder, but here it's transformed to be used in Code Stream.

### Pre Req
- A docker host setup in your pipeline
- Builder image url : python
Others with python 3 will probably work, but this is the one i'm using.
- A CI task, that install pywinrm.
I use the command "pip install pywinrm"

### Import
- Create a new Custom Integration with Runtime Python 3
- Copy/paste the script, into your Custom integration, replacing everything.
- Create new version, and release it, to use it. 

### Use
- Create a new pipeline, with the Pre Req, and create a custom task, and selct the imported job.
- Fill out the fields :-) 