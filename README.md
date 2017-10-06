# unity-testhooks

One of the simplest (and dumbest) automatic testing setups possible with Unity. **Requires Python and git.**

Features:
* Automatically run editor tests prior to every commit

# Requirements
1. Unity 5.3+ installed and on your path
2. Python 2.7 installed and on your path
3. A Unity project with a .git repo

# Installation
Currently, the easiest way to get set up:

1. Clone or download this repo
```
git clone git@github.com:zcabjro/unity-testhooks.git
cd unity-testhooks
```
2. Copy the contents of the **hook** directory into your project's **.git/hooks** directory
```
cp hooks/* /path/to/project/.git/hooks
```
3. Copy **test.py** to your project root directory
```
cp test.py /path/to/project
```
4. Every time you commit, git will run the **pre-commit** hook, which in turn calls upon **test.py** to trigger Unity to run editor tests and return the result. On success, the commit proceeds. On failure, the commit aborts.

# Notes

To skip this verification step, making this entire process redundant, use:
```
git commit -m "Your message" --no-verify
```
