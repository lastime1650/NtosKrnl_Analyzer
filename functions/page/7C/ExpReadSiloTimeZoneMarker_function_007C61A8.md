# ExpReadSiloTimeZoneMarker

- RVA: `0x007C61A8`–`0x007C61D2` (길이 `42` bytes)
- VA: `0x00000001407C61A8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007C61BF` → [ExpReadTimeZoneInformation](ExpReadTimeZoneInformation_function_007C61D8.md) (function, `0x007C61D8`)

### Direct callers
- [ExpSetTimeZoneInformation](ExpSetTimeZoneInformation_function_007C5240.md) at `0x007C5489`
- [ExpRefreshTimeZoneInformation](../A6/ExpRefreshTimeZoneInformation_function_00A6B46C.md) at `0x00A6B50F`
- [ExpRefreshTimeZoneInformation](../A6/ExpRefreshTimeZoneInformation_function_00A6B46C.md) at `0x00A6B54F`

### Static image references
- `0x007C61B8` → RVA `0x00038E20` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007C61A8  48 83 EC 28                     sub rsp, 0x28
007C61AC  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
007C61B1  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
007C61B6  33 D2                           xor edx, edx
007C61B8  48 8D 0D 61 2C 87 FF            lea rcx, [rip - 0x78d39f]
007C61BF  E8 14 00 00 00                  call 0x1407c61d8
007C61C4  83 7C 24 30 00                  cmp dword ptr [rsp + 0x30], 0
007C61C9  0F 95 C0                        setne al
007C61CC  48 83 C4 28                     add rsp, 0x28
007C61D0  C3                              ret
007C61D1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpReadSiloTimeZoneMarker(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    result = ExpReadTimeZoneInformation(v_rip - 7918495, a2, v_stack_p8, a4);
    result = (v_stack_p8 != 0) ? 1 : 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpReadSiloTimeZoneMarker(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    result = ExpReadTimeZoneInformation(v_rip - 7918495, Arg2, v_stack_p8, a4);
    result = (v_stack_p8 != 0) ? 1 : 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007C61A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007C61A8[BB_007C61A8]
  bb_007C61D1[BB_007C61D1]
```
