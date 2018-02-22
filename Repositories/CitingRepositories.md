# Citing Repositories in AAS Journals (AJ/ApJ)

This tutorial details how to cite repositories in your manuscript. The AAS Journals now recommend that content related to published manuscripts be archived in persistent repositories (See our parallel document, [Using Repositories](UsingRepositories.md)). This tutorial documents the acquisition of repository metadata and high level requirements for the final reference, as well as tips for constructing BibTeX and LaTeX bibliographies. Finally, it provides suggestions on how the inline citation should be constructed.

## Repository Citations

  Requirements for references are subject to change as we refine new citation types in AAS Journals, but the current reference format for digital objects in repositories is as follows:

    {author*} {year}, {title}, {version^}, {publisher|howpublished~}, {prefix}:{identifier#}

  To illustrate and document this format, we use a corresponding BibTeX entry taken and modified from a [real example](http://dx.doi.org/10.5281/zenodo.15991)). Note that all data/software BibTeX entries should be of the `@misc` type: 

    @misc{lia_corrales_2015_15991,
        author       = {Lia Corrales},
        title        = {{dust: Calculate the intensity of dust scattering halos in the X-ray}},
        month        = mar,
        year         = 2015,
        doi          = {10.5281/zenodo.15991},
        version      = {1.0},
        publisher    = {Zenodo},
        url          = {https://doi.org/10.5281/zenodo.15991}
        }
  The corresponding reference entry should look like:

    Corrales, L. 2015a, dust: Calculate the intensity of dust scattering halos in the X-ray, v1.0, Zenodo, doi:10.5281/zenodo.15991
    

#### BibTeX Tips, Tricks
  
  You can quickly get a BibTeX entry for a DOI issued by any of the third party repositories listed below with this simple command (Thanks [CrossRef!](http://labs.crossref.org/resolving-citations-we-dont-need-no-stinkin-parser/)):
  
  ```Shell
  curl -LH "Accept: application/x-bibtex" https://doi.org/10.5555/12345678
  ```
At the moment these BibTeX results can lack the requisite fields, e.g., version. 

  In addition, any DataCite DOI has a human readable metadata page associated with it that is accessible through the URL `https://search.datacite.org/works/<doi>`, e.g., `https://search.datacite.org/works/10.5281/zenodo.15991`. From here you can download the reference in RIS or BibTeX formats, though some important metadata may only be found in the DataCite XML or JSON metadata.
  
  There are a number of points to make about the conversion of this BibTeX entry into a formal reference in an AAS Journal article. First, the antiquated BibTeX style file, `apj.bst`, does not recognize all of these fields when formatting an `@misc` entry during LaTeX/BibTeX compilation. A new [`aasjournal.bst`](http://journals.aas.org/authors/aastex/aasjournal.bst) (last updated: 26 Oct 2017) style file has been specifically modified to enable this formatting for software/data citations. You can find it at the [AAS Journals website](http://journals.aas.org/authors/aastex.html) or on [GitHub](https://github.com/AASJournals/AASTeX60).

  Second, for software/data references, you can consider the following tips or advice about these BibTeX fields and how they translate to a reference in an AAS Journal article: 

  - **{author*}** the author field should been formatted to match journal style: last name, first initial, etc. The deprecated `apj.bst` BibTeX does this correctly, as does the newest [`aasjournal.bst`](http://journals.aas.org/authors/aastex/aasjournal.bst).
  - **{version^}** The deprecated `apj.bst` does not pick up the `version` BibTeX key, and you many have to insert it manually into your final reference. This field may or may not even exist for your data/code repository or data object. Zenodo now carries and aggregates released versions of code or data, including encoding a version tag in the repository metadata. See for instance the versioned references available for [astropy/astroquery](https://doi.org/10.5281/zenodo.591669).
  - **{publisher|howpublished~}** Please use the `{publisher}` key; you may have to add it manually as some repositories do not by default provide BibTeX with this key entered (e.g., Zenodo). It is not best practice to rely on information semantically encoded in the DOI string. Note you can "trick" BibTeX to use the `{howpublished}` key for the publisher and avoid manually fixing things, but this is not recommended as the new `aasjournal.bst` file will correctly parse the `{publisher}` BibTeX key. 
  - **{prefix}:{identifier#}** While in the majority of cases the "prefix" of the data/code persistent identifier will be a "doi", we reserve the generic model for edge cases, including "hdl", "arXiv", "ark", "purl", "ivoa", "abs", etc. If this were purely a "DOI" field then formal DataCite recommendations include listing the full URI with scheme (e.g., http), host (e.g., dx.doi.org) and path (e.g., /10.5281/zenodo.15991). 

  In summary, it is important to remember that some of the fields listed above are either not provided by the archives ("publisher") or are listed in the BibTeX but incorrectly recognized and encoded by the BibTeX program using older BibTeX style files. 

## Inserting Citations

  When inserting citations into your manuscript, you should use the standard natbib, `\citet`, `\citep`, etc markup used for all other references. There are two important nuances about digital object citations. First, unlike books or journal articles that are effectively static and unchanging after publication, software and possibly data *evolve* forward, improving by fixing bugs, revising reduction algorithms, etc. Such objects may have a non-static **current** version of that research object located at a specific URL that the author wishes to alert the reader about. Second, authors may simply want to highlight the digital objects inline to the manuscript so that readers can link directly to the software or data without browsing to the bibliography. 

  We recommend inline parenthetical or footnote markup to add direct links to non-static codebases or data:
  
  ```
  \citet[][]{lia_corrales_2015_15991}\footnote{Codebase: \url{https://github.com/eblur/dust} }
  ```

  ```  
  \citep[][Codebase: \url{https://github.com/eblur/dust}]{lia_corrales_2015_15991}
  ```

  ```
  \citep[][Dataset: \url{http://doi.org/10.5281/zenodo.15991}]{lia_corrales_2015_15991}
  ```
  
  
  These styles are our current recommended ways of dealing with this "dual pointer" problem. 

