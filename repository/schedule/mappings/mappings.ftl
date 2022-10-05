<#assign xpath=handlers('XmlHandler')>
<#assign dataset=providers('FileProvider', { 'file' : '/usr/src/app/schedule/files/file.xml' })>
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
@prefix cost: <http://data.cogito.iot.linkeddata.es/resources/cost/> .
@prefix interval: <http://data.cogito.iot.linkeddata.es/resources/interval/> .

@prefix process_data: <http://data.cogito.iot.linkeddata.es/resources/process/> .
@prefix project: <http://data.cogito.iot.linkeddata.es/resources/project/> .
@prefix task: <http://data.cogito.iot.linkeddata.es/resources/task/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .

data:Project_[=xpath.filter('./Project/Final_Project_ID/text()', dataset)]
    a facility:Project ;
    facility:isRelatedToProcess data:[=xpath.filter('./Project/GUID/text()', dataset)] .

data:Project_[=xpath.filter('./Project/Final_Project_ID/text()', dataset)] owl:sameAs project:[=xpath.filter('./Project/Final_Project_ID/text()', dataset)] .
project:[=xpath.filter('./Project/Final_Project_ID/text()', dataset)] owl:sameAs data:Project_[=xpath.filter('./Project/Final_Project_ID/text()', dataset)] .

data:Process_[=xpath.filter('./Project/Final_Project_ID/text()', dataset)]_[=xpath.filter('./Project/GUID/text()', dataset)]
    a process:Process ;
    process:hasTask
    <#list xpath.filter('./Project/Tasks/Task[*]',dataset)>
    <#items as task>
     data:Task_[=xpath.filter('./Project/Final_Project_ID/text()', dataset)]_[=xpath.filter('./Project/GUID/text()', dataset)]_[=xpath.filter('./Task/UID/text()', task)] <#if task?is_last> ; <#else> , </#if>
    </#items>
    </#list>
    process:processID '[=xpath.filter('./Project/GUID/text()', dataset)]' ;
    process:hasName '[=xpath.filter('./Project/Name/text()', dataset)]' ;
    process:hasCreationDate '[=xpath.filter('./Project/CreationDate/text()', dataset)]'^^<http://www.w3.org/2001/XMLSchema#dateTime>.

data:Process_[=xpath.filter('./Project/Final_Project_ID/text()', dataset)]_[=xpath.filter('./Project/GUID/text()', dataset)] owl:sameAs process_data:[=xpath.filter('./Project/Final_Project_ID/text()', dataset)]_[=xpath.filter('./Project/GUID/text()', dataset)] .

process_data:[=xpath.filter('./Project/Final_Project_ID/text()', dataset)]_[=xpath.filter('./Project/GUID/text()', dataset)] owl:sameAs data:Process_[=xpath.filter('./Project/Final_Project_ID/text()', dataset)]_[=xpath.filter('./Project/GUID/text()', dataset)] .

<#list xpath.filter('./Project/Tasks/Task[*]',dataset)>
<#items as task>
data:Task_[=xpath.filter('./Project/Final_Project_ID/text()', dataset)]_[=xpath.filter('./Project/GUID/text()', dataset)]_[=xpath.filter('./Task/UID/text()', task)] owl:sameAs task:[=xpath.filter('./Project/Final_Project_ID/text()', dataset)]_[=xpath.filter('./Project/GUID/text()', dataset)]_[=xpath.filter('./Task/UID/text()', task)] .

task:[=xpath.filter('./Project/Final_Project_ID/text()', dataset)]_[=xpath.filter('./Project/GUID/text()', dataset)]_[=xpath.filter('./Task/UID/text()', task)] owl:sameAs data:Task_[=xpath.filter('./Project/Final_Project_ID/text()', dataset)]_[=xpath.filter('./Project/GUID/text()', dataset)]_[=xpath.filter('./Task/UID/text()', task)] .

