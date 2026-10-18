# EmpSearchEntryDatabase

- RVA: `0x00580CE8`–`0x00580D1A` (길이 `50` bytes)
- VA: `0x0000000140580CE8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `17`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [EmProviderRegisterEntry](../../page/71/EmProviderRegisterEntry_function_00713300.md) at `0x007133AA`
- [EmpProviderRegister](../../page/AC/EmpProviderRegister_function_00ACC5D0.md) at `0x00ACC737`
- [EmpParseCallbacks](../../init/C2/EmpParseCallbacks_function_00C2657C.md) at `0x00C26711`
- [EmpParseEntryTypes](../../init/C2/EmpParseEntryTypes_function_00C267B4.md) at `0x00C2689E`
- [EmpParseRules](../../init/C2/EmpParseRules_function_00C2745C.md) at `0x00C27652`

### Static image references
- `0x00580CE8` → RVA `0x00F8F198` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00580CE8  48 8B 15 A9 E4 A0 00            mov rdx, qword ptr [rip + 0xa0e4a9]
00580CEF  EB 1C                           jmp 0x140580d0d
00580CF1  4C 8D 42 E8                     lea r8, [rdx - 0x18]
00580CF5  4D 8B 08                        mov r9, qword ptr [r8]
00580CF8  4C 2B 09                        sub r9, qword ptr [rcx]
00580CFB  75 08                           jne 0x140580d05
00580CFD  4D 8B 48 08                     mov r9, qword ptr [r8 + 8]
00580D01  4C 2B 49 08                     sub r9, qword ptr [rcx + 8]
00580D05  4D 85 C9                        test r9, r9
00580D08  74 0B                           je 0x140580d15
00580D0A  48 8B 12                        mov rdx, qword ptr [rdx]
00580D0D  45 33 C0                        xor r8d, r8d
00580D10  48 85 D2                        test rdx, rdx
00580D13  75 DC                           jne 0x140580cf1
00580D15  49 8B C0                        mov rax, r8
00580D18  C3                              ret
00580D19  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EmpSearchEntryDatabase(__int64 a1)
{
    goto loc_00580D0D;
loc_00580CF1:
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10544297) - 24)) - (*(unsigned __int64 *)(a1));
    if (!(condition_is_not_equal)) {
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10544297) - 24 + 8);
        a4 = (a4) - (*(unsigned __int64 *)(a1 + 8));
    }
    if (a4 == 0) goto loc_00580D15;
loc_00580D0D:
    a3 = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10544297)) != 0) goto loc_00580CF1;
loc_00580D15:
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t EmpSearchEntryDatabase(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    goto loc_00580D0D;
loc_00580CF1:
    a4 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA0E4A9) - 0x18)) - (*(uint64_t *)(arg1));
    if (!(condition_is_not_equal)) {
        a4 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xA0E4A9) - 0x18 + 0x8);
        a4 = (a4) - (*(uint64_t *)(arg1 + 0x8));
    }
    if (a4 == 0) goto loc_00580D15;
loc_00580D0D:
    a3 = 0;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA0E4A9)) != 0) goto loc_00580CF1;
loc_00580D15:
    return 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00580CE8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00580CE8[BB_00580CE8]
  bb_00580CF1[BB_00580CF1]
  bb_00580CFD[BB_00580CFD]
  bb_00580D05[BB_00580D05]
  bb_00580D0A[BB_00580D0A]
  bb_00580D0D[BB_00580D0D]
  bb_00580D15[BB_00580D15]
  bb_00580D19[BB_00580D19]
  bb_00580CE8 -->|branch| bb_00580D0D
  bb_00580CF1 -->|branch| bb_00580D05
  bb_00580CF1 -->|fallthrough| bb_00580CFD
  bb_00580CFD -->|flow| bb_00580D05
  bb_00580D05 -->|branch| bb_00580D15
  bb_00580D05 -->|fallthrough| bb_00580D0A
  bb_00580D0A -->|flow| bb_00580D0D
  bb_00580D0D -->|branch| bb_00580CF1
  bb_00580D0D -->|fallthrough| bb_00580D15
```
