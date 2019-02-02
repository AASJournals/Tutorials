Source Paper: *Neutrino-Driven Explosion of a 20 Solar-Mass Star in Three Dimensions Enabled by Strange-Quark Contributions to Neutrino–Nucleon Scattering*, Melson et al., 2014, ApJL, [doi:10.1088/2041-8205/808/2/L42](https://doi.org/10.1088/2041-8205/808/2/L42)

Attribution: Elena Erastova (MPG); Markus Rampp (MPG) 
Contact: August Muench (AAS)  
Creation Date: 2015-06-12  
Version Date: 2015-06-22 (ReadMe only updated on 2018-02-23)

## Goal

The goal here is to create an [x3d](http://www.web3d.org/realtime-3d/x3d/what-x3d) file, and an [X3DOM.js](http://www.x3dom.org/) driven interactive HTML wrapper.  Because [VisIt](https://wci.llnl.gov/simulation/computer-codes/visit) does not export x3d directly, users must export an intermediary file format and switch to a new tool that can export x3d objects. 

[ParaView](http://www.paraview.org/) is one such tool, utilizing [VTK](http://www.vtk.org/) as an intermediary file format. 

## Workflow

1. Create plot(s) in VisIt.

2. Export the plot(s) in vtk format in VisIt.
   `File -> Set Save Options` and select `vtk` as output format.  
   Each plot will be exported as an individual vtk file.

3. Open and render the vtk file(s) in ParaView.
   Change color scheme and opacity if necessary.

4. Export plots to x3d in ParaView.
   `File -> Export Scene` and select `x3d.`

5. Use the [yt-project](yt-project.org)'s deployment of [ModelConvert](https://github.com/x3dom/pipeline) to create the X3DOM HTML wrapper,   
   [http://hub.yt/modelconvert/](http://hub.yt/modelconvert). Set the appropriate optimization, HTML wrapper template, and run the conversion.  
   Download the HTML zip file and deploy to your own website or submit with a journal article. 