data:Task_[=xpath.filter('./Project/Final_Project_ID/text()', dataset)]_[=xpath.filter('./Project/GUID/text()', dataset)]_[=xpath.filter('./Task/UID/text()', task)]
    a process:Task ;
    facility:isRelatedToProject data:Project_[=xpath.filter('./Project/Final_Project_ID/text()', dataset)] ;
    process:taskId '[=xpath.filter('./Task/GUID/text()', task)]' ;
    process:taskUid '[=xpath.filter('./Task/UID/text()', task)]' ;
    process:hasName '[=xpath.filter('./Task/Name/text()', task)]'^^<http://www.w3.org/2001/XMLSchema#string> ;
    process:hasCreationDate '[=xpath.filter('./Task/CreationDate/text()', task)]'^^<http://www.w3.org/2001/XMLSchema#dateTime> ;
    process:hasPriority '[=xpath.filter('./Task/Priority/text()', task)]'^^<http://www.w3.org/2001/XMLSchema#integer> ;
    process:hasProgress '[=xpath.filter('./Task/RemainingWork/text()', task)]'^^<http://www.w3.org/2001/XMLSchema#string> ;
    process:hasStatus '[=xpath.filter('./Task/ActualWork/text()', task)]'^^<http://www.w3.org/2001/XMLSchema#string>
    <#if xpath.filter('./Task/Childs',task)?trim != '' || xpath.filter('./Task/Parent_WBS',task)?trim != ''>;<#else>.</#if>
    <#if xpath.filter('./Task/Childs',task)?trim != ''>
        process:hasSubTask
        <#assign childs = xpath.filter("./Task/Childs/WBS/text()",task)>
        <#if childs?is_sequence>
            <#list childs as child>
                data:Task_[=child] <#if child?is_last && xpath.filter('./Task/Parent_WBS',task)?trim == ''> . <#elseif child?is_last && xpath.filter('./Task/Parent_WBS',task)?trim != ''> ; <#else> , </#if>
            </#list>
        <#else>
             data:Task_[=childs] <#if xpath.filter('./Task/Parent_WBS',task)?trim == ''> . <#else> ; </#if>
        </#if>
    </#if>
    <#if xpath.filter('./Task/Parent_WBS',task)?trim != ''>
        process:isSubTaskOf data:Task_[=xpath.filter('./Task/Parent_WBS/text()', task)] .
    </#if>
</#items>
</#list>

<#--  Good Pactices -->

project:[=xpath.filter('./Project/Final_Project_ID/text()', dataset)]
    a facility:Project ;
    facility:isRelatedToProcess data:[=xpath.filter('./Project/GUID/text()', dataset)] .

process_data:[=xpath.filter('./Project/Final_Project_ID/text()', dataset)]_[=xpath.filter('./Project/GUID/text()', dataset)]
    a process:Process ;
    process:hasTask
    <#list xpath.filter('./Project/Tasks/Task[*]',dataset)>
    <#items as task>
     task:[=xpath.filter('./Project/Final_Project_ID/text()', dataset)]_[=xpath.filter('./Project/GUID/text()', dataset)]_[=xpath.filter('./Task/UID/text()', task)] <#if task?is_last> ; <#else> , </#if>
    </#items>
    </#list>
    process:processID '[=xpath.filter('./Project/GUID/text()', dataset)]' ;
    process:hasName '[=xpath.filter('./Project/Name/text()', dataset)]' ;
    process:hasCreationDate '[=xpath.filter('./Project/CreationDate/text()', dataset)]'^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<#list xpath.filter('./Project/Tasks/Task[*]',dataset)>
<#items as task>
task:[=xpath.filter('./Project/Final_Project_ID/text()', dataset)]_[=xpath.filter('./Project/GUID/text()', dataset)]_[=xpath.filter('./Task/UID/text()', task)]
    a process:Task ;
    facility:isRelatedToProject project:[=xpath.filter('./Project/Final_Project_ID/text()', dataset)] ;
    process:taskId '[=xpath.filter('./Task/GUID/text()', task)]' ;
    process:taskUid '[=xpath.filter('./Task/UID/text()', task)]' ;
    process:hasName '[=xpath.filter('./Task/Name/text()', task)]'^^<http://www.w3.org/2001/XMLSchema#string> ;
    process:hasCreationDate '[=xpath.filter('./Task/CreationDate/text()', task)]'^^<http://www.w3.org/2001/XMLSchema#dateTime> ;
    process:hasPriority '[=xpath.filter('./Task/Priority/text()', task)]'^^<http://www.w3.org/2001/XMLSchema#integer> ;
    process:hasProgress '[=xpath.filter('./Task/RemainingWork/text()', task)]'^^<http://www.w3.org/2001/XMLSchema#string> ;
    process:hasStatus '[=xpath.filter('./Task/ActualWork/text()', task)]'^^<http://www.w3.org/2001/XMLSchema#string>
    <#if xpath.filter('./Task/Childs',task)?trim != '' || xpath.filter('./Task/Parent_WBS',task)?trim != ''>;<#else>.</#if>
    <#if xpath.filter('./Task/Childs',task)?trim != ''>
        process:hasSubTask
        <#assign childs = xpath.filter("./Task/Childs/WBS/text()",task)>
        <#if childs?is_sequence>
            <#list childs as child>
                task:[=child] <#if child?is_last && xpath.filter('./Task/Parent_WBS',task)?trim == ''> . <#elseif child?is_last && xpath.filter('./Task/Parent_WBS',task)?trim != ''> ; <#else> , </#if>
            </#list>
        <#else>
             task:[=childs] <#if xpath.filter('./Task/Parent_WBS',task)?trim == ''> . <#else> ; </#if>
        </#if>
    </#if>
    <#if xpath.filter('./Task/Parent_WBS',task)?trim != ''>
        process:isSubTaskOf task:[=xpath.filter('./Task/Parent_WBS/text()', task)] .
    </#if>
</#items>
</#list>