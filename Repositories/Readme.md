

  This is a rough draft tutorial on how to archive and cite/reference data and/or software related to AAS Journal articles. It also provides a comparison of data/software repositories for the AAS author to consider. Given that it is a rough draft please consult the AAS Journal [authoring helpdesk](mailto:authors@aas.org) as you use these instructions for your manuscript. You may also provide direct revisions (pull requests) or report errors (issues) through Github.


## Inserting software/data links into your manuscript.

  Current practices include inserting `\footnote` or inline URL links into a manuscript or adding first class data/software references directly into a manuscript's bibliography. AAS Journals recognize all of these options for referencing data or software related to an article, but prefer that the link/archive be made as persistent as possible. Two articles that might aide your decisions about archiving data/sofware include: "Ten Simple Rules for the Care and Feeding of Scientific Data [(10.1371/journal.pcbi.1003542)](http://dx.doi.org/10.1371/journal.pcbi.1003542)" and "Achieving human and machine accessibility of cited data in scholarly publications [(10.7717/peerj-cs.1)](https://dx.doi.org/10.7717/peerj-cs.1)"

  AAS Journals strongly encourage authors to place data or software products related to an article into a persistent repository linked to the main journal article by a DOI and listed in the main references. See subsequent sections in this tutorial on formatting those references, and inserting them into your manuscript.
  
  Footnote or inline URLs should be protected by the `\url{}` command imported from the `\hyperref` LaTeX package. The current AASTeX `\url` does not http encode URLs, and should not be used, especially not with fragile math or other format codes attempting to try to achieve nice PDF typesetting with the AASTeX `\url`. These manual encodings often do not survive the final production and typsetting process; a future version of AASTeX will better protect inline URLs in manuscripts. 
  

