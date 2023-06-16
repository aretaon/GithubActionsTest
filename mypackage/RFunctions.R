# Function to test installation status and install packages from CRAN
CRANpkgTest <- function(x)
{
  if (!require(x,character.only = TRUE))
  {
    install.packages(x,dep=TRUE, repos='https://ftp.fau.de/cran/')
    if(!require(x,character.only = TRUE)) stop("Package not found")
  }
}

CRAN_packages <- c("rrcovNA", "tidyverse", "BiocManager", "devtools")
for (package in CRAN_packages){
  CRANpkgTest(package)
}

# read the args coming form Python
args = commandArgs(trailingOnly=TRUE)

input <- args[1]
print(input)