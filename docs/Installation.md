# Installation

## Latest stable version

The latest stable version of UIBCDF_tools can be installed from the UIBCDF Anaconda channel:

```bash
conda -c uibcdf uibcdf_tools
```

Once the library was installed, it can be removed from your conda environment with:

```bash
conda remove uibcdf_tools
```

## Developing version

The public repository of the whole library is available in the UIBCDF GitHub page. It can be cloned
in your computer to install it locally (within or without a conda environment, in this case is
indifferent).

```bash
git clone https://github.com/uibcdf/UIBCDF_tools.git
cd uibcdf_tools
python setup.py develop
```

To uninstall this version of the library:

```bash
pip uninstall uibcdf_tools
```

