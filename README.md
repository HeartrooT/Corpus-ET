# Corpus-ET
Automatic Corpus Expansion with Topic Transferring by Leveraging LLM
1. Project Background
In the era of LLM, how to develop NLP pipeline for automatic corpus expansion is an interesting issue among BioNLP community. 
Corpus construction plays a key role in downstream model building and knowledge discovery in the BioNLP community, and common corpus construction often has two obvious limitations. One is that common corpora, such as GENIA[1], Bacteria biotope(BB)[2], and Annotation of Genes with Alteration-Centric function changes(AGAC)[3], are usually manually annotated, which makes it difficult to have a large corpus size, and these annotations are usually limited to abstracts and not extended to full text. Secondly, these corpora usually focus on specific topics and have a more limited scope of use. For example, GENIA only contains annotations for 9 categories of biological events including gene expression, transcription, protein catabolism etc. , while the BB corpus focuses only on annotations of associations between microorganisms, habitats and phenotypes.
The rise of big language modeling has opened our eyes to the possibility of solving the above limitations. On the one hand, LLMs have the powerful generative ability to output similar samples in large quantities under the condition that we provide a small number of samples and appropriate prompts, and are not limited by language styles, which makes it possible to scale up the corpus in terms of size and style. On the other hand, LLM has a strong semantic comprehension capability to fully capture the underlying semantics behind the annotations, which promises to migrate annotations focusing on specific topics.
During BLAH8, we plan to explore the possibilities of LLM for existing corpus extensions as well as topic migration, and to build a complete pipeline to generate the extended corpus and explore the possibility of integrating this pipeline into PubAnnotation.

Aimed scientific and engineering issues for knowledge discovery on Rice-Alterome
Issue 1. Prompt design for texts selection under LLM 
Issue 2. “AGAC to AD”, a case study for corpus expansion and topic transferring. (Transfer AGAC Corpus to AD-specific genetic disease by using LLM.) 
Issue 3. More applications for other corpora
Issue 4. Tool integration with PubAnnotation 

2. Case Study
2.1 Original corpus
AGAC[3] is a corpus proposed by the HZAU-BioNLP team in BLAH4 and initially released and applied in BLAH5. The corpus focuses on genetic variants that bring about downstream functional changes, and its ** articles containing manual annotations are from PubMed abstracts searched with Cancer as the keyword.

2.2 AGAC Annotation example: AML-Alterome
We have also created an online data browser for querying and viewing the annotated rice corpus at http://lit-evi.hzau.edu.cn/AMLAlterome. As shown in Figure 1, we can query for a specific gene, e.g. TP53, in the data browser. The citation table (top) will displays the all query abstract for this gene, include query gene, genetic alteration, downstream term, the ancestor of the term (we chose the level-2 nodes in the ontology as the categories of their child node), and the number of citation in the corpus. When clicking on a specific row in the citation table, the detail table (bottom) will update the all sentence supports of the records, including the source literature information (PMID, Title, DOI, Journal, Year), whether the sentence is recognized complete regulatory events (IncludeEvent) and colored rich text.
<img width="417" alt="image" src="https://github.com/HeartrooT/Corpus-ET/assets/39959501/a694dbb3-591d-4505-b9d4-cf9ac25aec25">
Figure 1. Online data browser for annotated corpus, AML-Alterome.
2.3 AGAC to AD, From cancer to genetic disease--- Topic transferring. 
Although AGAC has made some progress in mining the AML literature, the size of AGAC's dataset as well as its subject matter continue to limit AGAC's progress and use.
To address this limitation, we plan to use AGAC as a case study for corpus expansion and topic migration using LLM. Specifically, on the one hand, we utilize a small number of AGAC samples as prompt input to force LLM to generate more AGAC annotations and expand the annotations to the full text. On the other hand, we plan to utilize the powerful semantic comprehension capability of LLM to migrate the cancer topic of AGAC to the text of genetic disease, Alzheimer's disease (AD), thus resulting in the construction of AD-AGAC corpus.

3. Possible Applications for More Corpora.
3.1 AGAC to AD
As stated in Section 2.3.
3.2 GENIA to Covid

