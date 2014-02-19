import fiona
with fiona.open('ne_110m_admin_0_countries.shp', 'r') as inp:
    output_schema = inp.schema.copy()
    with fiona.collection(
            "output.geojson", "w",
            crs=inp.crs, 
            driver="GeoJSON", 
            schema=output_schema
            ) as out:
        for f in inp:
            print f["properties"]
            if f["properties"]["sovereignt"] != "Antarctica":
                out.write(f)