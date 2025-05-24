## token budget and chunking strategy

* maximum context window: 32 000 tokens.  
* safety margin: 5 % (≈1 600 tokens) reserved for framework overhead.  
* generatorllm: allocate ≤15 000 tokens for analysis & spec generation, ≤5 000 for plan.  
* executorllm: allocate ≤10 000 tokens for code diff, ≤5 000 for logs.  

### chunking protocol
1. slice input documents on semantic boundaries (section headers, code blocks).  
2. each chunk ≤8 000 tokens.  
3. frameworkllm streams chunks sequentially, preserving order with `chunk_index` metadata.  
4. llms must reassemble context internally before final output.
