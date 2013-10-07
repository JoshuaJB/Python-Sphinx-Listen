#Python-Listen
###Version 0.0.2
This project is still only in the early stages, but it aims to present an intuitive interface for background listening and speech to text using cumSphinx's gstreamer plugin on Linux.


* See /source/sphinxwrap.py for module
* See /source/sphinxwrap.pyc for precompiled module
* See /source/basic demo.py for a demo


This module has only been tested on Ubuntu, but may work on other Linux distributions.

##Installation:
(Un-tested, may need other dependencies)

1.  Ubuntu:
  *  Install the following packages and all their dependencies: **gstreamer0.10-pocketsphinx** and **pocketsphinx-hmm-en-hub4wsj**
  *  Download /source/sphinxwrap.py and include in program.
  *  (Download the entire source if you want API documentation and sample code)

##Documentation:
(Anything inside <> should be replaced)

To import the module:
```
  import sphinxwrap
```

To create an instance of the listener use:
```python
  sphinxwrap.backgroundListener(<OPTIONAL: audio source, defaults to "alsasrc">)
```

To add a particular word to listen for use the *add* method:
```python
  .add(<a word of type str>, <event callback>)
  # returns True is successful
  # raises ValueError if the word is not of type str
  # rasies ValueError if the callback cannot be called
```

To stop listening for a particular word use the *remove* method:
```python
  .remove(<a word of type str>)
  # returns True is successful, False otherwise
  # raises ValueError if the word is not of type str
```

To start listening call the *startListening* method:
```python
  .startListening()
```

To stop listening call the *stopListening* method:
```python
  .stopListening()
```

##Licensing:
Module is avalible under The Apache 2.0 License.
Sample code is avalible under The MIT Licence.
