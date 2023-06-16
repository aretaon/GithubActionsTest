# Function to test installation status and install packages from CRAN
CRANpkgTest <- function(x)
{
  if (!require("pak",character.only = TRUE))
  {
    install.packages("pak",dep=TRUE, repos=c('https://ftp.fau.de/cran/', 'https://cloud.r-project.org'))
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