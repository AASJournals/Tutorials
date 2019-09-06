# Using Persistent Repositories in AAS Journals (AJ/ApJ/ApJL/ApJS/RNAAS)

The AAS Journals strongly encourage authors to place data or software products related to an article into a persistent repository linked to the main journal article by a [DOI][9f8a762d]. This is a change from our past use of supplementary tar.gz files to append various types of article related material. This tutorial describes the processes for choosing a repository and curating digital objects in those repositories. 

Two articles that might aid your decisions about archiving data/software include: **"Ten Simple Rules for the Care and Feeding of Scientific Data**" [(doi:10.1371/journal.pcbi.1003542)](https://doi.org/10.1371/journal.pcbi.1003542)" and **"Achieving human and machine accessibility of cited data in scholarly publications"** [(doi:10.7717/peerj-cs.1)](https://doi.org/10.7717/peerj-cs.1)". Please note that depositing your data objects is only the first step to making these materials useful for your reader.   

Instructions for mentioning and citing these digital objects in an AAS Journals manuscript are provided in "[Citing Repositories][7c9b06c7]."

## Software Archiving and Citation
Per the [AAS Journals' policy on Software](https://journals.aas.org/policy-statement-on-software/) we recommend that software used as part of the research process be persistently **archived** and **cited** in the final article text. In other words, the archived software should referenced as a first class citation in your final bibliography. This includes code of the classes:
- Reusable software packages created as a product of the research presented in the manuscript;
- Software scripts for the replication of analysis or figures or data presented in a manuscript.

Authors of such content should be careful to make informed, collaborative decisions about which develooers and contributors should be listed as authors for these cited software releases. Archived codes should be licensed (*at the archive*) and to the extent relevant for the code, [semantically versioned](https://semver.org/). Additional curation recommendations are given below, and authors may wish to read **"Software citation principles**" [(doi:10.7717/peerj-cs.86)](https://doi.org/10.7717/peerj-cs.86)" for additional analysis of the underlying goals of software citation.

The two most common workflow for authors to persistently archive and cite their codes include:
- Direct transfer from a tagged and released GitHub repository to Zenodo. This [workflow is documented](https://guides.github.com/activities/citable-code/), and produces a versioned software release. Developers using this workflow should pay very careful attention to matters of authorship as encoded by GitHub/Zenodo workflow and edit the necessary field(s) appropriately.
- Direct deposit of packaged software (zip/tar.gz) into one of the repositories listed below. This may or may not produce a properly versioned archival software package. This is also the best workflow for materials not stored in Github and for most data releases. 

## Article Related Content
There are many (non-software) types of article related content that are best served by archiving them in persistent repositories and linking them to final article text. These include:
- Software parameter and output files, e.g., MCMC chains;
- Reduced observational data, e.g., FITS images;
- Large computational or visualization datasets.

Individual repositories offer better search, discovery, and access mechanisms for these types of related data products than the extant practice of burying them in an article's supplementary materials. Over the past few years a number of open repositories affiliated with long lived institutions have come into existence, accepting a wide array of materials with larger storage sizes than currently allowed by the Journals. We now recommend authors use these services for preserving related content.

It is important to remember that certain materials are considered central to the final article and **should continue to be submitted with the manuscript.** The Journals consider preservation and association of such material with the final article impotant and a vital part of our charge in publishing your article(s). Such central, associated content includes:
- Tables of results, e.g., catalogs;
- Movies, audio recordings, or other animations;
- Compendium or atlas of images, e.g., "Figure Sets";
- Data directly related to a figure, e.g., "Data behind the Figure,";
- Interactive Figures. 

Currently there are no persistent platforms for author generated websites, e.g., a project website that contains arbitrary custom HTML/javascript visualizations of data products. While such websites are common in astronomy, the act of archiving and preserving their contents today involves saving only the low level data objects in persistent repositories and stripping away the browser rendered functionality.

## Recommended Repositories
There are a number of astronomy specific and/or generic repositories that we recommend authors use for archiving and linking you data or software to AAS Journal articles. At present, the AAS does not have contractual relationships with any of these, but consider them to be valid archives for your use. In addition to the repositories described here there are also institutional repositories that preserve such data products and issue DOI data links. Your institution's librarian will be able to tell you if they provide a similar service. 

90% of the effort in creating a dataset in one of these data repositories involves drag and drop of files into a web based workflow, and filling out metadata fields. We estimate that archiving data should take about 30 min of work not withstanding upload times or double-checking your work. The AAS Data editors are happy to assist you with any questions you have about these repositories or help solve problems that you experience when working with them. Please contact the [Data Editors helpdesk](mailto:data-editors@aas.org).

Some of these services directly connect to other everyday research tools like Dropbox and Github. Please see the comparison matrix below for more information on these.

#### Astronomy Specific Repositories
The following astronomy archives offer data preservation platforms that mint DOIs for specific categories of data. These archives may or may not be available for your particular project:
- [Caltech/NASA IPAC](https://www.ipac.caltech.edu/dois); [List of all [released data DOIs](https://search.datacite.org/works?data-center-id=caltech.ipacdoi)]
- [Canadian Advanced Network for Astronomical Research (CANFAR)](https://www.canfar.net/en/docs/digital_object_identifiers/); [List of all [released data DOIs](https://search.datacite.org/works?data-center-id=cisti.cadc)]
- [China-VO Paper Data Repository](http://paperdata.china-vo.org/); [List of all released data DOIs]
- [Mikulski Archive for Space Telescopes (MAST)](https://archive.stsci.edu/doi/search/); Contribution [Guidelines for HLSPs](https://archive.stsci.edu/hlsp/hlsp_guidelines/index.html); [List of all [released data DOIs](https://search.datacite.org/works?data-center-id=stsci.mast)]


#### Generic Repositories
There are a number of open "generic" data repositories that serve all fields from communities around the world. We curate collections of Journal related data in some of them: 
- [Zenodo][83fcbbbf]  (Contribute to the [AAS Journals' Zenodo Community](https://zenodo.org/communities/aas/))
- [Harvard Dataverse][c2dfe768] (Contribute to the [AAS Journals' Dataverse](https://dataverse.harvard.edu/dataverse/aas))
- [figshare][f93cb6fe]

  [83fcbbbf]: https://zenodo.org/ "Zenodo"
  [f93cb6fe]: http://figshare.com/ "figshare"
  [c2dfe768]: https://dataverse.harvard.edu/ "Dataverse"

All of these register DataCite DOIs for individual repository records. A "record" varies somewhat in its definition, classification, and defaults between these generic repositories. There are a variety of differences between these generic repositories that may influence your decision to utilize one or another of them. Please review the comparison table below to help you make your decision.

The AAS Journals maintain curated ''collections'' in each of these generic repositories; you will find those collection links in the comparison table below. A curated collection means that your dataset will appear collated with other datasets from AAS Journals, which helps readers find related content and alerts the AAS Editorial team to review and suggest metadata improvements to linked datasets. Please submit your AAS Journal related data set to the appropriate AAS Journal Collection. This can also be done after you have posted the material.

## Curating your Repository

Curation is a critical part of publishing digital objects. Your efforts to correctly describe the data or code you've preserved can immediately affect its discovery and reuse. For instance, a laconic abstract or description such as, "Here's the data related to my ApJ paper" does not help the reader understand or use the material shared. In addition to a clear description the AAS Journals request that you focus on four specific areas when curating your data release: authorship, licensing, community or collection, and linking. Some archives **require** you to carefully edit these fields and will reject the data submission if it is incorrect or incomplete.

#### Authorship
Please ensure that the author list for your repository corresponds to the appropriate authorship of the data or code. Sometimes a piece of code will be only yours, and in other cases the data is born out of a collaboration. Sometimes the repository authoring should match the authorship of the corresponding paper. Unfortunately automated workflows, e.g., "Zenodo+Github", can only guess contributor names based on GitHub metadata, or can choose only the repository owner as the lead author by default. The precision of these fields is almost always entirely in your hands. 

In the example below we created an organizational user as the lead author instead of a person. In any case, please do not include the AAS Journals Team in your author list. 

![Screen shot of authorship metadata fields in Zenodo. Be certain that your authorship list is complete and meaningfully ordered.](img/zenodo_authorship.png "Authorship Metadata Fields in Zenodo")

#### License 
It is critical to always license the objects you share for reuse. All rights are reserved to the author for unlicensed objects, making them almost impossible to reuse. When using a repository to release material be explicit about the license and ensure that it matches the license used elsewhere, e.g., if the code is MIT on GitHub then license it MIT on Zenodo. This is not automatically imported. 

![Screen shot of licensing metadata fields in Zenodo. You should always license your shared material. Please ensure the Zenodo license matches the license you've chosen for this release. ](img/zenodo_license.png "Licensing Metadata Fields in Zenodo")

#### Communities
You may want to list the data or code in the AAS Journals "Community". At the AAS Journals we manage these communities to raise awareness of data and codes published in our Journals; having your data/code in a Community means that a reader can click once to discover all the objects related to AAS Journals in that repository [(try it for Zenodo)](https://zenodo.org/communities/aas/). You can add your data/code DOI to a community when you are creating it.   

![Screen shot of Communities fields in Zenodo. Adding your data or code to a Community can increase its discoverability. ](img/zenodo_communities.png "Communities Metadata Fields in Zenodo")

#### Relationships to the Final Article
Most of the metadata for your data/code can be added at the same time you upload your data. Unless the data changes, the metadata can be easly updated after data publication to fix errors or make improvements. Besides fixing errors, one critical post-publication metadata edit you can make is to link your data DOI to the final published article. 

There are many types of links you can add; some are automatically generated by an archive; all such links show up on the main landing page of your archived object and in the metadata store for DOIs. Here are some examples. If you uploaded your code from GitHub into Zenodo then you will see an automatically created link between the github repository and your Zenodo archive DOI. If you create a new version of that code (or data) then there will be a "hasVersion" relationship between the DOIs automatically added. These should not be edited. 

Other kinds of relationships need to be added manually; we focus on those related to the final Journal article. Once your manuscript is published you should add a new field, entering the ApJ article "DOI" as a Related Identifier. You can ask the IOP office for the article DOI as soon your manuscript is transfered to them (post-acceptance). The proper semantic relationship is that your Journal article "is supplemented by" your data upload. We do not suggest exploring any other semantic relationships between your data and the article. While your arXiv preprint does not have its own DOI, you could also add a relationship between its URL and data DOI, e.g., https://arxiv.org/abs/1812.07565 is supplemented by https://doi.org/10.5281/zenodo.2225161. 

![Screen shot of Related Identifiers fields in Zenodo. Related Identifiers allow you to associate your data object to the final paper as a supplement or establish how it is cited in a subsequent article.](img/zenodo_relatedIds.png "Related Identifiers Metadata Fields in Zenodo")

## Generic Repository Comparison Lookup Table

### **[Zenodo](https://zenodo.org/)**

| Feature | Comments |
|---|---|
| **AAS Journals Collection**   | Zenodo **AAS** Community [Deposit Link](https://zenodo.org/deposit/?c=aas) | 
| **What is a DOI record?**     | A DOI record points to a group of files uploaded as a batch; a record assigned 1 of 8 "types" regardless of the content of the batch. Please use the correct type (software for software; dataset for data) | 
| **Record Types**              | Publication, Poster, Presentation, Dataset, Image, Video/Audio, Software, Lesson |
| **Collections of "objects”**  | Communities |
| **Other features**            | Github/Zenodo [Making Your Code Citable](https://guides.github.com/activities/citable-code/); PDF rendering; pre-reserve DOIs; versioned and concept DOIs |
| **File size limit**           | <50GB |
| **Record Limit**              | 50GB total per record (DOI) |
| **Metadata**                  | Rich |
| **File Level Metadata?**      | None |
| **Semantics?**                | Good relational related identifier schema |
| **Licensing?**                | Pretty much any standard option possible for the record. |
| **Versioning?**               | Serial file versioning; Metadata edits do not trigger versions; "Concept" DOIs pointing to latest version of record; always version and use semantic versioning |
| **Embargo?**                  | Open, Embargo, Restricted, Closed, Not-submitted |
| **Record description**        | Limited HTML; Lists but no tables (stripped out) |
| **Individual File URLs**      | Yes, human readable file links: `https://zenodo.org/record/<record#>/files/filename.ext` |
| **Upload options**            | Desktop; Github |
| **Who are they?**             | CERN Library |
| **Pricing/Policies/FAQ**      | http://help.zenodo.org/ |
| **Citation Policy**           | See recommended citation on individual record landing page |
| **Preservation Policy**       | http://about.zenodo.org/policies/ |
| **Other tips/tricks**         | Watch auto-generated GitHub=>Zenodo metadata; use 'Additional notes' for attribution requirements; use semantic versioning for version field |
| **API information**           | http://developers.zenodo.org/ |
|   |   |
|   |   |

### **[Harvard Dataverse](https://dataverse.harvard.edu/)**

| Feature | Comments |
|---|---|
| **AAS Journals Collection**   | AAS Journals [Dataverse](https://dataverse.harvard.edu/dataverse/aas) | 
| **What is a DOI record?**     | A DOI record points to a group files called a Dataverse *Dataset* |
| **Collections of "objects”**  | Dataverses |
| **Record Types**              | Look for "Kind of Data" (Uncontrolled vocabulary) |
| **Other features**            | ORCID support; FITS file metadata extraction; astronomy specific metadata; file level metadata |
| **File size limit**           | 2.7 Gb |
| **Record Limit**              | Unlimited though large numbers of files in a Dataset can cause usability issues |
| **Metadata**                  | Rich++ |
| **File Level Metadata?**      | Descriptions; Tagging (User assigned) |
| **Semantics?**                | Related Publications encoded by indentifer type, e.g., DOI, arXiv; no relational semantics |
| **Licensing?**                | CC0 or custom assigned terms of use |
| **Versioning?**               | Serial *internal* versioning; Metadata edits trigger X.Y versions; Only 1 DOI ever minted for any record |
| **Embargo?**                  | User permissions model; file level restrictions; |
| **Record description**        | Limited HTML (permitted tags listed); Lists but no tables |
| **Individual File URLs**      | Download URLs avaible on file landing pages and via API |
| **Upload options**            | Desktop; Dropbox |
| **Who are they?**             | Harvard University |
| **Citation Policy**           | https://dataverse.org/best-practices/academic-credit |
| **Preservation Policy**       | https://dataverse.org/best-practices/harvard-dataverse-preservation-policy |
| **Pricing/Policies/FAQ**      | http://best-practices.dataverse.org/harvard-policies |
| **API information**           | http://guides.dataverse.org/en/latest/api/index.html (generic to all Dataverse installs) |
| **Other tips/tricks**         | File tagging can be useful to create subsets of a record ("dataset") |
|   |   |
|   |   |

### **[figshare](http://figshare.com/)**

| Feature | Comments |
|---|---|
| **AAS Journals Collection**   | None |
| **What is a DOI record?**     | Each uploaded “file” or fileset can have 1 of N types; files can be grouped into *Collections*; any of these (files or Collections) can be assigned a DOI | 
| **Record Types**              | Figure, Media, Code, Dataset (Tables), Poster, Paper, Thesis, Code, Presentation, Fileset (for groups of related files) |
| **Collections of "objects”**  | Public Collections can have DOI; Private Projects & Collections |
| **Other features**            | Excellent previews (csv, markdown, FITS, etc); pre-reserve DOI; private links; ORCID support; |
| **File size limit**           | 5 Gb |
| **Record Limit**              | Unlimited public data; 20 Gb “free, private” then $ |
| **Metadata**                  | Limited data model |
| **File Level Metadata?**      | All records have same limited metadata fields |
| **Semantics?**                | Related links (No semantics or formal encoding) |
| **Licensing?**                | Depends on Type and Public/Private data; CC0 for meta/data; various for Code; CC-By for others |
| **Versioning?**               | Serial file versioning; Metadata edits do not trigger versions; "Concept" DOIs pointing to latest version of record; |
| **Embargo?**                  | Embargo, Private (w/private links);  |
| **Record description**        | Tables can be pasted in; unclear what are the full HTML limits of the “description” field; all files and filesets have individual descriptions |
| **Individual File URLs**      | Individual “big number” filenames; not human recognizable: `http://figshare.com/download/file/#######` |
| **Upload options**            | Desktop; Desktop Uploader; GitHub;  |
| **Who are they?**             | Digital Science; Springer-Nature Startup |
| **Citation Policy**           | https://support.figshare.com/support/solutions search for "cite" |
| **Preservation Policy**       | https://support.figshare.com/support/solutions search for "backup" |
| **Pricing/Policies/FAQ**      | https://support.figshare.com/support/home |
| **Other tips/tricks**         | Public collections useful for bundling individual DOI'd items; |
| **API information**           | https://docs.figshare.com/ |
|   |   |


[7c9b06c7]: CitingRepositories.md "Citing"
[9f8a762d]: https://en.wikipedia.org/wiki/Digital_object_identifier "DOI"
