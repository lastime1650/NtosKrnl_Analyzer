# RtlpSetFunctionOverrideCapability

- RVA: `0x00795658`–`0x00795690` (길이 `56` bytes)
- VA: `0x0000000140795658`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D01FC`
- 디코드: `17`개 명령, `56/56` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0079566F` → [RtlpGetCapabilityBitmap<_RTL_FUNCTION_OVERRIDE_CAPABILITIES,unsigned char>](RtlpGetCapabilityBitmap__RTL_FUNCTION_OVERRIDE_CAPABILITIES_unsigned_char__function_007954AC.md) (function, `0x007954AC`)

### Direct callers
- [RtlpSetUserKernelFunctionOverrideCapability](RtlpSetUserKernelFunctionOverrideCapability_function_00795698.md) at `0x007956A2`
- [RtlpSetUserKernelFunctionOverrideCapability](RtlpSetUserKernelFunctionOverrideCapability_function_00795698.md) at `0x007956AD`
- [RtlpInitFunctionOverrideCapabilities](RtlpInitFunctionOverrideCapabilities_function_0079AC60.md) at `0x0079AD6A`
- [RtlpInitFunctionOverrideCapabilities](RtlpInitFunctionOverrideCapabilities_function_0079AC60.md) at `0x0079AD7D`
- [RtlpInitFunctionOverrideCapabilities](RtlpInitFunctionOverrideCapabilities_function_0079AC60.md) at `0x0079AE18`
- [RtlpInitFunctionOverrideCapabilities](RtlpInitFunctionOverrideCapabilities_function_0079AC60.md) at `0x0079AE25`
- [RtlpInitFunctionOverrideCapabilities](RtlpInitFunctionOverrideCapabilities_function_0079AC60.md) at `0x0079AE32`
- [RtlpInitFunctionOverrideCapabilities](RtlpInitFunctionOverrideCapabilities_function_0079AC60.md) at `0x0079AE49`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00795658  48 8B C4                        mov rax, rsp
0079565B  89 48 08                        mov dword ptr [rax + 8], ecx
0079565E  48 83 EC 28                     sub rsp, 0x28
00795662  48 83 60 20 00                  and qword ptr [rax + 0x20], 0
00795667  4C 8D 48 20                     lea r9, [rax + 0x20]
0079566B  48 8D 48 08                     lea rcx, [rax + 8]
0079566F  E8 38 FE FF FF                  call 0x1407954ac
00795674  84 C0                           test al, al
00795676  74 12                           je 0x14079568a
00795678  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0079567D  48 85 C9                        test rcx, rcx
00795680  74 08                           je 0x14079568a
00795682  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00795686  48 0F AB 01                     bts qword ptr [rcx], rax
0079568A  48 83 C4 28                     add rsp, 0x28
0079568E  C3                              ret
0079568F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpSetFunctionOverrideCapability(int a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (40);
    result = RtlpGetCapabilityBitmap__RTL_FUNCTION_OVERRIDE_CAPABILITIES_unsigned_char_(v_rsp + 8, a2, a3, v_rsp + 32);
    if ((unsigned __int8)(result) == 0) goto loc_0079568A;
    if (v_stack_p20 != 0) {
        result = v_stack_p8;
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpSetFunctionOverrideCapability(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (40);
    result = RtlpGetCapabilityBitmap__RTL_FUNCTION_OVERRIDE_CAPABILITIES_unsigned_char_(local_rsp + 8, a2, a3, local_rsp + 32);
    if ((uint8_t)(result) == 0) goto loc_0079568A;
    if (v_stack_p20 != 0) {
        result = v_stack_p8;
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00795658&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00795658[BB_00795658]
  bb_00795678[BB_00795678]
  bb_00795682[BB_00795682]
  bb_0079568A[BB_0079568A]
  bb_0079568F[BB_0079568F]
  bb_00795658 -->|branch| bb_0079568A
  bb_00795658 -->|fallthrough| bb_00795678
  bb_00795678 -->|branch| bb_0079568A
  bb_00795678 -->|fallthrough| bb_00795682
  bb_00795682 -->|flow| bb_0079568A
```
