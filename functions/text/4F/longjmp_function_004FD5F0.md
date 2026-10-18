# longjmp

- RVA: `0x004FD5F0`–`0x004FD622` (길이 `50` bytes)
- VA: `0x00000001404FD5F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `16`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **23**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004FD607` → [KeCheckStackAndTargetAddress](../43/KeCheckStackAndTargetAddress_function_0043E580.md) (function, `0x0043E580`)
- `0x004FD611` → [_longjmp_internal](../6A/_longjmp_internal_function_006AC6D0.md) (function, `0x006AC6D0`)

### Direct callers
- [XmPopStack](../47/XmPopStack_function_00472588.md) at `0x004725AD`
- [XmGroup45General](../47/XmGroup45General_function_00472A80.md) at `0x00472B10`
- [XmGetStringAddressRange](../47/XmGetStringAddressRange_function_00472B88.md) at `0x00472C85`
- [XmOutOp](../47/XmOutOp_function_00472DB0.md) at `0x00472DF1`
- [XmPushStack](../47/XmPushStack_function_00473088.md) at `0x004730E0`
- [XmGetWordImmediate](../47/XmGetWordImmediate_function_004731DC.md) at `0x00473217`
- [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) at `0x004736A8`
- [XmInOp](../47/XmInOp_function_004737F0.md) at `0x00473837`
- [XmGetLongImmediate](../56/XmGetLongImmediate_function_0056DC70.md) at `0x0056DC90`
- [XmEffectiveOffset](../57/XmEffectiveOffset_function_00576180.md) at `0x005761C6`
- [XmGeneralRegister](../57/XmGeneralRegister_function_005762B0.md) at `0x005762EF`
- [XmGroup7General](../57/XmGroup7General_function_00576490.md) at `0x005764C7`
- [XmLoadSegment](../57/XmLoadSegment_function_005766C0.md) at `0x00576711`
- [XmEnterOp](../57/XmEnterOp_function_00577A10.md) at `0x00577A73`
- [XmHltOp](../57/XmHltOp_function_00577AC0.md) at `0x00577AD0`
- [XmBoundOp](../57/XmBoundOp_function_005782E0.md) at `0x00578377`
- [XmIllOp](../57/XmIllOp_function_005783B0.md) at `0x005783C0`
- [XmDivOp](../57/XmDivOp_function_005786A0.md) at `0x005786C1`
- [XmDivOp](../57/XmDivOp_function_005786A0.md) at `0x00578743`
- [XmIdivOp](../57/XmIdivOp_function_00578770.md) at `0x0057878B`
- [XmIdivOp](../57/XmIdivOp_function_00578770.md) at `0x00578870`
- [XmEvaluateIndexSpecifier](../57/XmEvaluateIndexSpecifier_function_00578928.md) at `0x00578B16`
- [XmGetOffsetAddress](../57/XmGetOffsetAddress_function_00578B84.md) at `0x00578BC0`
- [XmGetStringAddress](../57/XmGetStringAddress_function_00578BCC.md) at `0x00578C4C`
- [sub_006F3DB6](../6F/Unknown_function_006F3DB6.md) at `0x006F4163`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FD5F0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004FD5F5  57                              push rdi
004FD5F6  48 83 EC 20                     sub rsp, 0x20
004FD5FA  8B DA                           mov ebx, edx
004FD5FC  48 8B F9                        mov rdi, rcx
004FD5FF  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
004FD603  48 8B 49 50                     mov rcx, qword ptr [rcx + 0x50]
004FD607  E8 74 0F F4 FF                  call 0x14043e580
004FD60C  8B D3                           mov edx, ebx
004FD60E  48 8B CF                        mov rcx, rdi
004FD611  E8 BA F0 1A 00                  call 0x1406ac6d0
004FD616  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004FD61B  48 83 C4 20                     add rsp, 0x20
004FD61F  5F                              pop rdi
004FD620  C3                              ret
004FD621  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall longjmp(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = KeCheckStackAndTargetAddress(*(unsigned __int64 *)(a1 + 80), *(unsigned __int64 *)(a1 + 16), a3, a4);
    result = _longjmp_internal(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t longjmp(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = KeCheckStackAndTargetAddress(*(uint64_t *)(arg1 + 0x50), *(uint64_t *)(arg1 + 0x10), a3, a4);
    result = _longjmp_internal(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FD5F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FD5F0[BB_004FD5F0]
  bb_004FD621[BB_004FD621]
```
