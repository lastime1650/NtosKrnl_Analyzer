# DbgLoadImageSymbolsUnicode

- RVA: `0x004AE0BC`–`0x004AE10B` (길이 `79` bytes)
- VA: `0x00000001404AE0BC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B8594`
- 디코드: `24`개 명령, `79/79` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004AE0D5` → [DbgUnicodeStringToAnsiString](DbgUnicodeStringToAnsiString_function_004AE190.md) (function, `0x004AE190`)
- `0x004AE0EA` → [DbgLoadImageSymbols](DbgLoadImageSymbols_function_004AE220.md) (function, `0x004AE220`)
- `0x004AE0F6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MiCacheImageSymbols](../../page/AD/MiCacheImageSymbols_function_00AD9410.md) at `0x00AD9550`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004AE0F6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004AE0BC  40 53                           push rbx
004AE0BE  48 83 EC 30                     sub rsp, 0x30
004AE0C2  48 8B DA                        mov rbx, rdx
004AE0C5  0F 57 C0                        xorps xmm0, xmm0
004AE0C8  48 8B D1                        mov rdx, rcx
004AE0CB  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
004AE0D0  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
004AE0D5  E8 B6 00 00 00                  call 0x1404ae190
004AE0DA  85 C0                           test eax, eax
004AE0DC  74 29                           je 0x1404ae107
004AE0DE  49 83 C8 FF                     or r8, 0xffffffffffffffff
004AE0E2  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
004AE0E7  48 8B D3                        mov rdx, rbx
004AE0EA  E8 31 01 00 00                  call 0x1404ae220
004AE0EF  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
004AE0F4  33 D2                           xor edx, edx
004AE0F6  E8 75 47 6D 00                  call 0x140b82870
004AE0FB  B8 01 00 00 00                  mov eax, 1
004AE100  48 83 C4 30                     add rsp, 0x30
004AE104  5B                              pop rbx
004AE105  C3                              ret
004AE106  CC                              int3
004AE107  33 C0                           xor eax, eax
004AE109  EB F5                           jmp 0x1404ae100
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DbgLoadImageSymbolsUnicode(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (48);
    v_stack_m18 = v_xmm0;
    result = DbgUnicodeStringToAnsiString(v_stack_m18, a1, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_004AE107;
    a3 = (a3) | (-1);
    result = DbgLoadImageSymbols(v_stack_m18, a2, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m10, a2, a3, a4);
loc_004AE100:
    v_rsp = (v_rsp) + (48);
    return 1;
loc_004AE107:
    result = 0;
    goto loc_004AE100;
}
```

## 5. (Beta) C Style

```c
int64_t DbgLoadImageSymbolsUnicode(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (48);
    v_stack_m18 = v_xmm0;
    result = DbgUnicodeStringToAnsiString(v_stack_m18, Arg1, Arg3, a4);
    if ((uint32_t)(result) == 0) goto loc_004AE107;
    Arg3 = (Arg3) | (-1);
    result = DbgLoadImageSymbols(v_stack_m18, Arg2, Arg3, a4);
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m10, Arg2, Arg3, a4);
loc_004AE100:
    local_rsp = (local_rsp) + (48);
    return 1;
loc_004AE107:
    result = 0;
    goto loc_004AE100;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004AE0BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004AE0BC[BB_004AE0BC]
  bb_004AE0DE[BB_004AE0DE]
  bb_004AE100[BB_004AE100]
  bb_004AE106[BB_004AE106]
  bb_004AE107[BB_004AE107]
  bb_004AE0BC -->|branch| bb_004AE107
  bb_004AE0BC -->|fallthrough| bb_004AE0DE
  bb_004AE0DE -->|flow| bb_004AE100
  bb_004AE106 -->|flow| bb_004AE107
  bb_004AE107 -->|branch| bb_004AE100
```
