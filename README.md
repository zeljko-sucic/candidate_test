# 2e Systems – Job Applicant Test  

This repository contains the assignment materials for candidates applying to **2e Systems**.  

## Assignment Overview  

The task is split into two main steps:  

### Step 1 – Fix the Existing Script  
The repository includes a script called **`conversion_script.py`**, which was designed to replicate the functionality of a mapping utility. The original utility uses **XML configuration files** to transform data from one format into another.  

- In this case, the configuration file is **`mapper_v01.xml`**, which describes how to convert **`in_v01.json`** into **`out_v01.xml`**.  
- Instead of using the XML file directly, `conversion_script.py` generates a new Python tool called **`transformer.py`**, which performs the transformation.  
- The mechanism works in principle, but it contains a **bug** that you need to identify and fix.  

### Step 2 – Extend and Improve the Script  
Once the script is working correctly, extend it so that it can also handle a new configuration:  

- The script should not only work with **`mapper_v01.xml`**, but also with **`mapper_v02.xml`**.  
- This new configuration should allow transforming **`in_v02.json`** accordingly.  

All the information required to implement this functionality can be inferred from the provided mapper and input files.  


  
