# Discussion.md

## Solutions Considered
1. **Loading Entire File into Memory** (Not feasible for 1TB logs)
2. **Line-by-Line Streaming Read** (Efficient and used in the final solution)
3. **Parallel Processing with Multiprocessing** (Optional optimization)

## Final Solution Summary
- Used streaming read for memory efficiency.
- Writes matching logs directly to an output file.
- Optimized for speed by avoiding unnecessary processing.