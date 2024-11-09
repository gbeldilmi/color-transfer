# color-transfer

The goal of this project is find the best method to create a new image by using the details of a first image and the colors of a second one.

## Motivation

This project is an extension of a previous project given in the context of the course of Image Processing at the University of Burgundy. The goal of this project was to try, step by step, to transfer colors from one image to another using different methods.

## Development roadmap

Each stage of this project is detailed in the [doc](doc) folder. For now, it is written in French.

### Summary

01. [Grayscale](doc/01-grayscale.md)
02. [First steps with colors](doc/02-colors.md)
03. [Sliced Optimal Transport](doc/03-transfer.md)
04. [Bijection between two clouds of points](doc/04-bijection.md)
05. [Histogram specification adaptation for colors](doc/05-specification.md)

### Ideas for future work

+ Implementation of 3D representation of images in RGB space (cf. [printing_tool](src/printing_tool.py))

## Usage

For each method, the corresponding script will be in the `src/` folder and will be used as follows:

```sh
python src/<script>.py <image1> <image2>
```

The result of this command will be saved in the `out/` folder. Be aware that the two images must have the same size.
