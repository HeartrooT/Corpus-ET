# Corpus-ET
Automatic Corpus Expansion with Topic Transferring by Leveraging LLM

Applicant: Ziming Tang 

Lab name: HZAU-BioNLP

Lab PI: Jingbo Xia

Affiliation: Hubei Key Lab of Agricultural Bioinformatics, Huazhong Agricultural University, Wuhan, China

## Project homepage URL: <https://sites.google.com/view/corpus-et/#h.3j3vg09zwk8k>

## Project Slide: <https://www.google.com/url?q=https://docs.google.com/presentation/d/1MOVAXBKjSHtr4KGyNJ-7f6noVQNjEmamkuqZ004cDM4/edit?usp%3Dsharing&sa=D&source=editors&ust=1705370564249821&usg=AOvVaw0vNSMM753fzGdAbiN8oow1>

# Project Background

In the era of LLM (Large Language Models), how to develop an NLP pipeline for automatic corpus expansion is an interesting issue within the BioNLP community. Corpus construction plays a key role in downstream model building and knowledge discovery in the BioNLP community. However, common corpus construction often has two obvious limitations:

1. Common corpora, such as GENIA[1], Bacteria biotope (BB)[2], and Annotation of Genes with Alteration-Centric function changes (AGAC)[3], are usually manually annotated. This makes it difficult to have a large corpus size, and these annotations are usually limited to abstracts and not extended to full text.

2. These corpora usually focus on specific topics and have a more limited scope of use. For example, GENIA only contains annotations for 9 categories of biological events, including gene expression, transcription, protein catabolism, etc., while the BB corpus focuses only on annotations of associations between microorganisms, habitats, and phenotypes.

The rise of big language modeling has opened our eyes to the possibility of solving the above limitations. On the one hand, LLMs have the powerful generative ability to output similar samples in large quantities under the condition that we provide a small number of samples and appropriate prompts. They are not limited by language styles, which makes it possible to scale up the corpus in terms of size and style. On the other hand, LLMs have a strong semantic comprehension capability to fully capture the underlying semantics behind the annotations, which promises to transfer annotations focusing on specific topics.

During BLAH8, we plan to explore the possibilities of LLM for existing corpus extensions as well as topic migration and to build a complete pipeline to generate the extended corpus. We also aim to explore the possibility of integrating this pipeline into PubAnnotation.

# Aimed Scientific and Engineering Issues for Knowledge Discovery on Rice-Alterome

- Issue 1. Prompt design for text selection under LLM.
- Issue 2. "AGAC to AD," a case study for corpus expansion and topic transferring. (Transfer AGAC Corpus to AD-specific genetic disease by using LLM.)
- Issue 3. More applications for other corpora.
- Issue 4. Tool integration with PubAnnotation.

# References

Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes
<https://arxiv.org/pdf/2305.02301.pdf>

Distilling ChatGPT for Explainable Automated Student Answer Assessment
<https://arxiv.org/pdf/2305.12962.pdf>
