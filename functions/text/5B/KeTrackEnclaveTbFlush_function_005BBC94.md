# KeTrackEnclaveTbFlush

- RVA: `0x005BBC94`–`0x005BBCC9` (길이 `53` bytes)
- VA: `0x00000001405BBC94`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CA254`
- 디코드: `16`개 명령, `53/53` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005BBCAE` → [KiEncls](../6B/KiEncls_function_006B1BE0.md) (function, `0x006B1BE0`)
- `0x005BBCB5` → [KiEnclsStatus](../36/KiEnclsStatus_function_00368E1C.md) (function, `0x00368E1C`)

### Direct callers
- [MiProtectEnclavePages](../4D/MiProtectEnclavePages_function_004D5528.md) at `0x004D5AD2`
- [sub_006E362E](../6E/Unknown_function_006E362E.md) at `0x006E364C`

### Static image references
- `0x005BBC98` → RVA `0x00FC6B30` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005BBC94  48 83 EC 28                     sub rsp, 0x28
005BBC98  48 0F BA 25 8F AE A0 00 28      bt qword ptr [rip + 0xa0ae8f], 0x28
005BBCA1  73 1B                           jae 0x1405bbcbe
005BBCA3  45 33 C9                        xor r9d, r9d
005BBCA6  4C 8B C1                        mov r8, rcx
005BBCA9  33 D2                           xor edx, edx
005BBCAB  8D 4A 0C                        lea ecx, [rdx + 0xc]
005BBCAE  E8 2D 5F 0F 00                  call 0x1406b1be0
005BBCB3  8B C8                           mov ecx, eax
005BBCB5  E8 62 D1 DA FF                  call 0x140368e1c
005BBCBA  EB 07                           jmp 0x1405bbcc3
005BBCBC  EB 05                           jmp 0x1405bbcc3
005BBCBE  B8 BB 00 00 C0                  mov eax, 0xc00000bb
005BBCC3  48 83 C4 28                     add rsp, 0x28
005BBCC7  C3                              ret
005BBCC8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeTrackEnclaveTbFlush(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (condition_is_above_or_equal) goto loc_005BBCBE;
    a4 = 0;
    a2 = 0;
    result = KiEncls(a2 + 12, a2, a1, a4);
    result = KiEnclsStatus((unsigned int)((unsigned int)(result)), a2, a1, a4);
    goto loc_005BBCC3;
loc_005BBCBE:
loc_005BBCC3:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(0xC00000BBULL);
}
```

## 5. (Beta) C Style

```c
int64_t KeTrackEnclaveTbFlush(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (condition_is_above_or_equal) goto loc_005BBCBE;
    Arg4 = 0;
    Arg2 = 0;
    result = KiEncls(Arg2 + 12, Arg2, Arg1, Arg4);
    result = KiEnclsStatus((uint32_t)((uint32_t)(result)), Arg2, Arg1, Arg4);
    goto loc_005BBCC3;
loc_005BBCBE:
loc_005BBCC3:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(0xC00000BBULL);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005BBC94&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005BBC94[BB_005BBC94]
  bb_005BBCA3[BB_005BBCA3]
  bb_005BBCBC[BB_005BBCBC]
  bb_005BBCBE[BB_005BBCBE]
  bb_005BBCC3[BB_005BBCC3]
  bb_005BBCC8[BB_005BBCC8]
  bb_005BBC94 -->|branch| bb_005BBCBE
  bb_005BBC94 -->|fallthrough| bb_005BBCA3
  bb_005BBCA3 -->|branch| bb_005BBCC3
  bb_005BBCBC -->|branch| bb_005BBCC3
  bb_005BBCBE -->|flow| bb_005BBCC3
```
