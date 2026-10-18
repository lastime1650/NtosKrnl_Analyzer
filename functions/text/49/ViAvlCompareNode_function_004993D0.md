# ViAvlCompareNode

- RVA: `0x004993D0`–`0x0049940D` (길이 `61` bytes)
- VA: `0x00000001404993D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `23`개 명령, `61/61` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004993D0  4C 8B 0A                        mov r9, qword ptr [rdx]
004993D3  4D 8B 10                        mov r10, qword ptr [r8]
004993D6  4D 3B CA                        cmp r9, r10
004993D9  75 09                           jne 0x1404993e4
004993DB  B9 02 00 00 00                  mov ecx, 2
004993E0  8B C1                           mov eax, ecx
004993E2  C3                              ret
004993E3  CC                              int3
004993E4  72 12                           jb 0x1404993f8
004993E6  49 8B 48 08                     mov rcx, qword ptr [r8 + 8]
004993EA  49 03 CA                        add rcx, r10
004993ED  4C 3B C9                        cmp r9, rcx
004993F0  1B C9                           sbb ecx, ecx
004993F2  F7 D9                           neg ecx
004993F4  FF C1                           inc ecx
004993F6  EB E8                           jmp 0x1404993e0
004993F8  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
004993FC  49 03 C9                        add rcx, r9
004993FF  4C 3B D1                        cmp r10, rcx
00499402  B9 02 00 00 00                  mov ecx, 2
00499407  1B C0                           sbb eax, eax
00499409  23 C8                           and ecx, eax
0049940B  EB D3                           jmp 0x1404993e0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViAvlCompareNode(__int64 a1, __int64 a2, __int64 a3)
{
    if ((*(unsigned __int64 *)(a2)) != (*(unsigned __int64 *)(a3))) goto loc_004993E4;
loc_004993E0:
    return 2;
loc_004993E4:
    if ((*(unsigned __int64 *)(a2)) < (*(unsigned __int64 *)(a3))) goto loc_004993F8;
    a1 = (*(unsigned __int64 *)(a3 + 8)) + (*(unsigned __int64 *)(a3));
    a1 = (unsigned int)(-(a1));
    a1 = (unsigned int)((a1) + 1);
    goto loc_004993E0;
loc_004993F8:
    a1 = (*(unsigned __int64 *)(a2 + 8)) + (*(unsigned __int64 *)(a2));
    a1 = (unsigned int)((2) & (2));
    goto loc_004993E0;
}
```

## 5. (Beta) C Style

```c
int64_t ViAvlCompareNode(int64_t Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    if ((*(uint64_t *)(arg2)) != (*(uint64_t *)(arg3))) goto loc_004993E4;
loc_004993E0:
    return 2;
loc_004993E4:
    if ((*(uint64_t *)(arg2)) < (*(uint64_t *)(arg3))) goto loc_004993F8;
    Arg1 = (*(uint64_t *)(arg3 + 0x8)) + (*(uint64_t *)(arg3));
    Arg1 = (uint32_t)(-(Arg1));
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_004993E0;
loc_004993F8:
    Arg1 = (*(uint64_t *)(arg2 + 0x8)) + (*(uint64_t *)(arg2));
    Arg1 = (uint32_t)((2) & (2));
    goto loc_004993E0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004993D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004993D0[BB_004993D0]
  bb_004993DB[BB_004993DB]
  bb_004993E0[BB_004993E0]
  bb_004993E3[BB_004993E3]
  bb_004993E4[BB_004993E4]
  bb_004993E6[BB_004993E6]
  bb_004993F8[BB_004993F8]
  bb_004993D0 -->|branch| bb_004993E4
  bb_004993D0 -->|fallthrough| bb_004993DB
  bb_004993DB -->|flow| bb_004993E0
  bb_004993E3 -->|flow| bb_004993E4
  bb_004993E4 -->|branch| bb_004993F8
  bb_004993E4 -->|fallthrough| bb_004993E6
  bb_004993E6 -->|branch| bb_004993E0
  bb_004993F8 -->|branch| bb_004993E0
```
