# RtlXSaveS

- RVA: `0x003D8CE4`–`0x003D8D31` (길이 `77` bytes)
- VA: `0x00000001403D8CE4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `20`개 명령, `77/77` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003D8D2A` → [RtlXSave](RtlXSave_function_003D9D10.md) (function, `0x003D9D10`)

### Direct callers
- [KiSaveExtendedAndSupervisorState](KiSaveExtendedAndSupervisorState_function_003D9A1C.md) at `0x003D9C49`
- [KeSaveSupervisorState](../5B/KeSaveSupervisorState_function_005B9CB4.md) at `0x005B9D25`
- [sub_009A6B68](../../page/9A/Unknown_function_009A6B68.md) at `0x009A6BAD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003D8CE4  48 83 EC 28                     sub rsp, 0x28
003D8CE8  A1 EC 03 00 00 80 F7 FF FF      movabs eax, dword ptr [0xfffff780000003ec]
003D8CF1  4C 8B C2                        mov r8, rdx
003D8CF4  A8 02                           test al, 2
003D8CF6  74 32                           je 0x1403d8d2a
003D8CF8  48 BA 00 00 00 00 00 00 00 80   movabs rdx, 0x8000000000000000
003D8D02  33 C0                           xor eax, eax
003D8D04  48 09 91 08 02 00 00            or qword ptr [rcx + 0x208], rdx
003D8D0B  33 D2                           xor edx, edx
003D8D0D  0F C7 19                        xrstors ptr [rcx]
003D8D10  4C 23 81 08 02 00 00            and r8, qword ptr [rcx + 0x208]
003D8D17  49 8B D0                        mov rdx, r8
003D8D1A  49 8B C0                        mov rax, r8
003D8D1D  48 C1 EA 20                     shr rdx, 0x20
003D8D21  0F C7 29                        xsaves ptr [rcx]
003D8D24  48 83 C4 28                     add rsp, 0x28
003D8D28  C3                              ret
003D8D29  CC                              int3
003D8D2A  E8 E1 0F 00 00                  call 0x1403d9d10
003D8D2F  EB F3                           jmp 0x1403d8d24
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlXSaveS(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((((unsigned __int8)(result)) & (2)) == 0) goto loc_003D8D2A;
    result = 0;
    a2 = 0;
    a3 = (a2) & (*(unsigned __int64 *)(a1 + 520));
    a2 = (a3) >> (32);
loc_003D8D24:
    v_rsp = (v_rsp) + (40);
    return a3;
loc_003D8D2A:
    result = RtlXSave(a1, a2, a3, a4);
    goto loc_003D8D24;
}
```

## 5. (Beta) C Style

```c
int64_t RtlXSaveS(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((((uint8_t)(result)) & (2)) == 0) goto loc_003D8D2A;
    result = 0;
    Arg2 = 0;
    a3 = (Arg2) & (*(uint64_t *)(arg1 + 0x208));
    Arg2 = (a3) >> (32);
loc_003D8D24:
    local_rsp = (local_rsp) + (40);
    return a3;
loc_003D8D2A:
    result = RtlXSave(Arg1, Arg2, a3, a4);
    goto loc_003D8D24;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x208` | `64` | `R` |
| `Arg1` | `+ 0x208` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003D8CE4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003D8CE4[BB_003D8CE4]
  bb_003D8CF8[BB_003D8CF8]
  bb_003D8D24[BB_003D8D24]
  bb_003D8D29[BB_003D8D29]
  bb_003D8D2A[BB_003D8D2A]
  bb_003D8CE4 -->|branch| bb_003D8D2A
  bb_003D8CE4 -->|fallthrough| bb_003D8CF8
  bb_003D8CF8 -->|flow| bb_003D8D24
  bb_003D8D29 -->|flow| bb_003D8D2A
  bb_003D8D2A -->|branch| bb_003D8D24
```
