const NOT_GOOD_WORD: [char; 18] = ['.', '?', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '0', '[', ']', '-', ';', ',', '"'];
const MIN_WORD: usize = 2;

fn could_replace(c: char) -> bool {
    for not_good_w in NOT_GOOD_WORD { if c == not_good_w {return false;} }
    true
}

pub(crate) fn transfer_to_hashmap(document: Document) -> HashMap<String, i32>{
    let mut words: HashMap<String, i32> = HashMap::new();

    let pages = document.get_pages();

    for (i, _) in pages.iter().enumerate() {
        let page_number = (i + 1) as u32;
        let text = match document.extract_text(&[page_number]) {
            Ok(a) => a,
            Err(_) => panic!("No str returned"),
        };

        let mut str_iter = text.split_ascii_whitespace();
        loop {
            let str_split: &str = match str_iter.next() {
                Some(a) => a,
                None => break,
            };

            let mut str = String::from(str_split);

            str.retain(|c| could_replace(c));

            if str.len() <= MIN_WORD {
                continue;
            }

            if !words.contains_key(&str) {
                words.insert(str, 1);
            } else {
                let n = match words.get_key_value(&str) {
                    None => panic!("This should never happen!"),
                    Some(a) => a.1
                };
                words.insert(str, n+1);
                str_iter.next();
            }
        }
    }

    words
}
