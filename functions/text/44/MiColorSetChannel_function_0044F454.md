# MiColorSetChannel

- RVA: `0x0044F454`–`0x0044F48D` (길이 `57` bytes)
- VA: `0x000000014044F454`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063CEC`
- 디코드: `20`개 명령, `57/57` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0044F484` → [MiAssignDefaultChannel](../31/MiAssignDefaultChannel_function_0031E5B0.md) (function, `0x0031E5B0`)

### Direct callers
- [MiGetHugeRange](../67/MiGetHugeRange_function_00675954.md) at `0x00675A0D`
- [MiGetHugeRange](../67/MiGetHugeRange_function_00675954.md) at `0x00675A1D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0044F454  48 83 EC 28                     sub rsp, 0x28
0044F458  4C 8B C9                        mov r9, rcx
0044F45B  80 FA 02                        cmp dl, 2
0044F45E  74 1C                           je 0x14044f47c
0044F460  41 8B 01                        mov eax, dword ptr [r9]
0044F463  0F B6 CA                        movzx ecx, dl
0044F466  C1 E1 08                        shl ecx, 8
0044F469  33 C8                           xor ecx, eax
0044F46B  81 E1 00 01 00 00               and ecx, 0x100
0044F471  33 C8                           xor ecx, eax
0044F473  41 89 09                        mov dword ptr [r9], ecx
0044F476  48 83 C4 28                     add rsp, 0x28
0044F47A  C3                              ret
0044F47B  CC                              int3
0044F47C  8B 09                           mov ecx, dword ptr [rcx]
0044F47E  C1 E9 09                        shr ecx, 9
0044F481  83 E1 3F                        and ecx, 0x3f
0044F484  E8 27 F1 EC FF                  call 0x14031e5b0
0044F489  8A D0                           mov dl, al
0044F48B  EB D3                           jmp 0x14044f460
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiColorSetChannel(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a2 == 2) goto loc_0044F47C;
loc_0044F460:
    a1 = (unsigned int)((a2) << (8));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a1)))));
    a1 = (unsigned int)((a1) & (256));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a1)))));
    *(unsigned int *)(a1) = (unsigned int)(a1);
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(*(unsigned int *)(a1));
loc_0044F47C:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) >> (9));
    a1 = (unsigned int)((a1) & (63));
    result = MiAssignDefaultChannel(a1, a2, a3, a1);
    goto loc_0044F460;
}
```

## 5. (Beta) C Style

```c
int64_t MiColorSetChannel(void *Arg1, uint8_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg2 == 2) goto loc_0044F47C;
loc_0044F460:
    Arg1 = (uint32_t)((Arg2) << (8));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))));
    Arg1 = (uint32_t)((Arg1) & (256));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))));
    *(uint32_t *)(arg1) = (uint32_t)(Arg1);
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(*(uint32_t *)(arg1));
loc_0044F47C:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) >> (9));
    Arg1 = (uint32_t)((Arg1) & (63));
    result = MiAssignDefaultChannel(Arg1, Arg2, a3, Arg1);
    goto loc_0044F460;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0044F454&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0044F454[BB_0044F454]
  bb_0044F460[BB_0044F460]
  bb_0044F47B[BB_0044F47B]
  bb_0044F47C[BB_0044F47C]
  bb_0044F454 -->|branch| bb_0044F47C
  bb_0044F454 -->|fallthrough| bb_0044F460
  bb_0044F47B -->|flow| bb_0044F47C
  bb_0044F47C -->|branch| bb_0044F460
```
