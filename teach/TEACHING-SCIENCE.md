# Teaching Science Evidence Ledger

This file grounds `teach` in learning science and current LLM-tutoring evidence. Use it to justify teaching moves, not to turn every lesson into a literature review.

## Evidence tiers

```text
Tier      Meaning
A+        Multiple meta-analyses or large reviews; robust across settings.
A / A-    Strong evidence with important moderators.
B+ / B    Good evidence; domain/design dependent.
B- / C    Useful but contested, smaller, or easy to overclaim.
C / D     Benchmark, synthetic, preference, or early LLM evidence; useful for design, weak for real learning outcomes.
```

## High-confidence principles

### Learner diagnosis / prior knowledge / misconception probing — A- / B+

Prior knowledge strongly shapes what instruction helps, but diagnosis is method-dependent. A good tutor should gather enough evidence to choose the next teaching move; it should not run a long intake interview or treat self-reported level as ground truth.

Use in `teach`:

- diagnose with a short performance sample whenever practical: predict, classify, solve, debug, explain, or complete a worked step;
- ask only the learner-context questions that change instruction: goal, adjacent experience, and what the learner needs to personally judge vs delegate;
- use misconception-linked distractors, contrast cases, or "why?" prompts when the risk is a false-positive correct answer;
- ask for confidence before feedback when calibration matters;
- update the learner model continuously from attempts, feedback response, retry, and transfer; do not freeze it after the opening diagnostic.

Key sources:

- Dochy, Segers & Buehl (1999), prior knowledge review, DOI: https://doi.org/10.3102/00346543069002145
- Simonsmeier et al. (2022), domain-specific prior knowledge meta-analysis, DOI: https://doi.org/10.1080/00461520.2021.1939700
- Treagust (1988), diagnostic tests for misconceptions, DOI: https://doi.org/10.1080/0950069880100204
- Gierl et al. (2017), multiple-choice distractor review, DOI: https://doi.org/10.3102/0034654317726529
- Corbett & Anderson (1995), knowledge tracing, DOI: https://doi.org/10.1007/BF01099821
- Chi et al. (2001), human tutoring, DOI: https://doi.org/10.1207/s15516709cog2504_1

Caveat: diagnosis is probabilistic. Correct answers, fluent talk, or a learner's label of "beginner"/"advanced" are weak evidence by themselves. Stop diagnosing once the result changes the next teaching move.

### 1. Retrieval practice / testing effect — A+

Practice testing is one of the highest-utility learning techniques. Retrieval is not just assessment; retrieving strengthens later access.

Use in `teach`:

- ask the learner to recall, predict, classify, solve, or explain before revealing;
- prefer short-answer/free recall over recognition-only multiple choice;
- follow errors with feedback and retry.

Key sources:

- Yang et al. (2021), classroom testing meta-analysis, DOI: https://doi.org/10.1037/bul0000309
- Rowland (2014), testing vs restudy meta-analysis, DOI: https://doi.org/10.1037/a0037559
- Adesope et al. (2017), practice testing meta-analysis, DOI: https://doi.org/10.3102/0034654316689306
- Dunlosky et al. (2013), learning techniques review, DOI: https://doi.org/10.1177/1529100612453266

Caveat: retrieval practice is not high-stakes grading. Feedback matters after errors. Transfer needs varied and elaborated retrieval.

### 2. Spaced / distributed practice — A+

Spacing is robust across memory and classroom learning. Massed study often feels better but retains worse.

Use in `teach`:

- create future review prompts;
- start later sessions with due reviews;
- do not treat a one-pass lesson as durable learning.

Key sources:

- Cepeda et al. (2006), 839 assessments / 317 experiments, DOI: https://doi.org/10.1037/0033-2909.132.3.354
- Carpenter et al. (2012), spacing review, DOI: https://doi.org/10.1007/s10648-012-9205-z
- Dunlosky et al. (2013), DOI: https://doi.org/10.1177/1529100612453266

Caveat: optimal interval depends on desired retention interval. Start simple; do not overbuild scheduling.

### 3. Interleaving, variation, and contrast — B+

Interleaving helps learners discriminate similar concepts and choose the right method, but it can overload novices.

Use in `teach`:

- after initial schema formation, mix problem types;
- ask: "Which method applies here, and why?";
- use contrast sets for misconceptions.

Key sources:

- Brunmair & Richter (2019), interleaving meta-analysis, DOI: https://doi.org/10.1037/bul0000209
- Firth et al. (2021), systematic review, DOI: https://doi.org/10.1002/rev3.3266
- Rohrer (2012), DOI: https://doi.org/10.1007/s10648-012-9201-3
- Schmidt & Bjork (1992), desirable difficulties, DOI: https://doi.org/10.1111/j.1467-9280.1992.tb00029.x

