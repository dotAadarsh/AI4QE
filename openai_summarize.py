import os
import openai
import tiktoken

class OpenAISummarize(object):
    openai_key = ""

    def __init__(self, openai_key) -> None:
        self.openai_key = openai_key


    def count_tokens(self, text):
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        return len(encoding.encode(text))


    def chunk_text(self, text, max_tokens=500):
        """
        Breaks up a given text into chunks of at most `max_tokens` tokens.

        Args:
            text (str): The text to chunk.
            max_tokens (int): The maximum number of tokens allowed in each chunk.

        Returns:
            list of str: The chunks of text.
        """
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        tokens = encoding.encode(text)
        chunks = []

        current_chunk = []
        current_token_count = 0

        for token in tokens:
            if current_token_count + 1 <= max_tokens:
                current_chunk.append(token)
                current_token_count += 1
            else:
                chunks.append(encoding.decode(current_chunk))
                current_chunk = [token]
                current_token_count = 1

        if current_chunk:
            chunks.append(encoding.decode(current_chunk))

        return chunks


    def summarize_text(self, text, max_chunk_size=500, max_combined_summary_size=4000):
        """
        Generates a summary of a given text using OpenAI's text-davinci-003 model.

        Args:
            text (str): The text to summarize.
            max_chunk_size (int, optional): The size of each chunk of text to summarize. Defaults to 500.
            max_combined_summary_size (int, optional): The maximum size of the combined summary. Defaults to 4000.

        Returns:
            str: The generated summary of the text.
        """
        openai.api_key = self.openai_key
        model_engine = "text-davinci-003"
        prompt_template = "{}\n\nTl;dr (max 200 words)"

        def recursive_summarize(text):
            """
            Recursively generates a summary of a given text.

            Args:
                text (str): The text to summarize.

            Returns:
                str: The generated summary of the text.
            """
            chunks = self.chunk_text(text, max_chunk_size)
            summaries = []

            # Summarize each chunk separately using the OpenAI API
            for chunk in chunks:
                prompt = prompt_template.format(chunk)

                response = openai.Completion.create(
                    engine=model_engine,
                    prompt=prompt,
                    max_tokens=150,
                    n=1,
                    stop=None,
                    temperature=0.5,
                )

                summary = response.choices[0].text.strip()
                summaries.append(summary)

            combined_summary = " ".join(summaries)

            if self.count_tokens(combined_summary) > max_combined_summary_size:
                return recursive_summarize(combined_summary)
            else:
                return combined_summary

        final_summary = recursive_summarize(text)

        cohesion_prompt = f"{final_summary}\n\nTl;dr (max 2 paragraphs)"

        response = openai.Completion.create(
            engine=model_engine,
            prompt=cohesion_prompt,
            temperature=0.7,
            max_tokens=300,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=1,
        )

        rewritten_summary = response.choices[0].text.strip()

        return rewritten_summary
