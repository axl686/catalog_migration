
-- +pig Name: 00__items
-- +pig Requirements:
-- +pig Up

UPDATE products SET properties='[{"price": 238.0, "variantId": "4035340b-63dc-40c7-9a38-760cb52c85c2", "manufacturer": "INTEL", "orderLimit": null, "sku": "AS242482", "condition": "new", "salePrice": 0, "availability": "in stock", "salePriceEffectiveDate": null, "descriptions": ["6 Cores / 12 Threads\nSocket Type LGA 1200", "Up to 4. 8 GHz Unlocked", "Compatible with Intel 400 series chipset based motherboards", "Intel Optane Memory Support"], "specifications": "Brand: Intel\nProcessors Type: Desktop\nSeries: Core i5 10th Gen\nName: Core i5-10600K\nModel: BX8070110600K\nCPU Socket Type: LGA 1200\nCore Name: Comet Lake\n# of Cores : 6-Core\n# of Threads: 12\nOperating Frequency: 4.1 GHz\nMax Turbo Frequency: 4.80 GHz\nBus Speed: 8 GT/s\nL3 Cache: 12MB\nManufacturing Tech: 14nm\n64-Bit Support: Yes\nHyper-Threading Support: Yes\nMemory Types: DDR4 2666\nMemory Channel: 2\nVirtualization Technology Support: Yes\nIntegrated Graphics: Intel UHD Graphics 630\nGraphics Base Frequency: 350 MHz\nGraphics Max Dynamic Frequency: 1.2 GHz\nPCI Express Revision: 3.0\nMax Number of PCI Express Lanes: 16\nThermal Design Power: 125W\nCooling Device: Cooling device not included - Processor Only", "images": [], "upc": "735858447652"}]', updated_at=now() WHERE id='f217bef6-818d-47bd-ba5a-b3f343c08e1e' AND store_id='1dbf13e4-a02c-425e-8745-a9ebedb932c2';
UPDATE products SET properties='[{"price": 78.0, "variantId": "7afa6407-fde3-47e3-a436-65e344d66c0e", "manufacturer": "Raijintek", "orderLimit": null, "sku": "AS248618", "condition": "new", "salePrice": 0, "availability": "in stock", "salePriceEffectiveDate": null, "descriptions": ["Aluminum color hair-silk anodized appearance design\nEntire Coating black internally design", "Compatible with ATX POWER SUPPLY", "Compatible with max. 280mm VGA card", "Supports to max. 180mm height CPU cooler"], "specifications": "\nProduct Name: STYX / STYX CLASSIC\nProduct Number: 0R200025~0R200030, 0R200031~0R200036, 0R200037~0R200038, 0R20B00159\nDimension [W\u00d7D\u00d7H]: 210\u00d7360\u00d7335 mm\nWeight: 3.8 kg [N.W.] 5.2 kg [G.W.]\nMaterial: Aluminum 1.5mm [Surface]; SPCC 0.5mm [Interior]\nColor: Black / Red / Silver / Blue / Green / Gold / White / Pink\nM/B Support\t:Micro ATX / Mini-ITX\nDrive Bay: \n\u2022internal 3.5\"HDD\u00d73 + 2.5\"HDD\u00d72 or 3.5\"HDD\u00d71 + 2.5\"HDD\u00d74\n\u2022Slim DVD\u00d71\nExpansion Slot: PCI Slots [Tool-Free]\u00d75\nI/O Panel: USB3.0\u00d72, HD Audio\u00d71\nPower Supply: PS/2 [Internal Bottom-mount]\nCoolingSystem: \n\u2022Rear Fan: 120mm\u00d71 [pre-installed]\n\u2022Top Fan: 120mm\u00d72 or 240mm Radiator [option]\n\u2022Bottom Fan: 120mm\u00d71 [option]\nCPU Cooler Height: 180mm [Max.]\nGraphic Card Length: 280mm [Max.]\nSide Panel Style: Window / Flat", "images": [], "upc": "849939000879"}]', updated_at=now() WHERE id='c72bcf5e-101e-4638-a256-31319d697603' AND store_id='1dbf13e4-a02c-425e-8745-a9ebedb932c2';
UPDATE products SET properties='[{"price": 78.0, "variantId": "74f497af-5988-44ed-9788-0710d152dc5b", "manufacturer": "Raijintek", "orderLimit": null, "sku": "AS248624", "condition": "new", "salePrice": 0, "availability": "in stock", "salePriceEffectiveDate": null, "descriptions": ["Thermally Advantaged Chassis", "Removable Side Panels", "Removable Drive Cages"], "specifications": "\nProduct Name: STYX\nProduct Number: 0R200037\nDimension [W\u00d7D\u00d7H]\t210\u00d7360\u00d7335 mm\nWeight: 3.8 kg [N.W.] 5.2 kg [G.W.]\nMateriall: Aluminum 1.5mm [Surface]; SPCC 0.5mm [Interior]\nColor: White\nM/B Support: Micro ATX / Mini-ITX\nDrive Bay: \n\u2022internal 3.5\"HDD\u00d73 + 2.5\"HDD\u00d72 or 3.5\"HDD\u00d71 + 2.5\"HDD\u00d74\n\u2022Slim DVD\u00d71\nExpansion Slot: PCI Slots [Tool-Free]\u00d75\nI/O Panel: USB3.0\u00d72, HD Audio\u00d71\nPower Supply: PS/2 [Internal Bottom-mount]\nCooling System: \n\u2022Rear Fan: 120mm\u00d71 [pre-installed]\n\u2022Top Fan: 120mm\u00d72 or 240mm Radiator [option]\n\u2022Bottom Fan: 120mm\u00d71 [option]\nCPU Cooler Height: 180mm [Max.]\nGraphic Card Length: 280mm [Max.]\nSide Panel Style: Window / Flat", "images": [], "upc": "849939001135"}]', updated_at=now() WHERE id='7d6d03c2-362a-48a0-8e1c-405ae925d536' AND store_id='1dbf13e4-a02c-425e-8745-a9ebedb932c2';




-- +pig Down

DELETE FROM product_images WHERE product_id IN ();
DELETE FROM product_videos WHERE product_id IN ();
DELETE FROM products WHERE id IN ();
