# EtwCheckSecurityLoggerAccess

- RVA: `0x00A0FE94`–`0x00A0FEBE` (길이 `42` bytes)
- VA: `0x0000000140A0FE94`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009D63C`
- 디코드: `15`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A0FEAC` → [RtlTestProtectedAccess](../A1/RtlTestProtectedAccess_function_00A100C8.md) (function, `0x00A100C8`)

### Direct callers
- [EtwpQueryTrace](../8B/EtwpQueryTrace_function_008BF8B0.md) at `0x008BF994`
- [EtwpCheckNotificationAccess](../8C/EtwpCheckNotificationAccess_function_008C770C.md) at `0x008C778C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A0FE94  48 83 EC 28                     sub rsp, 0x28
00A0FE98  84 D2                           test dl, dl
00A0FE9A  75 08                           jne 0x140a0fea4
00A0FE9C  33 C0                           xor eax, eax
00A0FE9E  48 83 C4 28                     add rsp, 0x28
00A0FEA2  C3                              ret
00A0FEA3  CC                              int3
00A0FEA4  8A 89 FA 05 00 00               mov cl, byte ptr [rcx + 0x5fa]
00A0FEAA  B2 31                           mov dl, 0x31
00A0FEAC  E8 17 02 00 00                  call 0x140a100c8
00A0FEB1  F6 D8                           neg al
00A0FEB3  1B C0                           sbb eax, eax
00A0FEB5  F7 D0                           not eax
00A0FEB7  25 22 00 00 C0                  and eax, 0xc0000022
00A0FEBC  EB E0                           jmp 0x140a0fe9e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwCheckSecurityLoggerAccess(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a2 != 0) goto loc_00A0FEA4;
    result = 0;
loc_00A0FE9E:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00A0FEA4:
    result = RtlTestProtectedAccess(*(unsigned __int8 *)(a1 + 1530), 49, a3, a4);
    result = (unsigned __int8)(-(result));
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (0xC0000022ULL));
    goto loc_00A0FE9E;
}
```

## 5. (Beta) C Style

```c
int64_t EtwCheckSecurityLoggerAccess(void *Arg1, uint8_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg2 != 0) goto loc_00A0FEA4;
    result = 0;
loc_00A0FE9E:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00A0FEA4:
    result = RtlTestProtectedAccess(*(uint8_t *)(arg1 + 0x5FA), 49, a3, a4);
    result = (uint8_t)(-(result));
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (0xC0000022ULL));
    goto loc_00A0FE9E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x5FA` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A0FE94&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A0FE94[BB_00A0FE94]
  bb_00A0FE9C[BB_00A0FE9C]
  bb_00A0FE9E[BB_00A0FE9E]
  bb_00A0FEA3[BB_00A0FEA3]
  bb_00A0FEA4[BB_00A0FEA4]
  bb_00A0FE94 -->|branch| bb_00A0FEA4
  bb_00A0FE94 -->|fallthrough| bb_00A0FE9C
  bb_00A0FE9C -->|flow| bb_00A0FE9E
  bb_00A0FEA3 -->|flow| bb_00A0FEA4
  bb_00A0FEA4 -->|branch| bb_00A0FE9E
```
