use std::fs;
use lopdf::Document;

pub fn get_word_from_pdf(filename: String) -> Result<Vec<String>, String> {
    let files = match fs::read_dir(filename) {
        Ok(a) => a,
        Err(_) => panic!("[ERR] Error, directory not found! PANIC!"),
    };

    println!("[+] Importing files: ");

    let mut res: Vec<String> = Vec::new();

    for file in files {

        let nf = file.unwrap().path();
        println!("[+] Name: {}", nf.display());

        let doc = match Document::load(nf) {
            Ok(document) => document,
            Err(err) => panic!("Error: {}", err),
        };

        let pages = doc.get_pages();
        for (i, _) in pages.iter().enumerate() {
            let page_number = (i+1) as u32;
            let text = match doc.extract_text(&[page_number]) {
                Ok(a) => a,
                Err(_) => Err("No values returned"),
            };
            res.push(text);
        }
    }

    Ok(res)
}

pub fn return_list_of_word(vec_str: Vec<String>) -> Result<Vec<String>, String>{
    let mut res: Vec<String> = Vec::new();
    for str in vec_str {
        let mut str_iter = str.split_ascii_whitespace();
        loop {
            let mut str_split = match str_iter.next() {
                None => {break},
                Some(a) => a.to_string(),
            };

            str_split.retain(|c| is_ok_to_maintain(c));

        }
    }
    Ok(res)
}

fn is_ok_to_maintain(c: char) -> bool {
    true
}