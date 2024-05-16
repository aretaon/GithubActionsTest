# First install pak with the standard installation routine
if (!require("pak",character.only = TRUE))
{
install.packages("pak",dep=TRUE, repos=c('https://ftp.fau.de/cran/', 'https://cloud.r-project.org'))
if(!require("pak",character.only = TRUE)) stop("Package not found")
}

# Collect all required packages as vectors and install with pak
# see https://pak.r-lib.org/dev/reference/get-started.html
CRAN_packages <- c("rrcovNA", "tidyverse", "tmvtnorm")
BC_packages <- c("limma", "vsn", "RankProd", "pcaMethods", "impute", "SummarizedExperiment")
github_packages <- c("github::kreutz-lab/DIMAR")

installedPackages <- rownames(installed.packages())
for (package in c(github_packages, CRAN_packages, BC_packages)){
  if (package %in% installedPackages){
    require(package, character.only = TRUE)
    }
  else{
    pak::pkg_install(package)
    require(package,character.only = TRUE)
    }
}

# read the args coming form Python
args <- commandArgs(trailingOnly=TRUE)

input <- args[1]
print(input)
