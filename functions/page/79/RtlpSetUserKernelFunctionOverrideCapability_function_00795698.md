# RtlpSetUserKernelFunctionOverrideCapability

- RVA: `0x00795698`–`0x007956B8` (길이 `32` bytes)
- VA: `0x0000000140795698`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007956A2` → [RtlpSetFunctionOverrideCapability](RtlpSetFunctionOverrideCapability_function_00795658.md) (function, `0x00795658`)
- `0x007956AD` → [RtlpSetFunctionOverrideCapability](RtlpSetFunctionOverrideCapability_function_00795658.md) (function, `0x00795658`)

### Direct callers
- [RtlpInitFunctionOverrideCapabilities](RtlpInitFunctionOverrideCapabilities_function_0079AC60.md) at `0x0079ADC0`
- [RtlpInitFunctionOverrideCapabilities](RtlpInitFunctionOverrideCapabilities_function_0079AC60.md) at `0x0079ADCA`
- [RtlpInitFunctionOverrideCapabilities](RtlpInitFunctionOverrideCapabilities_function_0079AC60.md) at `0x0079ADDD`
- [RtlpInitFunctionOverrideCapabilities](RtlpInitFunctionOverrideCapabilities_function_0079AC60.md) at `0x0079ADED`
- [RtlpInitFunctionOverrideCapabilities](RtlpInitFunctionOverrideCapabilities_function_0079AC60.md) at `0x0079ADFD`
- [RtlpInitFunctionOverrideCapabilities](RtlpInitFunctionOverrideCapabilities_function_0079AC60.md) at `0x0079AE0C`
- [RtlpInitFunctionOverrideCapabilities](RtlpInitFunctionOverrideCapabilities_function_0079AC60.md) at `0x0079AE3C`
- [RtlpInitFunctionOverrideCapabilities](RtlpInitFunctionOverrideCapabilities_function_0079AC60.md) at `0x0079AE95`
- [RtlpInitFunctionOverrideCapabilities](RtlpInitFunctionOverrideCapabilities_function_0079AC60.md) at `0x0079AEA2`
- [RtlpInitFunctionOverrideCapabilities](RtlpInitFunctionOverrideCapabilities_function_0079AC60.md) at `0x0079AEAC`
- [RtlpInitFunctionOverrideCapabilities](RtlpInitFunctionOverrideCapabilities_function_0079AC60.md) at `0x0079AEB6`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00795698  48 83 EC 28                     sub rsp, 0x28
0079569C  45 33 C0                        xor r8d, r8d
0079569F  44 8B D9                        mov r11d, ecx
007956A2  E8 B1 FF FF FF                  call 0x140795658
007956A7  41 8B CB                        mov ecx, r11d
007956AA  41 B0 01                        mov r8b, 1
007956AD  E8 A6 FF FF FF                  call 0x140795658
007956B2  48 83 C4 28                     add rsp, 0x28
007956B6  C3                              ret
007956B7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpSetUserKernelFunctionOverrideCapability(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a3 = 0;
    result = RtlpSetFunctionOverrideCapability(a1, a2, a3, a4);
    result = RtlpSetFunctionOverrideCapability((unsigned int)((unsigned int)((unsigned int)(a1))), a2, 1, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpSetUserKernelFunctionOverrideCapability(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg3 = 0;
    result = RtlpSetFunctionOverrideCapability(Arg1, Arg2, Arg3, a4);
    result = RtlpSetFunctionOverrideCapability((uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, 1, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00795698&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00795698[BB_00795698]
  bb_007956B7[BB_007956B7]
```
