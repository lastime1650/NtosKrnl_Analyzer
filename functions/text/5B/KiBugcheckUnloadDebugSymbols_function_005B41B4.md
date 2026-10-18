# KiBugcheckUnloadDebugSymbols

- RVA: `0x005B41B4`–`0x005B41D5` (길이 `33` bytes)
- VA: `0x00000001405B41B4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005B41CA` → [DbgUnLoadImageSymbols](../4C/DbgUnLoadImageSymbols_function_004C6690.md) (function, `0x004C6690`)

### Direct callers
- [KeBugCheck2](KeBugCheck2_function_005B27D0.md) at `0x005B375C`
- [ExRebootSystemForRecovery](../65/ExRebootSystemForRecovery_function_00655924.md) at `0x006559C1`

### Static image references
- `0x005B41B8` → RVA `0x00E667E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B41B4  48 83 EC 28                     sub rsp, 0x28
005B41B8  80 3D 29 26 8B 00 00            cmp byte ptr [rip + 0x8b2629], 0
005B41BF  75 0E                           jne 0x1405b41cf
005B41C1  45 33 C0                        xor r8d, r8d
005B41C4  48 83 CA FF                     or rdx, 0xffffffffffffffff
005B41C8  33 C9                           xor ecx, ecx
005B41CA  E8 C1 24 F1 FF                  call 0x1404c6690
005B41CF  48 83 C4 28                     add rsp, 0x28
005B41D3  C3                              ret
005B41D4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiBugcheckUnloadDebugSymbols(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int8 *)(v_rip + 9119273)) == 0) {
        a3 = 0;
        a2 = (a2) | (-1);
        a1 = 0;
        result = DbgUnLoadImageSymbols(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiBugcheckUnloadDebugSymbols(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint8_t *)(v_rip + 0x8B2629)) == 0) {
        Arg3 = 0;
        Arg2 = (Arg2) | (-1);
        Arg1 = 0;
        result = DbgUnLoadImageSymbols(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B41B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B41B4[BB_005B41B4]
  bb_005B41C1[BB_005B41C1]
  bb_005B41CF[BB_005B41CF]
  bb_005B41D4[BB_005B41D4]
  bb_005B41B4 -->|branch| bb_005B41CF
  bb_005B41B4 -->|fallthrough| bb_005B41C1
  bb_005B41C1 -->|flow| bb_005B41CF
```