Caveat: difficulty is desirable only when it induces useful processing. Use blocked practice first for novices.

### 4. Feedback and formative assessment — A- / B+

Feedback helps when it is specific, task/process-oriented, and actionable. Vague praise, grades, or normative comparison can fail or harm.

Use in `teach`:

- answer: goal, current gap, reason, next action;
- give feedback adjacent to the learner's response;
- let the learner retry immediately.

Key sources:

- Wisniewski et al. (2020), feedback meta-analysis, DOI: https://doi.org/10.3389/fpsyg.2019.03087
- Hattie & Timperley (2007), DOI: https://doi.org/10.3102/003465430298487
- Shute (2008), formative feedback review, DOI: https://doi.org/10.3102/0034654307313795
- Yao & Amos (2024), formative assessment meta-analysis, DOI: https://doi.org/10.1080/13803611.2024.2363831

Caveat: feedback effects are heterogeneous. More feedback is not automatically better.

### 5. Worked examples and fading — A-

Worked examples reduce cognitive load for novices. Guidance should fade toward independent performance.

Use in `teach`:

- worked example → completion problem → faded hints → independent attempt → mixed transfer;
- do not keep advanced learners in worked-example mode.

Key sources:

- Barbieri et al. (2023), worked examples math meta-analysis, DOI: https://doi.org/10.1007/s10648-023-09745-1
- Atkinson et al. (2000), worked examples review, DOI: https://doi.org/10.3102/00346543070002181
- Sweller & Cooper (1985), DOI: https://doi.org/10.1207/s1532690xci0201_3
- Renkl & Atkinson (2003), fading transition, DOI: https://doi.org/10.1207/S15326985EP3801_3

Caveat: expertise reversal. Designs that help novices can hinder knowledgeable learners.

### 6. Cognitive load and multimedia design — A- / B+

Working memory is limited. Good instruction reduces extraneous load while preserving useful cognitive work.

Use in `teach`:

- one goal per screen/turn;
- chunk and segment;
- align labels, diagrams, controls, and feedback spatially;
- remove seductive details and decorative complexity.

Key sources:

- Sweller, van Merrienboer & Paas (2019), DOI: https://doi.org/10.1007/s10648-019-09465-5
- Noetel et al. (2022), multimedia meta-meta-analysis, DOI: https://doi.org/10.3102/00346543211052329
- Mayer & Moreno (2003), reducing cognitive load in multimedia, DOI: https://doi.org/10.1207/S15326985EP3801_6
- Sundararajan & Adesope (2020), seductive details meta-analysis, DOI: https://doi.org/10.1007/s10648-020-09522-4
- Alpizar et al. (2020), signaling meta-analysis, DOI: https://doi.org/10.1007/s11423-020-09748-7

Caveat: reducing cognitive load is not the same as making learning effortless. Preserve retrieval and reasoning.

### 7. Guided instruction beats unguided discovery for novices — A-

Pure discovery is weak for novices. Guided discovery can work when scaffolding and feedback are present.

Use in `teach`:

- model first when prerequisites are missing;
- constrain exploration;
- ask Socratic questions only with a diagnostic or reasoning purpose.

Key sources:

- Kirschner, Sweller & Clark (2006), DOI: https://doi.org/10.1207/s15326985ep4102_1
- Alfieri et al. (2011), discovery meta-analysis, DOI: https://doi.org/10.1037/a0021017
- Mayer (2004), pure discovery critique, DOI: https://doi.org/10.1037/0003-066X.59.1.14

Caveat: this is not anti-active-learning. The target is guided, active learning.

### 8. Self-explanation and elaboration — B+

Prompted self-explanation can improve understanding, especially when prompts focus attention on causal or structural reasoning.

Use in `teach`:

- ask focused prompts: "Why does this step follow?", "What rule applies?", "What would change if X changed?";
- evaluate the explanation's structure, not verbosity.

Key sources:

- Bisra et al. (2018), self-explanation meta-analysis, DOI: https://doi.org/10.1007/s10648-018-9434-x
- Rittle-Johnson et al. (2017), math self-explanation meta-analysis, DOI: https://doi.org/10.1007/s11858-017-0834-z
- Chi et al. (1994), DOI: https://doi.org/10.1207/s15516709cog1803_3
- Chi & Wylie (2014), ICAP framework, DOI: https://doi.org/10.1080/00461520.2014.965823

Caveat: prompts can become busywork or overload. Use sparingly.

### 9. Mastery criteria and deliberate practice — B- / C+

Mastery and deliberate practice help when tasks, feedback, and criteria are valid. They are often overclaimed.

Use in `teach`:

- define micro-skill criteria;
- stop drilling when criterion is met;
- require delayed retrieval before calling something mastered.

