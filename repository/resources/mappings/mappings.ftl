<#assign data=providers("FileProvider", { "file" : "/usr/src/app/resources/files/file.csv" })>

@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix data: <http://data.cogito.iot.linkeddata.es/resources/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix facility: <https://cogito.iot.linkeddata.es/def/facility#> .
@prefix process: <https://cogito.iot.linkeddata.es/def/process#> .
@prefix resource: <https://cogito.iot.linkeddata.es/def/resource#> .
@prefix const: <https://cogito.iot.linkeddata.es/def/construction#> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix s4city: <https://saref.etsi.org/saref4city#> .
@prefix saref: <https://saref.etsi.org/core#> .
@prefix resource_type: <http://data.cogito.iot.linkeddata.es/resources/resource_type/> .


<#list data?split("\n") as row>
    <#assign cols=row?split(",")>
    <#if cols?size == 6 && row?index gt 0>
    data:ResourceType_[=cols[1]] owl:sameAs resource_type:[=cols[1]] .
    resource_type:[=cols[1]] owl:sameAs data:ResourceType_[=cols[1]] .

    data:ResourceType_[=cols[1]] a resource:ResourceType ;
        <#if cols[2] == "Equipment">
            a resource:EquipmentType ;
            resource:resourceTypeId [=cols[0]] ;
            resource:name '[=cols[1]]'^^<http://www.w3.org/2001/XMLSchema#string> ;
            resource:initials [=cols[3]] ;
            resource:maxUnit [=cols[4]] ;
            resource:costPerHour [=cols[5]] .

        <#elseif cols[2] == "People">
            a resource:HumanRole ;
            resource:resourceTypeId [=cols[0]] ;
            resource:name '[=cols[1]]'^^<http://www.w3.org/2001/XMLSchema#string> ;
            resource:initials [=cols[3]] ;
            resource:maxUnit [=cols[4]] ;
            resource:costPerHour [=cols[5]] .

        <#else>
            a resource:TrackingTagGroup ;
            resource:resourceTypeId [=cols[0]] ;
            resource:name '[=cols[1]]'^^<http://www.w3.org/2001/XMLSchema#string> ;
            resource:initials [=cols[3]] ;
            resource:maxUnit [=cols[4]] ;
            resource:costPerHour [=cols[5]] .
            
        </#if>
    </#if>
</#list>

<#list data?split("\n") as row>
    <#assign cols=row?split(",")>
    <#if cols?size == 6 && row?index gt 0>
    resource_type:[=cols[1]] a resource:ResourceType ;
        <#if cols[2] == "Equipment">
            a resource:EquipmentType ;
            resource:resourceTypeId [=cols[0]] ;
            resource:name '[=cols[1]]'^^<http://www.w3.org/2001/XMLSchema#string> ;
            resource:initials [=cols[3]] ;
            resource:maxUnit [=cols[4]] ;
            resource:costPerHour [=cols[5]] .

        <#elseif cols[2] == "People">
            a resource:HumanRole ;
            resource:resourceTypeId [=cols[0]] ;
            resource:name '[=cols[1]]'^^<http://www.w3.org/2001/XMLSchema#string> ;
            resource:initials [=cols[3]] ;
            resource:maxUnit [=cols[4]] ;
            resource:costPerHour [=cols[5]] .

        <#else>
            a resource:TrackingTagGroup ;
            resource:resourceTypeId [=cols[0]] ;
            resource:name '[=cols[1]]'^^<http://www.w3.org/2001/XMLSchema#string> ;
            resource:initials [=cols[3]] ;
            resource:maxUnit [=cols[4]] ;
            resource:costPerHour [=cols[5]] .
            
        </#if>
    </#if>
</#list>