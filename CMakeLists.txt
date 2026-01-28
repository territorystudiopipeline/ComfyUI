
cmake_minimum_required(VERSION 4.1)

project("ComfyUI" 
    LANGUAGES
        NONE
)

include(RezBuild)



file(GLOB_RECURSE files 
    "*"
    PATTERN ".git" EXCLUDE
    PATTERN ".git/*" EXCLUDE
    PATTERN ".github" EXCLUDE
    PATTERN ".github/*" EXCLUDE
    PATTERN ".ci"
    PATTERN ".ci/*"
    PATTERN "bin" EXCLUDE
    PATTERN ".gitignore" EXCLUDE
)

list(FILTER files EXCLUDE REGEX "/\\.git(/|$)")
list(FILTER files EXCLUDE REGEX "/\\.github(/|$)")
list(FILTER files EXCLUDE REGEX "/\\.ci(/|$)")
list(FILTER files EXCLUDE REGEX "/build(/|$)")
list(FILTER files EXCLUDE REGEX "/bin(/|$)")
list(FILTER files EXCLUDE REGEX "/\\.gitignore$")

rez_install_files(
    ${files}
    DESTINATION ./ComfyUI
)

file(GLOB bins bin/*)
rez_install_files(
    ${bins}
    DESTINATION .
    RELATIVE bin
)
