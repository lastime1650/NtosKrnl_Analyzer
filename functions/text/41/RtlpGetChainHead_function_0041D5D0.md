# RtlpGetChainHead

- RVA: `0x0041D5D0`–`0x0041D60B` (길이 `59` bytes)
- VA: `0x000000014041D5D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `17`개 명령, `59/59` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlContractHashTable](RtlContractHashTable_function_0041D260.md) at `0x0041D2A8`
- [RtlContractHashTable](RtlContractHashTable_function_0041D260.md) at `0x0041D2B6`
- [RtlExpandHashTable](RtlExpandHashTable_function_0041D3A0.md) at `0x0041D409`
- [RtlStronglyEnumerateEntryHashTable](RtlStronglyEnumerateEntryHashTable_function_0041D570.md) at `0x0041D590`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0041D5D0  81 79 08 80 00 00 00            cmp dword ptr [rcx + 8], 0x80
0041D5D7  4C 8B 41 20                     mov r8, qword ptr [rcx + 0x20]
0041D5DB  77 0B                           ja 0x14041d5e8
0041D5DD  8B C2                           mov eax, edx
0041D5DF  48 C1 E0 04                     shl rax, 4
0041D5E3  49 03 C0                        add rax, r8
0041D5E6  C3                              ret
0041D5E7  CC                              int3
0041D5E8  8D 82 80 00 00 00               lea eax, [rdx + 0x80]
0041D5EE  C7 44 24 08 00 00 00 00         mov dword ptr [rsp + 8], 0
0041D5F6  0F BD C8                        bsr ecx, eax
0041D5F9  BA 01 00 00 00                  mov edx, 1
0041D5FE  D3 E2                           shl edx, cl
0041D600  33 D0                           xor edx, eax
0041D602  8D 41 F9                        lea eax, [rcx - 7]
0041D605  4D 8B 04 C0                     mov r8, qword ptr [r8 + rax*8]
0041D609  EB D2                           jmp 0x14041d5dd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpGetChainHead(__int64 a1, __int64 a2)
{
    __int64 result;
    unsigned int v_stack_p8;

    if ((*(unsigned int *)(a1 + 8)) > 128) goto loc_0041D5E8;
loc_0041D5DD:
    result = ((unsigned int)((unsigned int)(a2))) << (4);
    result = (result) + (*(unsigned __int64 *)(a1 + 32));
    return result;
loc_0041D5E8:
    v_stack_p8 = 0;
    a2 = (unsigned int)((1) << ((unsigned __int8)(a1)));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(a2 + 128)));
    goto loc_0041D5DD;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpGetChainHead(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    uint32_t v_stack_p8;

    if ((*(uint32_t *)(arg1 + 0x8)) > 128) goto loc_0041D5E8;
loc_0041D5DD:
    result = ((uint32_t)((uint32_t)(Arg2))) << (4);
    result = (result) + (*(uint64_t *)(arg1 + 0x20));
    return result;
loc_0041D5E8:
    v_stack_p8 = 0;
    Arg2 = (uint32_t)((1) << ((uint8_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(Arg2 + 128)));
    goto loc_0041D5DD;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x80` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0041D5D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0041D5D0[BB_0041D5D0]
  bb_0041D5DD[BB_0041D5DD]
  bb_0041D5E7[BB_0041D5E7]
  bb_0041D5E8[BB_0041D5E8]
  bb_0041D5D0 -->|branch| bb_0041D5E8
  bb_0041D5D0 -->|fallthrough| bb_0041D5DD
  bb_0041D5E7 -->|flow| bb_0041D5E8
  bb_0041D5E8 -->|branch| bb_0041D5DD
```
