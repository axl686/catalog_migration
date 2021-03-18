
-- +pig Name: 005_new_hierarchy
-- +pig Requirements: 
-- +pig Up

UPDATE categories SET hierarchy = '{
    "id": "6823b27b-0b34-4fbd-9bdb-fd4c5c9801a8",
    "name": "Root",
    "description": "Root category",
    "filter": {},
    "children": [
        {
            "id": "f593aa84-9f02-4acc-a2d9-e13342b705ea",
            "name": "Components",
            "description": "Components category",
            "filter": {},
            "children": [
                {
                    "id": "a71397c7-bf6e-4449-8ce8-548cfdc426a7",
                    "name": "CPU",
                    "description": "CPU category",
                    "filter": {
                        "price": {
                            "max": 914,
                            "min": 118,
                            "type": "RANGE",
                            "displayName": "Price"
                        },
                        "manufacturer": {
                            "values": [
                                "AMD",
                                "INTEL"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Manufacturer"
                        },
                        "socket": {
                            "values": [
                                "LGA 1200",
                                "AM4",
                                "LGA 1151"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Socket"
                        }
                    },
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/2acfa618-fce6-49fa-a584-231d2ab76e3d.svg"
                },
                {
                    "id": "cb00010c-de0e-401f-85aa-17258f37df16",
                    "name": "Case",
                    "description": null,
                    "filter": {
                        "price": {
                            "max": 347,
                            "min": 41,
                            "type": "RANGE",
                            "displayName": "Price"
                        },
                        "boardCompatibility": {
                            "values": [
                                "E-ATX",
                                "ATX",
                                "EEB",
                                "NUC",
                                "mITX",
                                "mATX",
                                "DTX"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Board Compatibility"
                        },
                        "manufacturer": {
                            "values": [
                                "Raijintek",
                                "Lian Li",
                                "NZXT",
                                "Antec",
                                "Thermaltake",
                                "Cooler Master",
                                "Fractal"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Manufacturer"
                        }
                    },
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/Catalogue/case.svg"
                },
                {
                    "id": "7b2a1770-1a52-4e04-aa3e-7432f50018c6",
                    "name": "Motherboard",
                    "description": null,
                    "filter": {
                        "price": {
                            "max": 404,
                            "min": 59,
                            "type": "RANGE",
                            "displayName": "Price"
                        },
                        "amdOrIntel": {
                            "values": [
                                "AMD",
                                "Intel"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "AMD or Intel"
                        },
                        "chipset": {
                            "values": [
                                "Z390",
                                "AMD A320",
                                "Intel H410 Express",
                                "Intel B365 Express",
                                "Intel Z390",
                                "AMD B550",
                                "Intel B365",
                                "Intel Z390 Express",
                                "Intel X490",
                                "AMD X570",
                                "Intel Z490",
                                "Intel B460",
                                "AMD B450"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Chipset"
                        },
                        "formFactor": {
                            "values": [
                                "ATX",
                                "mITX",
                                "mATX"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Form Factor"
                        },
                        "manufacturer": {
                            "values": [
                                "ASRock",
                                "Asus",
                                "MSI",
                                "Gigabyte"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Manufacturer"
                        },
                        "socket": {
                            "values": [
                                "LGA 1200",
                                "AM4",
                                "1200",
                                "LGA 1150",
                                "LGA 1151",
                                "1151"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Socket"
                        }
                    },
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/Catalogue/motherboard.svg"
                },
                {
                    "id": "f6e8f7fd-3efa-411c-861e-096a36e87e3e",
                    "name": "GPU",
                    "description": "GPU category",
                    "filter": {
                        "price": {
                            "max": 2436,
                            "min": 149,
                            "type": "RANGE",
                            "displayName": "Price"
                        },
                        "chip": {
                            "values": [
                                "RX 5500 XT",
                                "RX 6800 XT SE",
                                "RX 6800",
                                "RX 6700 XT",
                                "RX 5600 XT",
                                "RTX 3090",
                                "RTX 3070",
                                "RTX 3060 Ti",
                                "RX 5700 XT",
                                "RX 6800 XT",
                                "RTX 3080",
                                "GTX 1650",
                                "RX 6900 XT",
                                "GTX 1660",
                                "RX 580"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Chip"
                        },
                        "chipset": {
                            "values": [
                                "AMD",
                                "NVIDIA"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Chipset"
                        },
                        "manufacturer": {
                            "values": [
                                "PNY",
                                "MSI",
                                "ZOTAC",
                                "Asus",
                                "EVGA",
                                "ASUS",
                                "Sapphire",
                                "Gigabyte"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Manufacturer"
                        }
                    },
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/8cd3adbc-67ca-4a89-9817-1924374e9779.svg"
                },
                {
                    "id": "fb9aa1e1-948f-4bee-98ed-f977ff21b1b5",
                    "name": "Power Supply",
                    "description": "Power Supply category",
                    "filter": {
                        "price": {
                            "max": 205,
                            "min": 45,
                            "type": "RANGE",
                            "displayName": "Price"
                        },
                        "effeciencyRating": {
                            "values": [
                                "80+ Standard",
                                "80+ Bronze",
                                "80+ Gold",
                                "80+ White",
                                "80+ Platinum"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Efficiency Rating"
                        },
                        "formFactor": {
                            "values": [
                                "ATX",
                                "SFX"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Form Factor"
                        },
                        "manufacturer": {
                            "values": [
                                "Seasonic",
                                "Antec",
                                "Silverstone",
                                "Thermaltake",
                                "EVGA",
                                "Corsair",
                                "Cooler Master",
                                "Gigabyte"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Manufacturer"
                        },
                        "modularity": {
                            "values": [
                                "Full-Modular",
                                "Semi-Modular",
                                "Non-Modular"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Modularity"
                        },
                        "wattage": {
                            "max": 935,
                            "min": 405,
                            "type": "RANGE",
                            "displayName": "Wattage"
                        }
                    },
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/ed9ba7b8-cd0a-403b-ba0f-ecba31226468.svg"
                },
                {
                    "id": "b0cdc0b1-fde6-47e9-9675-eb8859c18663",
                    "name": "Internal Memory Module",
                    "description": "Internal Memory Module category",
                    "filter": {
                        "price": {
                            "max": 633,
                            "min": 30,
                            "type": "RANGE",
                            "displayName": "Price"
                        },
                        "capacity": {
                            "values": [
                                "4GB",
                                "64GB Kit (32GBx2)",
                                "128GB Kit (32GBx4)",
                                "32GB",
                                "8GB",
                                "16GB",
                                "16GB Kit (8GBx2)",
                                "32GB Kit (16GBx2)"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Capacity"
                        },
                        "manufacturer": {
                            "values": [
                                "Crucial",
                                "Kingston"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Manufacturer"
                        },
                        "memorySpeed": {
                            "values": [
                                "2666MHz",
                                "2400MHz",
                                "3000MHz",
                                "3200MHz"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Memory Speed, Mhz"
                        },
                        "memoryType": {
                            "values": [
                                "DDR4"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Memory Type"
                        },
                        "numberOfMemoryModules": {
                            "max": 4,
                            "min": 1,
                            "type": "RANGE",
                            "displayName": "Number of memory modules"
                        }
                    },
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/8df51d46-c696-4cca-8a45-9ac0cad41476.svg"
                },
                {
                    "id": "42194d5b-052f-4781-bf5b-d16985078425",
                    "name": "Storage",
                    "description": "Storage category",
                    "filter": {
                        "price": {
                            "max": 405,
                            "min": 31,
                            "type": "RANGE",
                            "displayName": "Price"
                        },
                        "capacity": {
                            "values": [
                                "1.9TB",
                                "480GB",
                                "1TB",
                                "240GB",
                                "120GB",
                                "1000GB",
                                "4TB",
                                "250GB",
                                "6TB",
                                "8TB",
                                "500GB",
                                "2TB",
                                "960GB"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Capacity"
                        },
                        "interface": {
                            "values": [
                                "SATA 6Gb/s",
                                "PCIe G3 x4, NVMe"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Interface"
                        },
                        "manufacturer": {
                            "values": [
                                "Seagate",
                                "Samsung",
                                "Crucial",
                                "Western Digital",
                                "Kingston"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Manufacturer"
                        },
                        "storageType": {
                            "values": [
                                "Platter",
                                "SSD"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Storage Type"
                        }
                    },
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/Catalogue/storage.svg"
                },
                {
                    "id": "6b9af510-daaf-4584-bd52-bb580a96b1ed",
                    "name": "Fan",
                    "description": "Fan category",
                    "filter": {
                        "price": {
                            "max": 143,
                            "min": 12,
                            "type": "RANGE",
                            "displayName": "Price"
                        },
                        "connectorType": {
                            "values": [
                                "3-Pin",
                                "4-Pin"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Connector Type"
                        },
                        "manufacturer": {
                            "values": [
                                "Cooler Master",
                                "Fractal",
                                "Corsair"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Manufacturer"
                        },
                        "size": {
                            "values": [
                                "92mm",
                                "80mm",
                                "360mm",
                                "240mm",
                                "140mm",
                                "120mm"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Size"
                        }
                    },
                    "children": null,
                    "imageUri": "https://22entertainment-gaming.s3-us-west-1.amazonaws.com/UI_Images/0dc05ed1-5644-4abc-8fe8-69d1cba808d1.svg"
                },
                {
                    "id": "75fa50be-29e0-41aa-8994-1c8efa81468f",
                    "name": "Air Cooler",
                    "description": "Air Cooler category",
                    "filter": {
                        "price": {
                            "max": 147,
                            "min": 20,
                            "type": "RANGE",
                            "displayName": "Price"
                        },
                        "connectorType": {
                            "values": [
                                "4-Pin"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Connector Type"
                        },
                        "manufacturer": {
                            "values": [
                                "Raijintek",
                                "Cooler Master",
                                "MSI"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Manufacturer"
                        },
                        "size": {
                            "values": [
                                "120mm",
                                "92mm",
                                "160mm"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Size"
                        }
                    },
                    "children": null,
                    "imageUri": "https://22entertainment-gaming.s3-us-west-1.amazonaws.com/UI_Images/Catalogue/Air.svg"
                },
                {
                    "id": "11efcdf2-8713-4955-921a-cb374223ae57",
                    "name": "AIO",
                    "description": "AIO category",
                    "filter": {
                        "price": {
                            "max": 194,
                            "min": 61,
                            "type": "RANGE",
                            "displayName": "Price"
                        },
                        "manufacturer": {
                            "values": [
                                "Cooler Master",
                                "Corsair",
                                "MSI",
                                "NZXT"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Manufacturer"
                        },
                        "size": {
                            "values": [
                                "120mm",
                                "240mm",
                                "280mm",
                                "360mm"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Size"
                        }
                    },
                    "children": null,
                    "imageUri": "https://22entertainment-gaming.s3-us-west-1.amazonaws.com/UI_Images/Catalogue/AIO.svg"
                }
            ],
            "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/98fff6a8-acd5-4ea3-a54b-4ebfefd7b291.png"
        },
        {
            "id": "173a2c62-bd6e-4f33-8c5d-9f61f7269e65",
            "name": "Computers",
            "description": "Computers category",
            "filter": {},
            "children": null,
            "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/1dcca50d-c683-4ed4-8f6f-a3f4f550760c.png"
        },
        {
            "id": "dc18ee26-66f5-494f-9240-238d9158b04c",
            "name": "Accessories & Peripherals",
            "description": "Accessories & Peripherals category",
            "filter": {},
            "children": [
                {
                    "id": "001a66ff-0e0f-4bec-baf2-1a35a45c10f8",
                    "name": "Keyboards",
                    "description": "Keyboards",
                    "filter": {
                        "price": {
                            "max": 183,
                            "min": 20,
                            "type": "RANGE",
                            "displayName": "Price"
                        },
                        "keySwitchType": {
                            "values": [
                                "Cherry MX Red",
                                "Blue Switch",
                                "Linear",
                                "Silver",
                                "Scissor Switches",
                                "Hybird",
                                "Membrane",
                                "Non-Mechanical",
                                "Blue",
                                "Tactile",
                                "Cherry MX Blue",
                                "Brown",
                                "Mem-Chanical",
                                "Red"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Key Switch"
                        },
                        "lighting": {
                            "values": [
                                "None",
                                "RGB",
                                "Aura Sync RGB"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Lighting"
                        },
                        "manufacturer": {
                            "values": [
                                "ASUS",
                                "Cooler Master",
                                "Rosewill",
                                "Corsair"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Manufacturer"
                        },
                        "numberOfKeysOrLayout": {
                            "values": [
                                "Compact",
                                "Full-Size",
                                "Ten-Keyless"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Layout"
                        }
                    },
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/Catalogue/keyboards.svg"
                },
                {
                    "id": "0c98bef6-b804-456c-ba83-ac6f55b974b2",
                    "name": "Headsets",
                    "description": "Headsets",
                    "filter": {
                        "price": {
                            "max": 118,
                            "min": 45,
                            "type": "RANGE",
                            "displayName": "Price"
                        },
                        "connectionType": {
                            "values": [
                                "USC Wireless Receiver",
                                "Analog",
                                "USB"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Connection Type"
                        },
                        "manufacturer": {
                            "values": [
                                "ASUS",
                                "Corsair",
                                "MSI"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Manufacturer"
                        },
                        "openOrClosedBack": {
                            "values": [
                                "Closed back",
                                "Open back"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Open or Closed"
                        }
                    },
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/Catalogue/headsets.svg"
                },
                {
                    "id": "b1edc914-c67e-4312-99f2-03c6a6916ce8",
                    "name": "Monitors",
                    "description": "Monitors",
                    "filter": {
                        "price": {
                            "max": 975,
                            "min": 133,
                            "type": "RANGE",
                            "displayName": "Price"
                        },
                        "adaptiveSyncSupport": {
                            "values": [
                                "AMD FreeSync"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Adaptive sync Support"
                        },
                        "manufacturer": {
                            "values": [
                                "ASUS",
                                "MSI",
                                "Gigabyte",
                                "Viewsonic"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Manufacturer"
                        },
                        "nativeResolution": {
                            "values": [
                                "2560*1440",
                                "3840 x 2160",
                                "1920 x 1080",
                                "2560 x 1440"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Native Resolution"
                        },
                        "panelSize": {
                            "values": [
                                "22\"",
                                "27\"",
                                "32\"",
                                "24\"",
                                "25\""
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Panel Size"
                        },
                        "panelType": {
                            "values": [
                                "VA"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Panel Type"
                        },
                        "refreshRate": {
                            "values": [
                                "165Hz"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Refresh Rate"
                        }
                    },
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/Catalogue/monitor.svg"
                },
                {
                    "id": "9fd2253c-53a0-4249-b7a7-a519b65b3067",
                    "name": "Mice",
                    "description": "Mice",
                    "filter": {
                        "price": {
                            "max": 107,
                            "min": 18,
                            "type": "RANGE",
                            "displayName": "Price"
                        },
                        "litOrRgb": {
                            "values": [
                                "RGB",
                                "Lit"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Lit or RGB"
                        },
                        "manufacturer": {
                            "values": [
                                "Cooler Master",
                                "Rosewill",
                                "Corsair"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Manufacturer"
                        },
                        "maxDpi": {
                            "max": 35200,
                            "min": 1080,
                            "type": "RANGE",
                            "displayName": "Maximum DPI"
                        },
                        "numberOfButtons": {
                            "max": 8,
                            "min": 4,
                            "type": "RANGE",
                            "displayName": "Number of Buttons"
                        },
                        "wiredOrWireless": {
                            "values": [
                                "Wireless",
                                "Wired"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Wired or wireless"
                        }
                    },
                    "children": null,
                    "imageUri": "https://22entertainment-gaming.s3-us-west-1.amazonaws.com/UI_Images/Catalogue/mice.svg"
                }
            ],
            "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/6b641421-ac31-4fe1-adec-d1a78024d6ef.png"
        },
        {
            "id": "6eb3072f-1f26-4ece-bf16-dccc83cbb167",
            "name": "Complete Systems",
            "description": "Complete Systems",
            "filter": {},
            "children": [
                {
                    "id": "3f10d8a0-620a-4c3e-9592-70cf45fe31e3",
                    "name": "Laptops",
                    "description": "Laptops",
                    "filter": {
                        "price": {
                            "max": 1978,
                            "min": 1017,
                            "type": "RANGE",
                            "displayName": "Price"
                        },
                        "cPU": {
                            "values": [
                                "Core i7-10875H",
                                "Core i7-10750H"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "CPU"
                        },
                        "gPU": {
                            "values": [
                                "NVIDIA GeForce RTX 2070 SUPER",
                                "NVIDIA GeForce GTX 1660 Ti"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "GPU"
                        },
                        "manufacturer": {
                            "values": [
                                "MSI"
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Manufacturer"
                        },
                        "screenSize": {
                            "values": [
                                "16\"",
                                "17\""
                            ],
                            "type": "CHECKBOX",
                            "displayName": "Screen Size"
                        }
                    },
                    "children": null,
                    "imageUri": "https://22entertainment-gaming.s3-us-west-1.amazonaws.com/UI_Images/Catalogue/Laptop.svg"
                }
            ],
            "imageUri": ""
        }
    ],
    "imageUri": ""
}' WHERE id = '6823b27b-0b34-4fbd-9bdb-fd4c5c9801a8';

-- +pig Down
