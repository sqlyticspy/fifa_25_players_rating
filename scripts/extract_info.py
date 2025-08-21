import asyncio
import json
import os
from crawl4ai import AsyncWebCrawler, JsonCssExtractionStrategy, CrawlerRunConfig, CacheMode

# Load player data
with open("./data/players_rating.json", "r", encoding='utf-8') as f:
    player_data = json.load(f)

# Load schema
with open("./schemas/schema_info.json", "r", encoding='utf-8') as f:
    schema = json.load(f)

async def crawl_player(crawler, config, player):
    url = player["player_url"]
    player_id = player["player_id"]
    
    result = await crawler.arun(url=url, config=config)
    
    if not result.success:
        return None
    
    extracted = json.loads(result.extracted_content)
    
    # Add player_id to each record
    for record in extracted:
        record["player_id"] = player_id
    
    return extracted

async def main():
    extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)
    config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        extraction_strategy=extraction_strategy
    )
    
    # Load existing data
    data_file = "./data/players_info.json"
    if os.path.exists(data_file) and os.path.getsize(data_file) > 0:
        with open(data_file, "r", encoding="utf-8") as f:
            all_data = json.load(f)
    else:
        all_data = []
    
    async with AsyncWebCrawler(verbose=True) as crawler:
        # Process in batches of 5
        for i in range(0, len(player_data), 5):
            batch = player_data[i:i+5]
            
            # Process batch
            tasks = [crawl_player(crawler, config, player) for player in batch]
            results = await asyncio.gather(*tasks)
            
            # Add to all_data
            new_data = [item for sublist in results if sublist for item in sublist]
            all_data.extend(new_data)
            
            # Save after each batch
            with open(data_file, "w", encoding="utf-8") as f:
                json.dump(all_data, f, ensure_ascii=False, indent=4)
            
            print(f"Saved batch {i//5 + 1}, total records: {len(all_data)}")
            
            # Wait 1 second before next batch
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())