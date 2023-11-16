mod hashmap_elaboration;
mod graph;
mod dataset;

use lopdf::Document;
use std::fs;
use std::collections::HashMap;
use std::string::String;

const PATH: &str = "./pdf/";

struct Word {
    present_in: Vec<usize>,
    count: Vec<i32>,
    filename: String,
}

fn elaborate_over_hm(vec_hm: &Vec<HashMap<String, i32>>, graph: &mut Vec<Word>) -> Vec<Word>{
    let mut hm_correlate: Vec<Word> = Vec::new();

    for first in vec_hm.iter().enumerate() {

        let mut tmp_correlate: HashMap<String, i32> = HashMap::new();
        for second in vec_hm.iter().enumerate() {

            if first.0 != second.0 {
                for (elem, _) in first.1 {

                    /*let value: i32 = match second.1.get(elem) {
                        None => continue,
                        Some(a) => {
                            graph.push(Word{
                                count: *a,
                                present_in:
                            });
                            *a
                        },
                    };*/

                    let _ = match second.1.get(elem) {
                        None => {continue}
                        Some(_) => {}
                    };

                }
            }
        }
    }

    hm_correlate
}

fn main() {



    let common_w = elaborate_over_hm(&wv, &graph);
    for (key, value) in common_w {
        println!("Common: {}, {}", key, value);
    }
}
