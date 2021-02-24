
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
                    "filter": {},
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/2acfa618-fce6-49fa-a584-231d2ab76e3d.svg"
                },
                {
                    "id": "cb00010c-de0e-401f-85aa-17258f37df16",
                    "name": "Case",
                    "description": null,
                    "filter": {},
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/Catalogue/case.svg"
                },
                {
                    "id": "7b2a1770-1a52-4e04-aa3e-7432f50018c6",
                    "name": "Motherboard",
                    "description": null,
                    "filter": {},
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/Catalogue/motherboard.svg"
                },
                {
                    "id": "f6e8f7fd-3efa-411c-861e-096a36e87e3e",
                    "name": "GPU",
                    "description": "GPU category",
                    "filter": {},
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/8cd3adbc-67ca-4a89-9817-1924374e9779.svg"
                },
                {
                    "id": "fb9aa1e1-948f-4bee-98ed-f977ff21b1b5",
                    "name": "Power Supply",
                    "description": "Power Supply category",
                    "filter": {},
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/ed9ba7b8-cd0a-403b-ba0f-ecba31226468.svg"
                },
                {
                    "id": "b0cdc0b1-fde6-47e9-9675-eb8859c18663",
                    "name": "Internal Memory Module",
                    "description": "Internal Memory Module category",
                    "filter": {},
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/8df51d46-c696-4cca-8a45-9ac0cad41476.svg"
                },
                {
                    "id": "42194d5b-052f-4781-bf5b-d16985078425",
                    "name": "Storage",
                    "description": "Storage category",
                    "filter": {},
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/Catalogue/storage.svg"
                },
                {
                    "id": "6b9af510-daaf-4584-bd52-bb580a96b1ed",
                    "name": "Fan",
                    "description": "Fan category",
                    "filter": {},
                    "children": null,
                    "imageUri": "https://22entertainment-gaming.s3-us-west-1.amazonaws.com/UI_Images/0dc05ed1-5644-4abc-8fe8-69d1cba808d1.svg"
                },
                {
                    "id": "75fa50be-29e0-41aa-8994-1c8efa81468f",
                    "name": "Air Cooler",
                    "description": "Air Cooler category",
                    "filter": {},
                    "children": null,
                    "imageUri": "https://22entertainment-gaming.s3-us-west-1.amazonaws.com/UI_Images/Catalogue/Air.svg"
                },
                {
                    "id": "11efcdf2-8713-4955-921a-cb374223ae57",
                    "name": "AIO",
                    "description": "AIO category",
                    "filter": {},
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
                    "filter": {},
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/Catalogue/keyboards.svg"
                },
                {
                    "id": "0c98bef6-b804-456c-ba83-ac6f55b974b2",
                    "name": "Headsets",
                    "description": "Headsets",
                    "filter": {},
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/Catalogue/headsets.svg"
                },
                {
                    "id": "b1edc914-c67e-4312-99f2-03c6a6916ce8",
                    "name": "Monitors",
                    "description": "Monitors",
                    "filter": {},
                    "children": null,
                    "imageUri": "https://dt32ivmrnpnfr.cloudfront.net/UI_Images/Catalogue/monitor.svg"
                },
                {
                    "id": "9fd2253c-53a0-4249-b7a7-a519b65b3067",
                    "name": "Mice",
                    "description": "Mice",
                    "filter": {},
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
                    "filter": {},
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
