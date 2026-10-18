# HvMarkHiveWithNoSectionExtend

- RVA: `0x00705B70`–`0x00705BAB` (길이 `59` bytes)
- VA: `0x0000000140705B70`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `16`개 명령, `59/59` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00705BA0` → [HvpViewMapAdjustFlag](../AC/HvpViewMapAdjustFlag_function_00ACDDA4.md) (function, `0x00ACDDA4`)

### Direct callers
- [CmpRecheckHiveVolumePolicy](../../text/46/CmpRecheckHiveVolumePolicy_function_0046EE14.md) at `0x0046EEA4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00705B70  48 83 EC 28                     sub rsp, 0x28
00705B74  8B 81 A0 00 00 00               mov eax, dword ptr [rcx + 0xa0]
00705B7A  BA 00 00 00 08                  mov edx, 0x8000000
00705B7F  85 C2                           test edx, eax
00705B81  75 22                           jne 0x140705ba5
00705B83  0B C2                           or eax, edx
00705B85  89 81 A0 00 00 00               mov dword ptr [rcx + 0xa0], eax
00705B8B  0F BA E0 11                     bt eax, 0x11
00705B8F  73 14                           jae 0x140705ba5
00705B91  48 81 C1 E0 00 00 00            add rcx, 0xe0
00705B98  41 B0 01                        mov r8b, 1
00705B9B  BA 08 00 00 00                  mov edx, 8
00705BA0  E8 FF 81 3C 00                  call 0x140acdda4
00705BA5  48 83 C4 28                     add rsp, 0x28
00705BA9  C3                              ret
00705BAA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvMarkHiveWithNoSectionExtend(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((((unsigned int)((unsigned int)(0x8000000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 160))))) != 0) goto loc_00705BA5;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 160))) | ((unsigned int)((unsigned int)(0x8000000ULL))));
    *(unsigned int *)(a1 + 160) = (unsigned int)(result);
    if (!(condition_is_above_or_equal)) {
        a1 = (a1) + (224);
        a3 = 1;
        a2 = 8;
        result = HvpViewMapAdjustFlag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvMarkHiveWithNoSectionExtend(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((((uint32_t)((uint32_t)(0x8000000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xA0))))) != 0) goto loc_00705BA5;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xA0))) | ((uint32_t)((uint32_t)(0x8000000ULL))));
    *(uint32_t *)(arg1 + 0xA0) = (uint32_t)(result);
    if (!(condition_is_above_or_equal)) {
        Arg1 = (Arg1) + (224);
        a3 = 1;
        a2 = 8;
        result = HvpViewMapAdjustFlag(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xA0` | `32` | `R` |
| `Arg1` | `+ 0xA0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00705B70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00705B70[BB_00705B70]
  bb_00705B83[BB_00705B83]
  bb_00705B91[BB_00705B91]
  bb_00705BA5[BB_00705BA5]
  bb_00705BAA[BB_00705BAA]
  bb_00705B70 -->|branch| bb_00705BA5
  bb_00705B70 -->|fallthrough| bb_00705B83
  bb_00705B83 -->|branch| bb_00705BA5
  bb_00705B83 -->|fallthrough| bb_00705B91
  bb_00705B91 -->|flow| bb_00705BA5
```
