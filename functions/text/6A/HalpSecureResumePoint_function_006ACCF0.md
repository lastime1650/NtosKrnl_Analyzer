# HalpSecureResumePoint

- RVA: `0x006ACCF0`–`0x006ACDD6` (길이 `230` bytes)
- VA: `0x00000001406ACCF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFDB8`
- 디코드: `35`개 명령, `230/230` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006ACD01` → RVA `0x00FC1A90` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006ACDD4` → [HalpResumePoint](HalpResumePoint_function_006ACDE0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006ACCF0  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
006ACCF8  8B C8                           mov ecx, eax
006ACCFA  48 69 C1 C0 05 00 00            imul rax, rcx, 0x5c0
006ACD01  48 03 05 88 4D 91 00            add rax, qword ptr [rip + 0x914d88]
006ACD08  48 05 F0 00 00 00               add rax, 0xf0
006ACD0E  48 8B 98 90 00 00 00            mov rbx, qword ptr [rax + 0x90]
006ACD15  48 8B 88 80 00 00 00            mov rcx, qword ptr [rax + 0x80]
006ACD1C  48 8B 90 88 00 00 00            mov rdx, qword ptr [rax + 0x88]
006ACD23  48 8B B0 A8 00 00 00            mov rsi, qword ptr [rax + 0xa8]
006ACD2A  48 8B B8 B0 00 00 00            mov rdi, qword ptr [rax + 0xb0]
006ACD31  48 8B A0 98 00 00 00            mov rsp, qword ptr [rax + 0x98]
006ACD38  48 8B A8 A0 00 00 00            mov rbp, qword ptr [rax + 0xa0]
006ACD3F  4C 8B 80 B8 00 00 00            mov r8, qword ptr [rax + 0xb8]
006ACD46  4C 8B 88 C0 00 00 00            mov r9, qword ptr [rax + 0xc0]
006ACD4D  4C 8B 90 C8 00 00 00            mov r10, qword ptr [rax + 0xc8]
006ACD54  4C 8B 98 D0 00 00 00            mov r11, qword ptr [rax + 0xd0]
006ACD5B  4C 8B A0 D8 00 00 00            mov r12, qword ptr [rax + 0xd8]
006ACD62  4C 8B A8 E0 00 00 00            mov r13, qword ptr [rax + 0xe0]
006ACD69  4C 8B B0 E8 00 00 00            mov r14, qword ptr [rax + 0xe8]
006ACD70  4C 8B B8 F0 00 00 00            mov r15, qword ptr [rax + 0xf0]
006ACD77  FF 70 44                        push qword ptr [rax + 0x44]
006ACD7A  9D                              popfq
006ACD7B  0F AE 88 00 01 00 00            fxrstor [rax + 0x100]
006ACD82  0F 28 B0 00 02 00 00            movaps xmm6, xmmword ptr [rax + 0x200]
006ACD89  0F 28 B8 10 02 00 00            movaps xmm7, xmmword ptr [rax + 0x210]
006ACD90  44 0F 28 80 20 02 00 00         movaps xmm8, xmmword ptr [rax + 0x220]
006ACD98  44 0F 28 88 30 02 00 00         movaps xmm9, xmmword ptr [rax + 0x230]
006ACDA0  44 0F 28 90 40 02 00 00         movaps xmm10, xmmword ptr [rax + 0x240]
006ACDA8  44 0F 28 98 50 02 00 00         movaps xmm11, xmmword ptr [rax + 0x250]
006ACDB0  44 0F 28 A0 60 02 00 00         movaps xmm12, xmmword ptr [rax + 0x260]
006ACDB8  44 0F 28 A8 70 02 00 00         movaps xmm13, xmmword ptr [rax + 0x270]
006ACDC0  44 0F 28 B0 80 02 00 00         movaps xmm14, xmmword ptr [rax + 0x280]
006ACDC8  44 0F 28 B8 90 02 00 00         movaps xmm15, xmmword ptr [rax + 0x290]
006ACDD0  48 8B 40 78                     mov rax, qword ptr [rax + 0x78]
006ACDD4  EB 0A                           jmp 0x1406acde0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpSecureResumePoint(void)
{
    __int64 result;

    result = ((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))));
    result = (result) + (*(unsigned __int64 *)(v_rip + 9522568));
    result = (result) + (240);
}
```

## 5. (Beta) C Style

```c
void HalpSecureResumePoint(void)
{
    int64_t result;

    result = ((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))) * ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))));
    result = (result) + (*(uint64_t *)(v_rip + 0x914D88));
    result = (result) + (240);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006ACCF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006ACCF0[BB_006ACCF0]
```