Key sources:

- Kulik et al. (1990), mastery learning meta-analysis, DOI: https://doi.org/10.3102/00346543060002265
- Kingston & Nash (2011), formative assessment meta-analysis, DOI: https://doi.org/10.1111/j.1745-3992.2011.00220.x
- Ericsson et al. (1993), deliberate practice, DOI: https://doi.org/10.1037/0033-295X.100.3.363
- Macnamara et al. (2014), deliberate practice meta-analysis, DOI: https://doi.org/10.1177/0956797614535810

Caveat: immediate test success can be fluency, not mastery.

### 10. Transfer and metacognitive calibration — B-

Transfer is hard and rarely automatic. Learners often overestimate fluency.

Use in `teach`:

- include near-to-far transfer ladders;
- compare cases;
- ask confidence before feedback;
- compare confidence to outcome.

Key sources:

- Alfieri et al. (2013), case comparison meta-analysis, DOI: https://doi.org/10.1080/00461520.2013.775712
- Pan & Rickard (2018), transfer of test-enhanced learning, DOI: https://doi.org/10.1037/bul0000151
- Dunlosky & Rawson (2012), overconfidence and learning, DOI: https://doi.org/10.1016/j.learninstruc.2011.08.003
- Sitzmann & Ely (2011), self-regulated learning meta-analysis, DOI: https://doi.org/10.1037/a0022777

Caveat: confidence ratings alone do not teach. They must be compared with outcomes.

## LLM-specific evidence

### Guardrails matter — A

General chatbots can improve immediate task performance while harming later unaided learning.

Use in `teach`:

- require attempts before solutions;
- use hint ladders;
- include no-AI checkpoints;
- do not optimize for convenience alone.

Key source:

- Bastani et al. (2025), high-school math RCT, DOI: https://doi.org/10.1073/pnas.2422633122

### LLM hints can work if checked — A/B

Generated help can match human-authored hints in narrow settings, but correctness checks matter.

Use in `teach`:

- verify generated hints and answer keys;
- use self-consistency or independent checking for generated exercises;
- do not present unchecked generated math/code/factual content as reliable.

Key source:

- Pardos & Bhandari (2024), ChatGPT-generated math help, DOI: https://doi.org/10.1371/journal.pone.0304013

### Purpose-built tutors can beat strong baselines narrowly — A with scope limits

A research-designed AI tutor outperformed an active-learning class in one Harvard physics RCT.

Use in `teach`:

- copy the design principle, not the hype: structured prompts, constrained path, worked solutions, active checks, feedback.

Key source:

- Kestin et al. (2025), Scientific Reports RCT, DOI: https://doi.org/10.1038/s41598-025-97652-6

### Lower effort can reduce depth — B

LLMs can lower cognitive load while producing weaker reasoning.

Use in `teach`:

- distinguish extraneous load from germane effort;
- require reasoning, note-making, retrieval, and transfer.

Key source:

- Stadler, Bannert & Sailer (2024), DOI: https://doi.org/10.1016/j.chb.2024.108386

### AI-driven tutoring systems are promising but heterogeneous — A/B

ITS and AI tutor reviews are generally positive, but effects depend on comparison condition, design, domain, and duration.

Use in `teach`:

- prefer immediate feedback, adaptivity, guided practice, step-level hints, and valid problem selection;
- avoid claiming "LLMs are good tutors" as a general fact.

Key sources:

- Letourneau et al. (2025), K-12 AI-driven ITS systematic review, DOI: https://doi.org/10.1038/s41539-025-00320-7
- Ma et al. (2014), ITS meta-analysis, DOI: https://doi.org/10.1037/a0037123
- VanLehn (2011), tutoring systems comparison, DOI: https://doi.org/10.1080/00461520.2011.611369

### Socratic LLM papers are useful design signals, not strong outcome proof — C/D for learning outcomes

SocraticLM, KELE, GuideEval, and similar work provide useful rubrics and interaction patterns, but much of the evidence is synthetic, benchmark-based, or expert-preference-based rather than real learner outcome RCTs.

Use in `teach`:

- adopt perception → orchestration → elicitation as a design check;
- do not treat Socratic question generation as proof of learning;
- give direct explanation when questioning stalls.

Examples:

- SocraticLM (NeurIPS 2024), DOI: https://doi.org/10.52202/079017-2721
- GuideEval (2025), https://arxiv.org/abs/2508.06583
- KELE (Findings EMNLP 2025), DOI: https://doi.org/10.18653/v1/2025.findings-emnlp.888

## Practical default

When evidence conflicts, choose the boring, robust path:

```text
short direct model → learner retrieval/attempt → specific feedback → retry → transfer → spaced review
```

Avoid novelty unless it improves one of those steps.
