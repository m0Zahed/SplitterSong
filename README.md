# SplitterSong


[![Latest Version](https://img.shields.io/pypi/v/openunmix.svg)](https://pypi.python.org/pypi/openunmix)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/openunmix.svg)](https://pypi.python.org/pypi/openunmix)
[![React Router](https://img.shields.io/badge/React%20Router-Latest%20Version-blue.svg)](https://reactrouter.com/)
[![Django REST](https://img.shields.io/badge/Django%20REST-Latest%20Version-green.svg)](https://www.django-rest-framework.org/)
[![](https://img.shields.io/badge/frontend-React-brightgreen)](https://github.com/m0Zahed/my-project)

## About

A web application for music source separation based on the Open-Unmix project.

## Requirements
This application requires that your GPU be compatible with CUDA SDK version 9.0+. You can check whether your GPU can run the application by cross-referencing its microarchitecture [here.](https://en.wikipedia.org/wiki/CUDA#GPUs_supported) 

## Features

- Separates music sources (vocals, bass, drums, harmonics, other) from a given audio input
- Built using React, Django, and Open-Unmix
- Supports pyTorch with CUDA 12 for GPU acceleration

## Usage

- [ ] Upload an audio file to the application.
- [ ] Choose the target model you want to use for separation.
- [ ] Click the "Separate" button.
- [ ] Wait for the separation process to complete.
- [ ] Download the separated audio files for each target source.
