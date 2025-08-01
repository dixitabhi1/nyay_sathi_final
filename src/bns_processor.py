
import json

def get_section_details(section_number, bns_data):
    for chapter in bns_data:
        for section in chapter["sections"]:
            if section["section_number"] == section_number:
                return section
    return None

def extract_reasoning(section_title, section_content):
    # Keywords and phrases that indicate reasoning
    reasoning_keywords = [
        "is applicable when", "applies to cases where", "deals with", "punishes for",
        "defines", "aims to prevent", "protects against", "is imposed for",
        "the purpose of this section is", "this section addresses"
    ]

    # Check for explicit reasoning in content
    for keyword in reasoning_keywords:
        if keyword in section_content.lower():
            # Attempt to extract the sentence containing the keyword
            sentences = section_content.split(". ")
            for sentence in sentences:
                if keyword in sentence.lower():
                    return sentence.strip() + "."

    # Fallback to generic reasoning based on title or content
    if "punishment" in section_title.lower():
        return f"This section outlines the punishment for the offense of {section_title.lower().replace('punishment for', '').strip()}."
    elif "offence" in section_title.lower():
        return f"This section defines the offense of {section_title.lower().replace('of offence', '').strip()}."
    elif "right" in section_title.lower():
        return f"This section pertains to the right of {section_title.lower().replace('right of', '').strip()}."
    elif "abetment" in section_title.lower():
        return f"This section deals with the abetment of {section_title.lower().replace('abetment of', '').strip()}."
    else:
        # Default to a summary of the content if no specific reasoning is found
        sentences = section_content.split(". ")
        if len(sentences) > 1:
            return sentences[0].strip() + ". " + sentences[1].strip() + "."
        return section_content.strip()

if __name__ == '__main__':
    with open('/home/ubuntu/split-screen-legal-chatbot/src/bns_data.json', 'r') as f:
        bns_data = json.load(f)

    # Example usage:
    section = get_section_details('101', bns_data)
    if section:
        print(f"Section {section['section_number']}: {section['section_title']}")
        print(f"Content: {section['content']}")
        print(f"Reasoning: {extract_reasoning(section['section_title'], section['content'])}")
    else:
        print("Section not found.")


