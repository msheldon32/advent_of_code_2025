use std::io;
use std::fs;
use std::cmp::{min, max};

use std::io::BufRead;

fn process_ranges(ranges : &mut Vec<(i64, i64)>) -> Result<Vec<(i64, i64)>, std::io::Error> {
    ranges.sort();
    let mut new_ranges : Vec<(i64, i64)> = Vec::new();

    
    for range in ranges {
        // I don't know how to code in Rust :(
        let err = std::io::Error::new(std::io::ErrorKind::Other, "Failed");
        if new_ranges.len() == 0 || new_ranges.last().ok_or(err)?.1 < range.0 {
            new_ranges.push(*range);
        } else {
            //new_ranges.last()[1] = max(new_ranges.last()[1], range[1]);
            let err = std::io::Error::new(std::io::ErrorKind::Other, "Failed");
            let last = new_ranges.last().ok_or(err)?;
            let new_range = (last.0, max(range.1, last.1));
            new_ranges.pop();
            new_ranges.push(new_range);
        }
    }

    Ok(new_ranges)
}

fn query_range(x : i64, ranges : &Vec<(i64, i64)>) -> bool {
    let mut lo = 0;
    let mut hi = ranges.len();

    while lo < hi {
        let mid = (lo+hi)/2;
        if ranges[mid].0 <= x {
            lo = mid+1;
        } else {
            hi = mid;
        }
    }

    if lo == 0 {
        return false;
    }

    let tup_idx = lo-1;
    println!("Looking for {} at {}", x, tup_idx);
    println!("Tuple: {}-{}", ranges[tup_idx].0, ranges[tup_idx].1);

    if tup_idx < ranges.len() - 1 {
        println!("Next tuple: {}-{}", ranges[tup_idx+1].0, ranges[tup_idx+1].1);
    }

    ranges[tup_idx].1 >= x && ranges[tup_idx].0 <= x
}

fn main() -> io::Result<()>{
    let filename = "input";
    let file = fs::File::open(filename)?;
    let reader = io::BufReader::new(file);

    let mut ranges : Vec<(i64, i64)> = Vec::new();

    let mut range_complete = false;

    let mut total_success = 0;
    let mut total_fresh = 0;

    for line in reader.lines() {
        //println!("{}", line?);
        let line = line?;
        if range_complete {
            let n : i64 = line.parse().expect("Failed to convert to integer");
            if query_range(n, &ranges) {
                total_success += 1;
            }
        } else if line.len() == 0 {
            range_complete = true;
            ranges = process_ranges(&mut ranges)?;

            for range in &ranges {
                println!("Range: {}-{}", range.0, range.1);
                total_fresh += (range.1-range.0) + 1;
            }
        } else {
            let range : Vec<i64> = line.split("-").map(|x| x.parse().expect("Failed to convert to integer")).collect();

            ranges.push((range[0], range[1]));
        }
    }

    println!("Total successes: {}", total_success);
    println!("Total fresh: {}", total_fresh);

    Ok(())
}