3.3 BB to 宏基因组
Expansion and topic migration of existing corpora using LLM will be a very valuable topic for resource building in the BioNLP community. Although the project only uses AGAC as a case study for the construction of the pipeline, the pipeline has the potential for a wide range of applications. Specifically, GENIA also contains very few full-text annotations and, due to its background, is unable to annotate the most recent epidemiology, such as Covid-19, whereas an LLM-based pipeline would allow for the migration of this topic. Similarly, the BB corpus has valuable annotations on microbes, habitats, and phenotypic relationships, and there is great potential for application if its annotation topics can be migrated to gut microbes using LLM models.
4. Brief LLM-based Idea 
The application of AGAC to AML has shown potential in capturing gene regulatory events, enhancing disease pathology understanding. However, the AGAC corpus is limited in size, with only 627 abstracts in its most recent iteration. This limitation poses several challenges. Firstly, abstracts offer limited information, with substantial research findings often hidden in the full-text section, which typically adopts a distinct descriptive style compared to the abstract, making AGAC less effective for event extraction from full-text. Secondly, AGAC's small size and complex information structure hindered its performance in evaluation tasks, such as BioNLP-OST 2019 and CHIP2022. To address these issues, we plan to leverage the semantic comprehension capability of LLM. We aim to construct a compact, representative prompt dataset from AGAC manually. We will design a prompt for LLM to incorporate this dataset and generate AGAC-like annotations for full-text sections. Subsequently, we intend to evaluate the augmented AGAC corpus in a relevant task, enhancing downstream deep learning models by incorporating this newly generated data and obtaining comparable evaluation metrics with the original corpus.
In contrast, AGAC, designed for cancer text annotation, may excel in gene regulatory event mining for AML. However, for genetic diseases like Alzheimer's disease, there is a greater need to capture downstream regulation from genetic alterations to comprehend pathomechanisms. AGAC might encounter performance limitations in the context of genetic diseases. Following the successful augmentation of AGAC using LLM, we plan to apply a similar approach to annotate text related to Alzheimer's disease (AD). We will construct a concise and representative prompt dataset and instruct LLM to annotate both abstracts and full texts of AD research papers, generating a new corpus in the corresponding format. Subsequently, we will employ downstream deep learning models to demonstrate that the AD-AGAC corpus generated by LLM exhibits comparable learning capabilities.

5. Discussion Points in BLAH8
Issue 1. Prompt design for texts selection under LLM 
Discuss the methods and criteria for selecting AGAC sample.
Evaluate the representativeness and balance of the constructed datasets.
Discuss potential improvements and refinements to enhance dataset quality.

Issue 2. “AGAC to AD”, a case study for corpus expansion and topic transferring. 
Prompt Design and AML Gene Regulatory Event Generation
Design prompts for describing the task and providing sample data to guide LLM generation.
Review and critique the prompt design for expanding AGAC corpus generation.
Generate expanded AGAC corpus using example data based on an online version of ChatGPT.

Issue 3. More applications for other corpora
Build the ChatGPT 3.5 API-based experimental platform.
Explore the technical aspects of using the API for batch generation.
Conduct batch generation of novel AGAC corpus using the API.
Discuss and test the feasibility and efficiency of the API for batch annotation.

Issue 4. Tool integration with PubAnnotation
Evaluation of the generated AGAC extended corpus using downstream deep learning models.
Generation of AGAC corpus in AD context using LLM models.
Evaluation of downstream deep learning models and manual inspection of the generated AD-AGAC corpus.

Day 5. Corpus Curation and Online Presentation
Evaluation of downstream deep learning models and manual inspection of the generated AD-AGAC corpus.
Organize the extended AGAC corpus and the generated AD-AGAC corpus and distribute them on the PubAnnotation platform.
Reference
[1] Kim, J-D., et al. "GENIA corpus—a semantically annotated corpus for bio-textmining." 	Bioinformatics 19.suppl_1 (2003): i180-i182.
[2] Bossy, Robert, et al. "Bacteria biotope at BioNLP open shared tasks 2019." Proceedings of 	the 	5th 	workshop on BioNLP open shared tasks. 2019.
[3] Wang, Yuxing, et al. "Guideline design of an active gene annotation corpus for the purpose of 	drug repurposing." 2018 11th International Congress on Image and Signal Processing, BioMedical 	Engineering and Informatics (CISP-BMEI). IEEE, 2018. 	https://hzaubionlp.com/agac/
