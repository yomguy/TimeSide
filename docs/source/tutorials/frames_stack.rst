.. This file is part of TimeSide
   @author: Thomas Fillon

===============================================
 Using the 'stack' (previously decoded frames)
===============================================

This is an example of using the `stack` argument in :class:`timeside.plugins.decoder.file.FileDecoder` to run a pipe with previously decoded frames stacked in memory on a second pass.

First, let's import everything and define the audio file source:

>>> import timeside.core
>>> from timeside.core import get_processor
>>> from timeside.core.tools.test_samples import samples
>>> import numpy as np
>>> audio_file = samples['sweep.mp3']

Then let's setup a :class:`FileDecoder <timeside.plugins.decoder.file.FileDecoder>` with argument `stack=True` (default argument is `stack=False`):

>>> decoder = timeside.plugins.decoder.file.FileDecoder(audio_file, stack=True)

Setup an arbitrary analyzer to check that decoding process from file and from stack are equivalent:

>>> level = get_processor('level')()
>>> pipe = (decoder | level)
>>> print pipe.processors #doctest: +ELLIPSIS
[file_decoder-{}, level-{}]


Run the pipe:

>>> pipe.run()

The processed frames are stored in the pipe attribute ``frames_stack`` as a list of frames:

>>> print type(pipe.frames_stack)
<type 'list'>

First frame:

>>> print pipe.frames_stack[0] #doctest: +ELLIPSIS
(array([[...]], dtype=float32), False)

Last frame :

>>> print pipe.frames_stack[-1] #doctest: +ELLIPSIS
(array([[...]], dtype=float32), True)

If the pipe is used for a second run, the processed frames stored in the stack are passed to the other processors without decoding the audio source again.