## Formatting References

  Requirements for data or code references are subject to change as we refine new citation types in AAS Journals, but the current reference format is as follows:

    {author*} {year}, {title}, {version^}, {publisher|howpublished~}, {prefix}:{identifier#}

  To illustrate and document this format, we use a corresponding bibtex entry taken and modified from a [real example](http://dx.doi.org/10.5281/zenodo.15991)). Note that all data/software bibtex entries should be of the `@misc` type: 

    @misc{lia_corrales_2015_15991,
        author       = {Lia Corrales},
        title        = {{dust: Calculate the intensity of dust scattering halos in the X-ray}},
        month        = mar,
        year         = 2015,
        doi          = {10.5281/zenodo.15991},
        version      = {1.0},
        publisher    = {Zenodo},
        url          = {http://dx.doi.org/10.5281/zenodo.15991}
        }
  The corresponding reference entry should look like:

    Corrales, L. 2015a, dust: Calculate the intensity of dust scattering halos in the X-ray, v1.0, Zenodo, doi:10.5281/zenodo.15991

#### bibtex Tips, Tricks
  
  You can quickly get a bibtex entry for a DOI issued by any of the third party repositories listed below with this simple command (Thanks [CrossRef!](http://labs.crossref.org/resolving-citations-we-dont-need-no-stinkin-parser/)):
  
  ```Shell
  curl -LH "Accept: application/x-bibtex" http://dx.doi.org/10.5555/12345678
  ```
  
  There are a number of points to make about the conversion of this bibtex entry into a formal reference in an AAS Journal article. First, our current bibtex style file, [`apj.bst`](ads.harvard.edu/pubs/bibtex/astronat/apj/apj.bst), does not recognize all of these fields when formatting an `@misc` entry during LaTeX/bibtex compilation. A future release of AASTeX with a modified apj.bst for software/data citations is forthcoming. Thus at the present time, some manual repair by authors of software/data references will be necessary.

  Second, when manually fixing software/data references, you can consider the following tips or advice about these bibtex fields and how they translate to a reference in an AAS Journal article: 

  - **{author*}** the author field should been formatted to match journal style: last name, first initial, etc. The current [`apj.bst`](ads.harvard.edu/pubs/bibtex/astronat/apj/apj.bst) does this correctly. 
  - **{version^}** The current `apj.bst` does not pick up the version bibtex key, and you many have to insert it manually into your final reference. This field may or may not even exist for your data/code repository and data object. For example, there is no versioning in the Zenodo archive (yet), requiring you to carry version along manually.
  - **{publisher|howpublished~}** Please use the `{publisher}` key; you may have to add it manually as some repositories do not by default provide bibtex with this key entered (e.g., Zenodo). Note you can "trick" bibtex to use the `{howpublished}` key for the publisher and avoid manually fixing things, but this is not recommended as future `apj.bst` files will correctly parse the `{publisher}` bibtex key. 
  - **{prefix}:{identifier#}** While in the majority of cases the "prefix" of the data/code persistent identifier will be a "doi", we reserve the generic model for edge cases, including "hdl", "arXiv", "ark", "purl", "ivoa", "abs", etc. If this were purely a "DOI" field then formal DataCite recommendations include listing the full URI with scheme (e.g., http), host (e.g., dx.doi.org) and path (e.g., /10.5281/zenodo.15991). This format may be adjusted going forward if the `\url` bibtex key consistently reflects the full URI for all data/code repositories.

  
  
  In summary, it is important to remember that some of the fields listed above are either not provided by the archives ("publisher") or are listed in the bibtex but incorrectly recognized and encoded by the bibtex program using the apj.bst style file. 

## Inserting Citations

  When inserting citations into your manuscript, you would use the standard natbib, `\citet`, `\citep/`, etc markup used for all other references. However, unlike books or journal articles that are effectively static and unchanging after publication, software and possibly data *evolve* forward, improving by fixing bugs, revising reduction algorithms, etc. If you are referencing a persistent copy of a non-static object and wish to alert the reader as to where the non-static **current** version of that research object is stored, then use the parenthetical markup:

    \citet[][See also \url{https://github.com/eblur/dust}]{lia_corrales_2015_15991}

  Again, the `\url` used here is the one imported from \hyperref and not the one from AASTeX v5.2. Again, this LaTeX markup may be rendered unnecessary by future versions of AASTeX and apj.bst that properly carry the original non-static software/data repository along as part of the final citation reference.

## Using 3rd party Data/Code repositories

There are a number of options for placing you data or software in trusted third party repositories and linking them to AAS Journal articles. At present, the AAS does not have contractual relationships with any of these, but consider them to be valid archives for your use. We do maintain curated collections in a number of these repositories; you will find those links in the comparison table below. A curated collection means that your dataset will appear collated with other datasets from AAS Journals, and help us to review and suggest metadata improvements to linked datasets. In addition there are also institutional repositories that preserve such data products and issue DOI data links, so you might contact your institution's librarian to see if they provide a similar service. 

90% of the effort in creating a dataset in one of these data repositories involves drag and dropping files into a web based workflow, and filling out metadata fields. We estimate that it should take about 30 min of work not withstanding upload times.  The AAS Data editors are happy to assist you with any questions you have about these repositories or help solve problems that you experience when working with them. Please contact the [Data Editors helpdesk](mailto:data-editors@aas.org).

Some of these services directly connect to other everyday research tools like Dropbox and Github. Please see the comparison matrix below for more information on these.

#### Comparing Data Repositories.

All of these register DataCite DOIs for records. A "record" varies somewhat in its definition, classification, and defaults. There are other differences between these repositores that may influence your decision to utilize one or another of them.

|   | [Zenodo](https://zenodo.org/) | [Figshare](http://figshare.com/) | [Dataverse](https://dataverse.harvard.edu/) |
|------------|----------|----------|----------|
| **What is a DOI record?** | A DOI record points to a group of files uploaded as a batch; a record assigned 1 of 8 "types" regardless of the content of the batch. | Each uploaded “file” can have 1 of 8 types, and files can be grouped into *Filesets*; any of these (files or filesets) can be assigned a DOI. | A DOI record points to a group files called a Dataverse *Dataset*. |
| **Record Types** | Publication (subtypes), Poster, Presentation, Dataset (Table), Image (subtypes), Video/Audio, Software, Lesson | Figure, Media, Dataset (Table), Poster, Paper, Thesis, Code, Presentation, (Fileset for groups of files) | None |
| **Collections of "data objects” or other curation vehicle** | Communities | Projects | Dataverses |
| **Other features** | Github/Zenodo [Making Your Code Citable](https://guides.github.com/activities/citable-code/); PDF rendering; | Nice previews (csv, markdown, FITS, etc); | File metadata extraction; domain specific metadata;  |
| **Individual File URLs** | Yes, human readable file links: `https://zenodo.org/record/<record#>/files/filename.ext` | Individual “big number” filenames; not human recognizable: `http://figshare.com/download/file/#######` | Not really; API can expose file “IDs” but not filenames. |
| **Record description** | Limited HTML; Lists but no tables (stripped out). | Tables can be pasted in; unclear what are the full HTML limits of the “description” field; all files and filesets have individual descriptions. | Limited HTML (permitted tags listed); Lists but no tables. |
| **File size limit** | 2 Gb | 256 Mb | 2 Gb |
| **Record Limit** | Unlimited? | 1Gb “free” then $ | Unlimited? |
| **Metadata** | Rich | Limited | Rich++ |
| **File Level Metadata?** | None | All records have same fields (filesets or individual files) | Descriptions; Tagging (User assigned) |
| **Semantics?** | Good relational related identifier schema | Related links (No semantics or formal encoding) | Related Publications (No semantics; encoded by indentifer type, e.g., DOI, arXiv,) |
| **Licensing?** | Pretty much any option possible for the record. | CC-BY for filesets; CC0 for files in filesets. | CC0 or custom assigned terms of use. |
| **Embargo?** | Open, Embargo, Restricted, Closed, Not-submitted | Draft or nah.  | User permissions model; file level restrictions; |
| **Upload options** | Desktop; Dropbox; Github | Desktop; Github | Desktop; Dropbox |
| **Who are they? Who pays for it?** | CERN | Digital Science; Startup | Harvard University (or similar host) |
| **Pricing/Policies/FAQ** | https://zenodo.org/faq | http://figshare.com/pricing | http://best-practices.dataverse.org/harvard-policies |
| **AAS Journals Collection** | Zenodo **AAS** Community [Deposit Link](https://zenodo.org/deposit/?c=aas) | | AAS Journals [Dataverse](https://dataverse.harvard.edu/dataverse/aas) | 
