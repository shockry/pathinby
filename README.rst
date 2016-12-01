PathinBy
========
What is PathinBy
----------------

PathinBy is a tiny tool (used as a command line app or a Python module),
that converts your directory structure into a nice formatted tree to use in your blog posts or other illustrations.

How to use
^^^^^^^^^^
Imagine you have a directory structure like this:

.. image:: http://i.imgur.com/BlW8YHn.png
   :height: 263 px
   :width: 614 px

- To use as a Python module
   >>> import pathinby
   >>> print ('\n'.join(pathinby.create_path('Cats')))

This gives the output:
 .. code::

  |-Big
  | |-Simba.bcat
  |-Sylvester.cat
  |-Tom.cat

- To use as a commend line tool
   .. code::

    $ pathinby -s Cats

This will traverse the Cats directory and print the contents tree to the terminal window.

By default, pathinby will do its work on the current directory if no directory is specified, in this case we specified "Cats".

The *s* option means "*show*", prints the output to the terminal.

Other option is

  -o {path to file} writes the output to the specified file
