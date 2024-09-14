#!/usr/bin/env bash

function error() {
    echo '[91m[ERROR][0m' "$1"
}

function warning() {
    echo '[93m[WARNING][0m' "$1"
}

function success() {
    echo '[92m[SUCCESS][0m' "$1"
}

function info() {
    echo '[97m[INFO][0m' "$1"
}
