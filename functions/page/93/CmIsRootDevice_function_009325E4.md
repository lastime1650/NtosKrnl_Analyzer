# CmIsRootDevice

- RVA: `0x009325E4`–`0x0093261F` (길이 `59` bytes)
- VA: `0x00000001409325E4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008EE54`
- 디코드: `17`개 명령, `59/59` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x009325F8` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x00932610` → [RtlEqualUnicodeString](RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)

### Direct callers
- [PiDcResetChildDeviceContainerCallback](../73/PiDcResetChildDeviceContainerCallback_function_00730DE0.md) at `0x00730E36`
- [PiCMDeleteDeviceWorker](../73/PiCMDeleteDeviceWorker_function_0073B420.md) at `0x0073B471`
- [sub_008E80AE](../8E/Unknown_function_008E80AE.md) at `0x008E8183`
- [_CmSetDeviceRegPropWorker](../8F/_CmSetDeviceRegPropWorker_function_008FD804.md) at `0x008FDA8F`
- [CmGetDeviceParent](CmGetDeviceParent_function_00932368.md) at `0x009323BD`
- [_CmUpdateDevicePanel](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) at `0x00A0A227`
- [_CmSetDeviceMappedProperty](../A0/_CmSetDeviceMappedProperty_function_00A0B098.md) at `0x00A0B0CE`
- [PiCMCreateDevice](../AC/PiCMCreateDevice_function_00ACB824.md) at `0x00ACB944`
- [PiCMQueryRemove](../AD/PiCMQueryRemove_function_00AD43F4.md) at `0x00AD44EE`
- [sub_00B284C0](../B2/Unknown_function_00B284C0.md) at `0x00B28625`

### Static image references
- `0x00932604` → RVA `0x000021E0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009325F8` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009325E4  48 83 EC 38                     sub rsp, 0x38
009325E8  0F 57 C0                        xorps xmm0, xmm0
009325EB  48 8B D1                        mov rdx, rcx
009325EE  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
009325F3  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
009325F8  E8 63 13 B3 FF                  call 0x140463960
009325FD  85 C0                           test eax, eax
009325FF  78 1A                           js 0x14093261b
00932601  41 B0 01                        mov r8b, 1
00932604  48 8D 15 D5 FB 6C FF            lea rdx, [rip - 0x93042b]
0093260B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00932610  E8 0B 04 00 00                  call 0x140932a20
00932615  48 83 C4 38                     add rsp, 0x38
00932619  C3                              ret
0093261A  CC                              int3
0093261B  32 C0                           xor al, al
0093261D  EB F6                           jmp 0x140932615
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmIsRootDevice(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    v_stack_m18 = v_xmm0;
    result = RtlInitUnicodeStringEx(v_stack_m18, a1, a3, a4);
    if (sign_flag) goto loc_0093261B;
    result = RtlEqualUnicodeString(v_stack_m18, v_rip - 9634859, 1, a4);
loc_00932615:
    v_rsp = (v_rsp) + (56);
    return result;
loc_0093261B:
    result = 0;
    goto loc_00932615;
}
```

## 5. (Beta) C Style

```c
int64_t CmIsRootDevice(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    v_stack_m18 = v_xmm0;
    result = RtlInitUnicodeStringEx(v_stack_m18, Arg1, a3, a4);
    if (sign_flag) goto loc_0093261B;
    result = RtlEqualUnicodeString(v_stack_m18, v_rip - 9634859, 1, a4);
loc_00932615:
    local_rsp = (local_rsp) + (56);
    return result;
loc_0093261B:
    result = 0;
    goto loc_00932615;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009325E4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009325E4[BB_009325E4]
  bb_00932601[BB_00932601]
  bb_00932615[BB_00932615]
  bb_0093261A[BB_0093261A]
  bb_0093261B[BB_0093261B]
  bb_009325E4 -->|branch| bb_0093261B
  bb_009325E4 -->|fallthrough| bb_00932601
  bb_00932601 -->|flow| bb_00932615
  bb_0093261A -->|flow| bb_0093261B
  bb_0093261B -->|branch| bb_00932615
```
