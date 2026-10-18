# PspCheckForJobAffinityViolation

- RVA: `0x00A79648`–`0x00A7967D` (길이 `53` bytes)
- VA: `0x0000000140A79648`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005FC2C`
- 디코드: `17`개 명령, `53/53` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A7966B` → [KeIsSubsetAffinityEx](../../text/2C/KeIsSubsetAffinityEx_function_002CDC80.md) (function, `0x002CDC80`)

### Direct callers
- [PspInsertThread](../9F/PspInsertThread_function_009F0314.md) at `0x009F04F8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A7966B` → [KeIsSubsetAffinityEx](../../text/2C/KeIsSubsetAffinityEx_function_002CDC80.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A79648  48 83 EC 28                     sub rsp, 0x28
00A7964C  8B 81 20 04 00 00               mov eax, dword ptr [rcx + 0x420]
00A79652  4C 8B C2                        mov r8, rdx
00A79655  A8 10                           test al, 0x10
00A79657  75 08                           jne 0x140a79661
00A79659  33 C0                           xor eax, eax
00A7965B  48 83 C4 28                     add rsp, 0x28
00A7965F  C3                              ret
00A79660  CC                              int3
00A79661  48 8D 91 D8 02 00 00            lea rdx, [rcx + 0x2d8]
00A79668  49 8B C8                        mov rcx, r8
00A7966B  E8 10 46 85 FF                  call 0x1402cdc80
00A79670  F7 D8                           neg eax
00A79672  1B C0                           sbb eax, eax
00A79674  F7 D0                           not eax
00A79676  25 01 00 00 C0                  and eax, 0xc0000001
00A7967B  EB DE                           jmp 0x140a7965b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspCheckForJobAffinityViolation(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1056)))) & (16)) != 0) goto loc_00A79661;
    result = 0;
loc_00A7965B:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00A79661:
    result = KeIsSubsetAffinityEx(a2, a1 + 728, a2, a4);
    result = (unsigned int)(-(result));
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (0xC0000001ULL));
    goto loc_00A7965B;
}
```

## 5. (Beta) C Style

```c
int64_t PspCheckForJobAffinityViolation(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x420)))) & (16)) != 0) goto loc_00A79661;
    result = 0;
loc_00A7965B:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00A79661:
    result = KeIsSubsetAffinityEx(Arg2, Arg1 + 728, Arg2, a4);
    result = (uint32_t)(-(result));
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (0xC0000001ULL));
    goto loc_00A7965B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2D8` | `64` | `R` |
| `Arg1` | `+ 0x420` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A79648&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A79648[BB_00A79648]
  bb_00A79659[BB_00A79659]
  bb_00A7965B[BB_00A7965B]
  bb_00A79660[BB_00A79660]
  bb_00A79661[BB_00A79661]
  bb_00A79648 -->|branch| bb_00A79661
  bb_00A79648 -->|fallthrough| bb_00A79659
  bb_00A79659 -->|flow| bb_00A7965B
  bb_00A79660 -->|flow| bb_00A79661
  bb_00A79661 -->|branch| bb_00A7965B
```
