Source Paper: *Unveiling the Role of the Magnetic Field at the Smallest Scales of Star Formation*, Hull et al., 2018, ApJL, [doi:10.3847/2041-8213/aa71b7](https://doi.org/10.3847/2041-8213/aa71b7)

Attribution: Chat Hull (Harvard-Smithsonian Center for Astrophysics)  
Contact: August Muench (AAS)   
Creation Date:  2017-05-05  
Version Date: 2018-02-23


## Goal

To allow 2 (or more) images to toggle on click allow the user to manipulate/control annotations. 

The "toggleJS" algorithm is pretty simple, and is sourced in this example W3C example: https://www.w3schools.com/js/tryit.asp?filename=tryjs_lightbulb

    <script>
    function changeImage() {
        var image = document.getElementById('figure2int');
        if (image.src.match("BfieldOn")) {
            image.src = "fig2_BfieldOff-300-crop.png";
        } else {
            image.src = "fig2_BfieldOn-300-crop.png";
        }
    }
    </script>

## Workflow

Contents of Tutorial

    example/
        fig2_BfieldOff-300-crop.png -- annotations off
        fig2_BfieldOn-300-crop.png  -- annotations on
        index3.html                 -- html wrapper
