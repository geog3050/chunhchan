# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2024-05-05 14:02:35
"""
import arcpy
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *

def Model():  # Model

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")

    Veg_Polys = "Veg_Polys"
    Park_Boundary = "Park_Boundary"
    NHDFlowline = "NHDFlowline"
    USGS_1_n33w112_20240401_tif = arcpy.Raster("USGS_1_n33w112_20240401.tif")
    USGS_1_n33w111_20240401_tif = arcpy.Raster("USGS_1_n33w111_20240401.tif")
    finalProjectModel_gdb = "Z:\\2024_Spring\\GEOG_3520\\STUDENT\\chunhchan\\Final Project\\Model\\finalProjectModel\\finalProjectModel.gdb"
    Input_true_raster_or_constant_value = 1
    Input_false_raster_or_constant_value = 0
    Input_true_raster_or_constant_value_3_ = 1
    Input_false_raster_or_constant_value_2_ = 0

    # Process: Clip (2) (Clip) (analysis)
    Vegetation = "Z:\\2024_Spring\\GEOG_3520\\STUDENT\\chunhchan\\Final Project\\Model\\finalProjectModel\\finalProjectModel.gdb\\Vegetation"
    arcpy.analysis.Clip(in_features=Veg_Polys, clip_features=Park_Boundary, out_feature_class=Vegetation)

    # Process: Project (2) (Project) (management)
    VegetationFinal = "Z:\\2024_Spring\\GEOG_3520\\STUDENT\\chunhchan\\Final Project\\Model\\finalProjectModel\\finalProjectModel.gdb\\VegetationFinal"
    arcpy.management.Project(in_dataset=Vegetation,out_dataset=VegetationFinal, out_coor_system="PROJCS[\"NAD_1983_UTM_Zone_12N\",GEOGCS[\"GCS_North_American_1983\",DATUM[\"D_North_American_1983\",SPHEROID[\"GRS_1980\",6378137.0,298.257222101]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",-111.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]")

    # Process: Clip (Clip) (analysis)
    FlowLineClip = "Z:\\2024_Spring\\GEOG_3520\\STUDENT\\chunhchan\\Final Project\\Model\\finalProjectModel\\finalProjectModel.gdb\\FlowLineClip"
    arcpy.analysis.Clip(in_features=NHDFlowline, clip_features=Park_Boundary, out_feature_class=FlowLineClip)

    # Process: Project (Project) (management)
    FlowLineFinal = "Z:\\2024_Spring\\GEOG_3520\\STUDENT\\chunhchan\\Final Project\\Model\\finalProjectModel\\finalProjectModel.gdb\\FlowLineFinal"
    arcpy.management.Project(in_dataset=FlowLineClip, out_dataset=FlowLineFinal, out_coor_system="PROJCS[\"NAD_1983_UTM_Zone_12N\",GEOGCS[\"GCS_North_American_1983\",DATUM[\"D_North_American_1983\",SPHEROID[\"GRS_1980\",6378137.0,298.257222101]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",-111.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]")

    # Process: Buffer (Buffer) (analysis)
    FlowLineBuffer = "Z:\\2024_Spring\\GEOG_3520\\STUDENT\\chunhchan\\Final Project\\Model\\finalProjectModel\\finalProjectModel.gdb\\FlowLineBuffer"
    arcpy.analysis.Buffer(in_features=FlowLineFinal, out_feature_class=FlowLineBuffer, buffer_distance_or_field="60 FeetInt", dissolve_option="ALL")

    # Process: Extract by Mask (Extract by Mask) (sa)
    DEM1 = "Z:\\2024_Spring\\GEOG_3520\\STUDENT\\chunhchan\\Final Project\\Model\\finalProjectModel\\finalProjectModel.gdb\\DEM1"
    Extract_by_Mask = DEM1
    DEM1 = arcpy.sa.ExtractByMask(USGS_1_n33w112_20240401_tif, Park_Boundary, "INSIDE", "-111.244008949663 32.1036882463363 -110.998333333416 32.3522045741637 GEOGCS[\"GCS_North_American_1983\",DATUM[\"D_North_American_1983\",SPHEROID[\"GRS_1980\",6378137.0,298.257222101]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]]")
    DEM1.save(Extract_by_Mask)


    # Process: Extract by Mask (2) (Extract by Mask) (sa)
    DEM2 = "Z:\\2024_Spring\\GEOG_3520\\STUDENT\\chunhchan\\Final Project\\Model\\finalProjectModel\\finalProjectModel.gdb\\DEM2"
    Extract_by_Mask_2_ = DEM2
    DEM2 = arcpy.sa.ExtractByMask(USGS_1_n33w111_20240401_tif, Park_Boundary, "INSIDE", "-111.001666666982 32.1036882463363 -110.497480841373 32.3522045741637 GEOGCS[\"GCS_North_American_1983\",DATUM[\"D_North_American_1983\",SPHEROID[\"GRS_1980\",6378137.0,298.257222101]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]]")
    DEM2.save(Extract_by_Mask_2_)


    # Process: Mosaic To New Raster (Mosaic To New Raster) (management)
    MergedDEM = arcpy.management.MosaicToNewRaster(input_rasters=[DEM1, DEM2], output_location=finalProjectModel_gdb, raster_dataset_name_with_extension="MergedDEM", number_of_bands=1)[0]
    MergedDEM = arcpy.Raster(MergedDEM)

    # Process: Project Raster (Project Raster) (management)
    MergedDEMFinal = "Z:\\2024_Spring\\GEOG_3520\\STUDENT\\chunhchan\\Final Project\\Model\\finalProjectModel\\finalProjectModel.gdb\\MergedDEMFinal"
    arcpy.management.ProjectRaster(in_raster=MergedDEM, out_raster=MergedDEMFinal, out_coor_system="PROJCS[\"NAD_1983_UTM_Zone_12N\",GEOGCS[\"GCS_North_American_1983\",DATUM[\"D_North_American_1983\",SPHEROID[\"GRS_1980\",6378137.0,298.257222101]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",-111.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]")
    MergedDEMFinal = arcpy.Raster(MergedDEMFinal)

    # Process: Con (Con) (sa)
    ConDemFrog = "Z:\\2024_Spring\\GEOG_3520\\STUDENT\\chunhchan\\Final Project\\Model\\finalProjectModel\\finalProjectModel.gdb\\ConDemFrog"
    Con = ConDemFrog
    ConDemFrog = arcpy.sa.Con(MergedDEMFinal, Input_true_raster_or_constant_value, Input_false_raster_or_constant_value, "VALUE >= 1000 And VALUE <= 2790")
    ConDemFrog.save(Con)


    # Process: Raster to Polygon (Raster to Polygon) (conversion)
    DemFrogPoly = "Z:\\2024_Spring\\GEOG_3520\\STUDENT\\chunhchan\\Final Project\\Model\\finalProjectModel\\finalProjectModel.gdb\\DemFrogPoly"
    with arcpy.EnvManager(outputMFlag="Disabled", outputZFlag="Disabled"):
        arcpy.conversion.RasterToPolygon(in_raster=ConDemFrog, out_polygon_features=DemFrogPoly)

    # Process: Con (2) (Con) (sa)
    ConDemSnake = "Z:\\2024_Spring\\GEOG_3520\\STUDENT\\chunhchan\\Final Project\\Model\\finalProjectModel\\finalProjectModel.gdb\\ConDemSnake"
    Con_2_ = ConDemSnake
    ConDemSnake = arcpy.sa.Con(MergedDEMFinal, Input_true_raster_or_constant_value_3_, Input_false_raster_or_constant_value_2_, "VALUE >= 40 And VALUE <= 2590")
    ConDemSnake.save(Con_2_)
    

    # Process: Raster to Polygon (2) (Raster to Polygon) (conversion)
    DemSnakePoly = "Z:\\2024_Spring\\GEOG_3520\\STUDENT\\chunhchan\\Final Project\\Model\\finalProjectModel\\finalProjectModel.gdb\\DemSnakePoly"
    with arcpy.EnvManager(outputMFlag="Disabled", outputZFlag="Disabled"):
        arcpy.conversion.RasterToPolygon(in_raster=ConDemSnake, out_polygon_features=DemSnakePoly)
    arcpy.management.AddField("VegetationFinal", "Frog", "short")

    arcpy.management.AddField("VegetationFinal", "Snake", "short")

    vegfields = arcpy.ListFields(r"Z:\2024_Spring\GEOG_3520\STUDENT\chunhchan\Final Project\Model\finalProjectModel\finalProjectModel.gdb\VegetationFinal")

    for field in vegfields:
    print(f"{field.name} has a type of {field.type} with a length of {field.length}")

    arcpy.management.CalculateField("VegetationFinal", "Frog", 0)

    arcpy.management.CalculateField("VegetationFinal", "Snake", 0)

    vegfc = "VegetationFinal"

    vegfields = ["Snake", "Frog", "MapClass"]


    with arcpy.da.UpdateCursor(vegfc, vegfields) as cursor:
        for row in cursor:
            map_class = row[2]
            if "Flooded" in map_class or "Riparian" in map_class or "Floodplain" in map_class:
                row[0] = 1  
                row[1] = 1  
            elif "Quercus" in map_class and "Forest" in map_class:
                row[0] = 1  
            elif "Quercus" in map_class and "Woodland" in map_class:
                row[1] = 1  
            cursor.updateRow(row)
            print("Snake: {}, Frog: {}".format(row[0], row[1]))
if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace="Z:\\2024_Spring\\GEOG_3520\\STUDENT\\chunhchan\\Final Project\\Model\\finalProjectModel\\finalProjectModel.gdb", workspace="Z:\\2024_Spring\\GEOG_3520\\STUDENT\\chunhchan\\Final Project\\Model\\finalProjectModel\\finalProjectModel.gdb"):
        Model()
