# Domain annotation tool

## Description
In this repo, we implement a tool for annotating scientific abstracts about coastal areas within 11 domains:
- **Ecology**: *Examination of coastal ecosystems (e.g., mangroves, coral reefs, salt marshes) and their biodiversity, food webs, and ecosystem services.*
- **Sedimentology**: *Analysis of sediment sources, types, and dynamics, including how sediments influence coastal morphology and habitats.*
- **Geomorphology**: *Study of landforms and processes shaping the coast, such as erosion, sediment deposition, and dune formation.*
- **Oceanography**: *Investigation of tides, waves, currents, and their influence on littoral systems, including sediment transport and nutrient cycling.*
- **Hydrology**: *Study of freshwater inputs (e.g., rivers, groundwater) into littoral systems and their impacts on salinity gradients, nutrient fluxes, and sediment loads.*
- **Climatology**: *Evaluation of climate change impacts, including sea-level rise, temperature shifts, and extreme weather events on coastal zones.*
- **Engineering**: *Understanding human interventions (e.g., seawalls, breakwaters) and their effects on natural littoral processes and habitats.*
- **Social Sciences & Humanities**: *Study of human interactions with coastal systems, including socio-economics, cultural practices, resilience, and the historical and archaeological significance of coastal areas.*
- **Chemistry**: *Study of water quality, nutrient loading, and pollutant dynamics, including the effects of human and natural inputs on coastal health.*
- **Policy and Governance**: *Exploration of coastal management practices, laws, and conservation strategies to balance development and environmental protection.*
- **Public Health**: *Study of how coastal systems affect human health, including impacts from pollution, climate change, and diseases, and benefits of these ecosystems on health.*

One abstract might have multiple labels.

The aim is to evaluate Llama on text classification into topics, multi-label.

## Requirements
Please install all the necessary libraries noted in [requirements.txt](./requirements.txt) using this command:

```
pip install -r requirements.txt
```

## How to use
```
python app.py
```

In the app, click on any class to attribute it to an abstract. The application has an autosave function, which means it will save at each modification. Your annotations will be available in `./annotations/annotations.json`. DO NOT DELETE THIS FILE, AS YOU WOULD LOSE ALL YOUR ANNOTATIONS.

## Contributors:

- :wheel: [DELAUNAY Julien](https://github.com/jdelaunay) :wheel: